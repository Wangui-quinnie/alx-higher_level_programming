#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if i * 10 + j < 89:
            print("{}{}".format(i, j), end=", ")
print("{}".format(89))
