#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status.
"""
import requests

url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    content = response.text  # Use response.text instead of response.json()
    print("Body response:")
    print("\t- type:", type(content).__name__)
    print("\t- content:", content)
