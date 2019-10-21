import asyncio
import logging

logger = logging.basicConfig(level=logging.INFO)

import cfg
import handlers.leading_handler as lh


async def main():
    server = await asyncio.start_server(lh.hand, cfg.SERVER_ADDRESS, cfg.SERVER_PORT)
    self_address = server.sockets[0].getsockname()
    print(f'Running at {self_address}')

    async with server:
        await server.serve_forever()


asyncio.run(main())
