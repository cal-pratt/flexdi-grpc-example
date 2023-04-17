import asyncio
import logging

from flexjob.server.server import serve


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(serve())
