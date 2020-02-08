# -*- coding: utf-8 -*-
# authors: Ethosa
# search anime by image url
import asyncio
from pprint import pprint

from tracemoe import ATraceMoe


async def main():
    response = await tracemoe.search(
        "https://randomc.net/image/Hanayamata/Hanayamata%20-%2004%20-%20Large%2015.jpg",
        is_url=True
    )
    pprint(response)


if __name__ == "__main__":
    tracemoe = ATraceMoe()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
