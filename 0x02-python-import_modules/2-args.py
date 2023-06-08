#!/usr/bin/python3
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('arguments', nargs='*', help='list of args')
    args = parser.parse_args()
    args_list = args.arguments
    argc = len(args_list)

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc > 1:
        print("{} arguments: ".format(argc))
        for i, argv in enumerate(args_list, start=1):
            print("{}: {}".format(i, argv))
    elif argc == 1:
        print("{} argument: ".format(argc))
        for y, argv in enumerate(args_list, start=1):
            print("{}: {}".format(y, argv))
