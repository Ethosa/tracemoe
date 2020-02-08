# -*- coding: utf-8 -*-
# authors: Ethosa
# get imae preview
import asyncio

from tracemoe import ATraceMoe


async def main():
    response = await tracemoe.search(
        "https://randomc.net/image/Hanayamata/Hanayamata%20-%2004%20-%20Large%2015.jpg",
        is_url=True
    )
    image = await tracemoe.image_preview(response)

    with open("async_image.png", "wb") as f:
        f.write(image)


if __name__ == "__main__":
    tracemoe = ATraceMoe()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
