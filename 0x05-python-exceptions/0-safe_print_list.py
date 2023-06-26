#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # a function that prints x elements of a list.
    # Returns the real number of elements printed.
    try:
        element_count = 0
        for element in range(x):
            if element_count < x:
                print(my_list[element], end="")
                element_count += 1
            else:
                break
    except IndexError:
        pass
    finally:
        print()
    return element_count
