#!/usr/bin/python3
from sys import argv


def main():
    num_args = len(argv) - 1
    i = 1

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(num_args))
        while i < len(argv):
            print(f"{i}: {argv[i]}")
            i += 1


if __name__ == "__main__":
    main()
