import nox

PYTHON_VERSION = "3.11"
SUPPORTED_VERSIONS = ["3.11"]
BLACK_ARGS = ["black", "src/", "tests/", "scripts/"]
ISORT_ARGS = ["isort", "src/", "tests/", "scripts/"]
LOCAL_PACKAGE = "."
DEV_DEPS = [
    "black >= 23.1.0",
    "docker >= 6.0.1",
    "bumpversion >= 0.6.0",
    "flake8 >= 6.0.0",
    "grpcio-tools >= 1.53.0",
    "grpc-stubs >= 1.53",
    "isort >= 5.12.0",
    "mypy >= 1.2.0",
    "mypy-extensions >= 1.0.0",
    "mypy-protobuf >= 3.4.0",
    "pydantic >= 1.10.5",
    "pytest >= 7.2.1",
    "pytest-asyncio >= 0.20.3",
    "sqlalchemy[mypy]",
    "testcontainers-postgres >= 0.0.1rc1",
    "types-protobuf >= 4.22.0.2",
]

nox.options.sessions = ["dev"]


@nox.session(python=PYTHON_VERSION, reuse_venv=True)
def dev(session):
    session.install("nox")
    session.install(*DEV_DEPS)
    session.install("-e", LOCAL_PACKAGE)


@nox.session(python=SUPPORTED_VERSIONS, reuse_venv=True)
def tests(session):
    session.install(*DEV_DEPS)
    session.install("-e", LOCAL_PACKAGE)
    session.run("pytest", "tests/")


@nox.session(python=PYTHON_VERSION, reuse_venv=True)
def clean(session):
    session.install(*DEV_DEPS)
    session.install("-e", LOCAL_PACKAGE)
    session.run(*BLACK_ARGS)
    session.run(*ISORT_ARGS)


@nox.session(python=PYTHON_VERSION, reuse_venv=True)
def flake8(session):
    session.install(*DEV_DEPS)
    session.install("-e", LOCAL_PACKAGE)
    session.run("flake8", "--version")
    session.run("flake8", "src/", "tests/")


@nox.session(python=PYTHON_VERSION, reuse_venv=True)
def black(session):
    session.install(*DEV_DEPS)
    session.install("-e", LOCAL_PACKAGE)
    session.run("black", "--version")
    session.run(*BLACK_ARGS, "--check", "--diff")


@nox.session(python=PYTHON_VERSION, reuse_venv=True)
def isort(session):
    session.install(*DEV_DEPS)
    session.install("-e", LOCAL_PACKAGE)
    session.run(*ISORT_ARGS, "--diff", "--check-only")


@nox.session(python=PYTHON_VERSION, reuse_venv=True)
def mypy(session):
    session.install(*DEV_DEPS)
    session.install("-e", LOCAL_PACKAGE)
    session.run("mypy", "--strict", "--python-version", "3.11", "src/", "tests/")


@nox.session(python=PYTHON_VERSION, reuse_venv=True)
def protos(session):
    session.install(*DEV_DEPS)
    session.install("-e", LOCAL_PACKAGE)
    session.run("python", "scripts/protogen.py")
