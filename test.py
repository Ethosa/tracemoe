# -*- coding: utf-8 -*-
# authors: Ethosa
import asyncio

from tracemoe import ATraceMoe


async def main():
    response = await tracemoe.search(
        "https://randomc.net/image/Hanayamata/Hanayamata%20-%2004%20-%20Large%2015.jpg",
        is_url=True
    )
    video = await tracemoe.video_preview_natural(response)

    with open("async_video.mp4", "wb") as f:
        f.write(video)


if __name__ == "__main__":
    tracemoe = ATraceMoe()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
