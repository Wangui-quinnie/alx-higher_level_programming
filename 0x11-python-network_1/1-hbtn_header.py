#!/usr/bin/python3
"""
A python script that fetches the value of the X-Request-Id variable
from the header of the response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(req) as response:
        request_id = response.headers.get('X-Request-Id')
        print(request_id)
