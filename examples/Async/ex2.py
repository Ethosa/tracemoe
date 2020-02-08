# -*- coding: utf-8 -*-
# authors: Ethosa
# get self info
import asyncio

from tracemoe import ATraceMoe


async def main():
    print(await tracemoe.me())


if __name__ == "__main__":
    tracemoe = ATraceMoe()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
