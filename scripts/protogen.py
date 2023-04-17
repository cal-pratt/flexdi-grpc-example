import pathlib
import shutil
import subprocess
import sys

import requests
import yaml

SCRIPT_PATH = pathlib.Path(__file__).absolute()
SCRIPT_DIR = SCRIPT_PATH.parent
PROTOS_CONF = SCRIPT_DIR.joinpath(pathlib.Path("protos.yaml"))


if __name__ == "__main__":
    with open(PROTOS_CONF, "r") as f:
        protos_conf = yaml.safe_load(f)

    proto_dir = SCRIPT_DIR.joinpath(pathlib.Path(protos_conf["proto_dir"]))
    python_dir = SCRIPT_DIR.joinpath(pathlib.Path(protos_conf["python_dir"]))
    python_package: str = protos_conf["python_package"]

    if python_dir.exists():
        shutil.rmtree(python_dir)

    proto_paths = []
    proto_packages = set()
    for proto in protos_conf["protos"]:
        path = pathlib.Path(proto["path"])
        package: str = proto["package"]

        proto_paths.append(proto_path := proto_dir.joinpath(path))
        proto_packages.add(package)
        proto_path.parent.mkdir(parents=True, exist_ok=True)

        if url := proto.get("url"):
            print(f"Downloading proto: {url}")
            res = requests.get(url)
            res.raise_for_status()

            with open(proto_dir.joinpath(path), "wb") as f:
                f.write(res.content)

        python_path = python_dir.joinpath(path).parent
        python_path.mkdir(parents=True, exist_ok=True)
        init_file = python_path.joinpath("__init__.py")

        if not init_file.exists():
            with open(init_file, "w") as f:
                f.write("# Generated __init__.py file\n")

    args = (
        f"{sys.executable} -m grpc_tools.protoc "
        f"-I{proto_dir} "
        f"--python_out={python_dir} "
        f"--grpc_python_out={python_dir} "
        f"--proto_path={proto_dir} "
        f"--mypy_out={python_dir} "
        f"--mypy_grpc_out={python_dir} "
    ).split() + list(map(str, proto_paths))

    join = " \\\n  "
    print(f"Running command: {join.join(args)}")
    if subprocess.run(args).returncode != 0:
        raise Exception("Failed to generate python code")

    print("Adjusting generated outputs...")

    for filepath in python_dir.rglob("*"):
        if not filepath.is_file():
            continue
        with open(filepath, "r") as f:
            contents = f.read()

        if filepath.name.endswith("_pb2.py") or filepath.name.endswith("_pb2_grpc.py"):
            for proto_package in proto_packages:
                contents = contents.replace(
                    f"from {proto_package} ",
                    f"from {python_package}.{proto_package} ",
                )
        if filepath.name.endswith("_pb2.pyi") or filepath.name.endswith(
            "_pb2_grpc.pyi"
        ):
            for proto in protos_conf["protos"]:
                pacakge = f"{proto['package']}.{proto['name']}"
                contents = contents.replace(
                    f"{pacakge}_pb2",
                    f"{python_package}.{pacakge}_pb2",
                )
        if filepath.name.endswith("_pb2_grpc.pyi"):
            contents = contents.replace(
                "import grpc",
                "import grpc.aio as grpc\nimport typing",
            )
            contents = contents.replace(
                "context: grpc.ServicerContext,",
                "context: grpc.ServicerContext[typing.Any, typing.Any],",
            )

        with open(filepath, "w") as f:
            f.write(contents)

    print("Complete!")
