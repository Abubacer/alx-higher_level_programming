#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    sum = add(a, b)
    difference = sub(a, b)
    product = mul(a, b)
    quotient = div(a, b)
    print("{} + {} = {}".format(a, b, sum))
    print("{} - {} = {}".format(a, b, difference))
    print("{} * {} = {}".format(a, b, product))
    print("{} / {} = {}".format(a, b, quotient))
