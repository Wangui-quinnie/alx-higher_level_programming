#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, displays
the id and name like this: [<id>] <name>
Otherwise:
Displays Not a valid JSON if the JSON is invalid
Displays No result if the JSON is empty
using the package requests and sys.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    r = requests.post(url, data=data)

    try:
        json_r = response.json()
        if json_r:
            print("[{}] {}".format(json_r.get("id"), json_r.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
