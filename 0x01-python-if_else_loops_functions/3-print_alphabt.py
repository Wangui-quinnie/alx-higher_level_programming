#!/usr/bin/python3
for alphabet_letters in range(ord('a'), ord('z)+1):
    if chr(alphabet_letters) not in ('e', 'q'):
        print("{:c}".format(alphabet_letters), end="")
