#!/bin/bash
# Script that takes in a url,sends a GET request, and displays the body of the response
curl -s -o /dev/stdout -w "%{http_code}" "$1" | awk '{body=(NR>1?body $0"\n":$0)} END {if($0==200)print body}'
