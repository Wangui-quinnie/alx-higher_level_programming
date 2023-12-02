#!/usr/bin/python3
"""1-hbtn_header module."""


import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Fetches the value of the X-Request-Id variable from the header of the
    response.
    """

    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        request_id = response.headers.get('X-Request-Id')
        print(request_id)


if __name__ == '__main__':
    fetch_x_request_id(url)
