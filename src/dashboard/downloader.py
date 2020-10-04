#!/usr/bin/python3
"""
This class is used for downloading data from Italian Civil Protection
"""
import requests


class Downloader:
    def __init__(self, url):
        self.r = requests.get(self.url, allow_redirects=True)
        self.url = url

    def start(self):
        # start the download
        pass

    # save downloaded data to file
    def save(self, name):
        open(name, 'wb').write(self.r.content)

    def downloadable(self):
        return requests.is_downloadable(self.url)
