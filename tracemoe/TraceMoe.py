# -*- coding: utf-8 -*-
# authors: Ethosa
from base64 import b64encode

from requests import Session


class TraceMoe:
    def __init__(self, token=""):
        """
        Initialize trace moe API.
        """
        self.api_url = "https://api.trace.moe/"
        self.main_url = "https://trace.moe/"
        self.media_url = "https://trace.moe/media/"
        self.token = token
        self.session = Session()
        self.session.headers = {"Content-Type": "application/json"}

    def me(self):
        """
        Gets limit for your IP.

        Returns:
            dict -- server response
        """
        url = "%sme" % (self.api_url)

        if self.token:
            url += "?token=%s" % (self.token)

        return self.session.get(url).json()

    def image_preview(self, response, index=0):
        """
        Gets image preview after server response.

        Arguments:
            response {dict} -- server response

        Returns:
            bytes -- content for the write-in file.
        """
        url = response["result"][index]["image"]

        return self.session.get(url).content

    def video_preview(self, response, index=0):
        """
        Gets video preview after server response.

        Arguments:
            response {dict} -- server response

        Returns:
            bytes -- content for the write-in file.
        """
        url = response["result"][index]["video"]

        return self.session.get(url).content

    def video_preview_natural(self, response, index=0, mute=False):
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
        url = response["result"][index]["video"]
        url += "&size=l"

        if mute:
            url += "&mute"

        return self.session.get(url).content

    def search(self, path, search_filter=0, is_url=False, **kwargs2):
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
            return self.session.get(url, params={"url": path, **kwargs}).json()
        with open(path, "rb") as f:
            encoded = b64encode(f.read()).decode("utf-8")
        return self.session.post(
            url, json={"image": encoded, "filter": search_filter}
        ).json()
