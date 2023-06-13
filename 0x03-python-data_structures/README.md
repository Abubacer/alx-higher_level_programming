![My GitHub avatar](https://avatars.githubusercontent.com/u/13408012?s=200&v=4)

# 0x03-Python - Data Structures: Lists, Tuples

Python is awesome :nerd_face:
## Learning Objectives

At the end of this project, we are expected to be able to explain to anyone, without the help of Google:
* Why Python programming is awesome
* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the del statement and how to use it

## Project Tasks

### 0-print_list_integer.py
Write a function that prints all integers of a list.

- Prototype: def print_list_integer(my_list=[]):
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use str.format() to print integers

```python
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 
```
#### The execution flow
1. Initiates a loop that iterates over each number in the list.
2.  Print each element in the list and format each element as an int using the format() method with the :d format specifier.

#### The source code: [0-print_list_integer.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/0-print_list_integer.py)
***
### 1-element_at.py
Write a function that retrieves an element from a list like in C.

- Prototype: def element_at(my_list, idx):
- If idx is negative, the function should return None
- If idx is out of range (> of number of element in my_list), the function should return None
- You are not allowed to import any module
- You are not allowed to use try/except

```python
guillaume@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$ 
```
#### The execution flow
1. Check if the provided index is negative (less than 0) or out of range (greater than or equal to the length of the list).
2. If either condition is true, it means the index is invalid and step 2 is true: return None.
3. If step 2 is false: return the list with the value at the specified index.

#### The source code: [1-element_at.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/1-element_at.py)
***
### 2-replace_in_list.py
Write a function that replaces an element of a list at a specific position (like in C).

- Prototype: def replace_in_list(my_list, idx, element):
- If idx is negative, the function should not modify anything, and returns the original list
- If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
- You are not allowed to import any module
- You are not allowed to use try/except

```python
guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$ 
```
#### The execution flow
1. Check if the provided index is negative (less than 0) or out of range (greater than or equal to the length of the list).
2. If either condition is true, it means the index is invalid and step 2 is true: return the list without making any changes.
3. If step 2 is false:  set the value of the var "element" to the element at the specified index in the list this will replaces the existing value at that index with the new value.
4. Return the list with the updated value at the specified index.

#### The source code: [2-replace_in_list.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/2-replace_in_list.py)
***
### 3-print_reversed_list_integer.py
Write a function that prints all integers of a list, in reverse order.

- Prototype: def print_reversed_list_integer(my_list=[]):
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use str.format() to print integers

```python
guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$ 
```
#### The execution flow
1. Check if the provided list is a list type
2. If condition is true: reverse the list using reverse() function.
3. Iterates over each element in the list
4. print and format each element as an int using the format() method with the :d format specifier.

#### The source code: [3-print_reversed_list_integer.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/3-print_reversed_list_integer.py)
***

### 4-new_in_list.py
Write a function that prints all integers of a list.

- Prototype: def print_list_integer(my_list=[]):
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use str.format() to print integers
```python
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$
```
#### The execution flow
1. Creates a new list that is a copy of the original list to avoid modifying the original list.
2. Check if the provided index is negative (less than 0) or out of range (greater than or equal to the length of the list).
3. If either condition is true, it means the index is invalid and step 2 is true: return the copy of the list without making any changes.
4. If step 2 is false:  set the value of the var "element" to the element at the specified index in the copy this will replaces the existing value at that index with the new value.
5. Return the copy of the list with the updated value at the specified index.
#### The source code: [4-new_in_list.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/4-new_in_list.py)
***
### 5-no_c.py
Write a function that removes all characters c and C from a string.

- Prototype: def no_c(my_string):
- The function should return the new string
- You are not allowed to import any module
- You are not allowed to use str.replace()
```python
guillaume@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$ 
```
#### The execution flow
1. Creates a new list and iterates over each character in the provided string.
2. Check if the character is not equal to 'c' (lowercase) and not equal to 'C' (uppercase). 
3. Filter out the characters 'c' and 'C' from the original string.
4.  Joins the elements in list into a new single string using the join() and put the "" separator between the elements
5. Return the new string
#### The source code: [5-no_c.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/5-no_c.py)
***

### 6-print_matrix_integer.py
Write a function that prints a matrix of integers.

- Prototype: def print_matrix_integer(matrix=[[]]):
- Format: see example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use str.format() to print integers

```python
guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 
```
#### The execution flow
1. Initiates a loop that iterates over each row in the matrix
2. Iterates over each element in the row and format each element as an int using the format() method with the :d format specifier.
3. Concatenates the elements of the iterator into a single string, using join() and the space " " as a separator.
4. Print the string as row of the matrix with elements separated by spaces.
#### The source code: [6-print_matrix_integer.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/6-print_matrix_integer.py)
***
### 7-add_tuple.py
Write a function that adds 2 tuples.

- Prototype: def add_tuple(tuple_a=(), tuple_b=()):
- Returns a tuple with 2 integers:
- The first element should be the addition of the first element of each argument
- The second element should be the addition of the second element of each argument
- You are not allowed to import any module
- You can assume that the two tuples will only contain integers
- If a tuple is smaller than 2, use the value 0 for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers

```python
guillaume@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$ 
```
#### The execution flow
1. Creates a new tuple 'A' by concatenating 'tuple_a' with a tuple (0, 0).
2. Check if the 'A' has a length of at least 2 using a slicing operation and len() 
3. If 'tuple_a' has a length of 2 or more, the slicing operation is essentially an empty slice [:], resulting in 'A' being the same as 'tuple_a'. 
4. Otherwise, append (0, 0) to 'tuple_a' to ensure 'A' has two elements.
5. Creates a new tuple 'B' and repeat the step 1, 2, 3
6. Calculates the sum of the 'A' and 'B' by performing element-wise addition to generate a new tuple
5. Return the sum
#### The source code:  [7-add_tuple.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/7-add_tuple.py)
***
### 8-multiple_returns.py
Write a function that returns a tuple with the length of a string and its first character.

- Prototype: def multiple_returns(sentence):
- If the sentence is empty, the first character should be equal to None
- You are not allowed to import any module

```python
guillaume@ubuntu:~/0x03$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/0x03$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/0x03$ 
```
#### The execution flow
1. Check if the string is empty.
2. If the condition is true: return None and set the first character to None.
3. Otherwise, return the length of a string and its first character.
#### The source code: [8-multiple_returns.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/8-multiple_returns.py)

***
### 9-max_integer.py
Write a function that finds the biggest integer of a list.

- Prototype: def max_integer(my_list=[]):
- If the list is empty, return None
- You can assume that the list only contains integers
- You are not allowed to import any module
- You are not allowed to use the builtin max()

```python
guillaume@ubuntu:~/0x03$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

guillaume@ubuntu:~/0x03$ ./9-main.py
Max: 90
guillaume@ubuntu:~/0x03$ 
```
#### The execution flow
1. Check if the list is empty. if the length of the list is equal to 0 is true:  there are no elements in the list, return None.
2. Initialize the variable to store the first element of the list.
3.  Iterates over each element in the list to find the actual maximum value in the list. 
4. Compare each element with the current value of the variable from step 2.
5. If an element in the list is greater than the current value of the variable, it updates to the new value of the element.
6. Return the value which represents the maximum value in the list.
#### The source code: [9-max_integer.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/9-max_integer.py)
***
### 10-divisible_by_2.py

Write a function that finds all multiples of 2 in a list.

- Prototype: def divisible_by_2(my_list=[]):
- Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
- The new list should have the same size as the original list
- You are not allowed to import any module

```python
guillaume@ubuntu:~/0x03$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

guillaume@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/0x03$ 
```
#### The execution flow
1. Iterates over the range of indices using a for loop
2.  Check and evaluated if each index is divisible by 2.
3.  Iterates over each element in the list to find the actual maximum value in the list. 
4. If it is true: the number in the list is an even number 
5. If it is false: the number in the list is an odd number.
6. Return the result with the corresponding boolean values true or false.
#### The source code: [10-divisible_by_2.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/10-divisible_by_2.py)
***
### 11-delete_at.py
Write a function that deletes the item at a specific position in a list.

- Prototype: def delete_at(my_list=[], idx=0):
- If idx is negative or out of range, nothing change (returns the same list)
- You are not allowed to use pop()
- You are not allowed to import any module

```python
guillaume@ubuntu:~/0x03$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/0x03$ 
```
#### The execution flow
1. Check if the provided index is negative (less than 0) or out of range (greater than or equal to the length of the list).
2. If either condition is true, it means the index is invalid and step 2 is true: return the list without making any changes
3. If step 2 is false:  delete the value of the element at the specified index in the list using del().
4. Return the list with the updated value at the specified index.
#### The source code: [11-delete_at.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/11-delete_at.py)
***
### 12-switch.py
Complete the source code in order to switch value of a and b

- You can find the source code [here](https://github.com/alx-tools/0x03.py/blob/b8a061490a491521af7e3f35424b23af0fcefd21/12-switch_py)
- Your code should be inserted where the comment is (line 4)
- Your program should be exactly 5 lines long
```python
guillaume@ubuntu:~/py/0x03$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/0x03$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/0x03$ 
```
#### The execution flow
1. Use tuple packing and unpacking to swap the values of a and b. The values of b and a are packed into a tuple (b, a), and then unpacked back into the variables a and b,  swapping their values.
#### The source code: [12-switch.py](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/12-switch.py)
***
### 13-is_palindrome.c
Write a function in C that checks if a singly linked list is a palindrome.

- Prototype: int is_palindrome(listint_t **head);
- Return: 0 if it is not a palindrome, 1 if it is a palindrome
- An empty list is considered a palindrome
- You can find the source code here: [13-main.c](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/13-main.c)  [linkedlists.c](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/linked_lists.c)  [lists.h](https://github.com/Abubacer/alx-higher_level_programming/blob/2b680d408cc0bcd5c1d30d18cfad89a818eabcfc/0x03-python-data_structures/lists.h)
```C
carrie@ubuntu:0x03$ gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome
carrie@ubuntu:0x03$ ./palindrome
1
17
972
50
98
98
50
972
17
1
Linked list is a palindrome
carrie@ubuntu:0x03$
```
#### The execution flow
1. Declare four pointers.
2. Check if the linked list is empty or contains only one node. If true: return 1 indicating a palindrome.
3. Initialize the tree pointers to the input head of the list.
4. Using a while loop find the middle of the linked list using "slow and fast pointers" algorithm.
5. After the loop, if the fast pointer is not NULL, it means the list has an odd number of nodes. In such a case, the slow pointer is moved one step forward to skip the middle element, and adjusts the slow pointer to point to the beginning of the second half of the list.
6. The function calls the reverse_list() function, passing the slow pointer as the input, to reverse the second half of the list. The reversed list is stored in the fourth pointer.
7. Using a while loop the function compare the corresponding nodes of the list two halves.
8. Return 0 If at any point the values differ, it means the list is not a palindrome.
9. Return 1 indicating that the list is a palindrome, If the loop completes without any mismatches.
#### The source code: [13-is_palindrome.c](https://github.com/Abubacer/alx-higher_level_programming/blob/fc1ac6747a6923ab82cfb86bc784f8976d62a627/0x03-python-data_structures/13-is_palindrome.c)
***
Thank you :heart:

