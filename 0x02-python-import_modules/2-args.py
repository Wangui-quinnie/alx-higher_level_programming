#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print(f"{num_args} argument:")
        for i, argument in enumerate(args, start=1):
            print(i, ":", argument)
    else:
        print(f"{num_args} arguments:")
        for i, argument in enumerate(args, start=1):
            print(i, ":", argument)
