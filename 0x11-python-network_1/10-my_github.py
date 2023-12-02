#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
Must use Basic Authentication with a personal access token as
password to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a
personal access token as password)
You must use the package requests and sys
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]  #personal access token

    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        print(response.json()["id"])
    else:
        print(None)
