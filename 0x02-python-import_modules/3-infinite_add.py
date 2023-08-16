#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    sum = 0
    for num in range(1, length):
        sum += int(sys.argv[num])
    print("{:d}".format(sum))
