import asyncio
import utils

import cfg
import handlers.leading_handler as lh


async def main():
    logger = utils.create_file_logger(__name__)

    server = await asyncio.start_server(lh.hand, cfg.SERVER_ADDRESS, cfg.SERVER_PORT)
    self_address = server.sockets[0].getsockname()
    logger.info(f'Running at {self_address}')

    async with server:
        await server.serve_forever()


asyncio.run(main())
