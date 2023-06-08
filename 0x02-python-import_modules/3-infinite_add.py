#!/usr/bin/python3
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('int', type=int, nargs='*')
    parser.add_argument('add', action='store_const', const=sum)
    args = parser.parse_args()
    int_sum = args.add(args.int)
    print(int_sum)
