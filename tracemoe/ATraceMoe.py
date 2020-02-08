# -*- coding: utf-8 -*-
# authors: Ethosa
from json import loads
from base64 import b64encode

from aiohttp import ClientSession


class ATraceMoe:
    def __init__(self, token=""):
        """
        Initialize trace moe API.
        """
        self.api_url = "https://trace.moe/api/"
        self.main_url = "https://trace.moe/"
        self.media_url = "https://media.trace.moe/"
        self.token = token
        self.session = ClientSession()
        self.session.headers = {
            "Content-Type": "application/json"
        }

    async def me(self):
        """
        Gets limit for your IP.

        Returns:
            dict -- server response
        """
        url = "%sme" % (self.api_url)

        if self.token:
            url += "?token=%s" % (self.token)

        response = await self.session.get(url)

        return await response.json()

    async def image_preview(self, response, index=0, page="thumbnail.php"):
        """
        Gets image preview after server response.

        Arguments:
            response {dict} -- server response

        Returns:
            bytes -- content for the write-in file.
        """
        response = response["docs"][index]
        url = "%s%s?anilist_id=%s&file=%s&t=%s&token=%s" % (
            self.main_url, page, response["anilist_id"],
            response["filename"], response["at"], response["tokenthumb"]
        )
        response = await self.session.get(url)

        return await response.content.read()

    async def video_preview(self, response, index=0):
        """
        Gets video preview after server response.

        Arguments:
            response {dict} -- server response

        Returns:
            bytes -- content for the write-in file.
        """
        return await self.image_preview(response, index, "preview.php")

    async def video_preview_natural(self, response, index=0, mute=False):
        """
        With trace.moe-media, it can now detect timestamp boundaries of a scene naturally.

        Arguments:
            response {dict} -- server response

        Keyword Arguments:
            index {number} -- index from response (default: {0})
            mute {bool} -- mute video sound. {default: {False}}

        Returns:
            bytes -- content for the write-in file.
        """
        response = response["docs"][index]
        url = "%svideo/%s/%s?t=%s&token=%s" % (
            self.media_url, response["anilist_id"],
            response["filename"], response["at"],
            response["tokenthumb"]
        )

        if mute:
            url += "&mute"

        response = await self.session.get(url)

        return await response.content.read()

    async def search(self, path, search_filter=0, is_url=False):
        """
        Searchs anime by image.

        Arguments:
            path {str} -- image path or url.

        Keyword Arguments:
            is_url {bool} -- use url, if True. (default: {False})

        Returns:
            dict -- server response
        """
        url = "%ssearch" % (self.api_url)

        if self.token:
            url += "?token=%s" % (self.token)

        if is_url:
            response = await self.session.get(
                url, params={"url": path}
            )
            return loads(await response.text())
        else:
            with open(path, "rb") as f:
                encoded = b64encode(f.read()).decode("utf-8")
            response = await self.session.post(
                url, json={"image": encoded, "filter": search_filter}
            )
            return loads(await response.text())
