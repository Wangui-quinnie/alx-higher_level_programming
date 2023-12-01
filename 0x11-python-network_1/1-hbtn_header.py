#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    request_id = response.headers.get('X-Request-Id')
    print(request_id)


if __name__ == "__main__":
