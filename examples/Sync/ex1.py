# -*- coding: utf-8 -*-
# authors: Ethosa
# search anime by image url
from tracemoe import TraceMoe


if __name__ == "__main__":
    tracemoe = TraceMoe()
    response = tracemoe.search(
        "https://randomc.net/image/Hanayamata/Hanayamata%20-%2004%20-%20Large%2015.jpg",
        is_url=True
    )
    print(response)
