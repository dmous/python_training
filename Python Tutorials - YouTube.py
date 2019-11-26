# Intro to Python
# BODMAS Rules
# Brackets - Orders - Divide or Multiply - Add - Subtract
print(5 // 2)
print(5 ** 3)
print(5 % 2)
print(5 // 2)

print("Dimi's laptop")
print("Dimi's 'laptop'")
print('Dimi\'s "laptop"')

print("Dimi " * 2)
print("c:\docs\ndimi")
print(r"c:\docs\ndimi")

# Variables
x = 2
x + 3
# use the output of the previous operation
_ + 3

name = "YouTube"
print(name[0])
print(name[-1])
print(name[len(name) - 1])
print(name[-7])

print(name[0:2])
print(name[0:])
print(name[0:-1])
print(name[:3])
print(name[3:10])

name[0:3] = "My"
# strings are imputable

print("My{0}".format(name[3:]))
print(len(name))

# Lists
numbers = [25, 12, 6, 36, 95]
print(numbers)
print(numbers[0])
print(numbers[4])
print(len(numbers))
print(numbers[0:2])
print(numbers[-1])

names = ["James", "Alan", "Ulises", "Thomas"]
print(names)

values = [9.1, "Alan", 25]
print(values)

misc = [numbers, names]
print(misc)

numbers.append(45)
print(numbers)

numbers.clear()
print(numbers)

numbers = [25, 12, 6, 36, 95]
numbers.insert(2, 13)
print(numbers)

numbers.remove(12)
print(numbers)

numbers.pop(1)
print(numbers)

numbers.pop()
print(numbers)

del numbers[1:]
print(numbers)

numbers.extend([29, 13, 23])
print(numbers)

min(numbers)
max(numbers)
sum(numbers)
numbers.sort()
print(numbers)

# Tuples
tup = (13, 23, 7)
print(tup)

print(tup[0])
tup[1] = 33

tup.count(13)
tup.index(13)

# Set
s = {22, 25, 33, 5}
print(s)

s = {22, 25, 33, 5, 5}
print(s)
s.add(10)
print(s)

help()
help("FLOAT")

# More on variables
num = 5
id(num)
a = 10
b = a

# Same id, memory efficient
print(id(a) == id(b))
id(10)
print(id(a) == id(10))

# Capital letters for indicating the intention for a constant declaration
PI = 3.14
type(PI)

# Data types
# None,
# Numeric (INT, FLOAT, COMPLEX, BOOL),
# Sequence (List, Tuple, Set, String, Range),
# Dictionary

# Numeric
num = 2.5
print(type(num))

num = 5
print(type(num))

num = 6 + 9j
print(type(num))

a = 5.6
type(a)
b = int(a)
type(b)

c = complex(a, b)
type(c)

test = b < a
print(test)
type(test)

print(int(True))
print(int(False))

# Sequence
string = "a"
type(string)

print(range(10))
print(list(range(10)))
type(range(10))

print(list(range(2, 11, 2)))

# Dictionary
d = {"James": "iPhone",
     "Alan": "Samsung",
     "Johnny": "MI5"}

print(d)
print(d.values())
print(type(d.values()))
print(d["James"])
print(d.get("Alan"))

# Operators
x = 2
y = 3

print(x / y)

x = 8
x = x + 2
x += 2
x
x *= 2
x

x /= 3
x

a, b = 1, 5
a, b, c = 1, 5, 5

n = 7
x = -n

b == c
b != c

a, b = 5, 4
(a < 8) and (b < 5)
(a < 8) and (b < 2)
(a < 8) or (b < 2)

x = True
not x

# Number System
# Decimal to Binary format
bin(25)
bin(12)
print(0b1100)

# Swap numbers
a, b = 5, 6
b, a = a, b

# Import math functions
import math

x = math.sqrt(25)
x

x = math.sqrt(15)
x

math.floor(x)
math.ceil(x)
math.pow(3, 2)
math.pi
math.e

from math import sqrt, pow

sqrt(25)
pow(2, 4)

help(math)

x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))

z = x + y
print("The sum of the numbers entered is: {0}".format(z))

sample = eval(input("Please enter an expression: "))
print(sample)

# If else statements - controlling the execution flow
x = 8
r = x % 2

if r == 0:
    print("The number is an even number")
else:
    print("The number is an odd number")

print("Not included in the if block...")

x = 8
r = x % 2

if r == 0:
    print("The number is an even number")
    if x > 5:
        print("Great!")
    else:
        print("Not so great!")
else:
    print("The number is an odd number")

# If elif else
x = 2
if x == 1:
    print("One!")
elif x == 2:
    print("Two!")
else:
    print("Neither 1 nor 2")

# Loops
counter = 1
i = 1
while counter <= 5:
    while i <= 5:
        print("- Alan Shore - the best lawyer ever, right?")
        print("- Yeah, He totally rocks!")
        i += 1
    counter += 1


counter = 1
i = 1
while counter <= 2:
    while i <= 2:
        print("Alan Shore - the best lawyer ever, right?", end=" ")
        print("Yeah, He totally rocks!", end=" ")
        i += 1
    counter += 1


x = ['james', 63, 2.5]
for i in x:
    print(i)

x = "Alan Shore"
for i in x:
    print(i)

for i in range(10):
    print(i)

for i in range(11, 31, 10):
    print(i)

for i in range(31, 1, -1):
    print(i)

for i in range(1, 21, 1):
    print(i)

# Break - Continue - Pass
max_candies = 10
x = int(input("Please enter the number of candies that you want:"))
i = 1

while i <= x:
    if i > max_candies:
        print("Out of stock")
        break

    print("Candy!")
    i += 1

print("Bye!")


for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

print("Bye!")


for i in range(1, 101):
    if i % 2 != 0:
        pass
    else:
        print(i)

print("Bye!")

# Printing Patterns
print("# # # #")

for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()


for i in range(1, 5):
    for j in range(i):
        print("# ", end="")
    print()


for i in range(4):
    for j in range(4-i):
        print("# ", end="")
    print()

# For else statements
nums = [12, 17, 18, 21, 26]

# break is compulsory in this setting
# print "Not found..." only when the whole loops returns false
for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("Not found...")

# Prime Numbers example for For else block
number = 10

for i in range(2, number):
    if number % 2 == 0:
        print("Not a prime number...")
        break
else:
    print("Prime!")

# Arrays
import array as arr
# https://docs.python.org/3/library/array.html
vals = arr.array("i", [12, 23, 13])
print(vals)
print(vals.buffer_info())
print(vals.typecode)
vals[0]

for i in range(len(vals)):
    print(vals[i])

for e in vals:
    print(e)

vals = arr.array("u", ["a", "e", "i"])
for e in vals:
    print(e)

vals = arr.array("i", [12, 23, 13])
newArr = arr.array(vals.typecode, (a*a for a in vals))
for e in newArr:
    print(e)

# Array values from user
array = arr.array("i", [])
times = int(input("Please enter the length of the array:"))


for i in range(times):
    x = int(input("Please enter the next value:"))
    array.append(x)

print(array)
val = int(input("Enter the value to search:"))

k = 0
for e in array:
    if e == val:
        print("The location of the number in the array is: {0}".format(k))
        break

    k += 1

# array.index(val)

# Numpy
import numpy as np
array = np.array([13, 23, 7, 10])
print(array)
print(array.shape)
print(array.dtype)

array = np.array([13, 23, 7, 10.5])
print(array)
print(array.shape)
print(array.dtype)

array = np.linspace(0, 16, 10)
array = np.linspace(0, 16)

array = np.arange(0, 10, 2)
array = np.logspace(1, 40, 5)
print("%.2f" % array[0])

array = np.zeros(5, int)
array = np.ones(5, int)

# Coping an array
array = np.array([13, 23, 7, 10])
array_calc = array + 5
print(array_calc)
print(array + array_calc)  # vectorised operation
array.sum()
array.min()
np.sqrt(array)
np.concatenate([array, array_calc])

array_copied = array.copy()  # deep copy - different arrays, not linked
id(array_copied)
id(array)
array_copied = array.view()  # shallow copy - if you change sth in the first the second changes as well

# Multi-dimensional arrays - matrix
multi_array = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

multi_array.dtype
multi_array.shape
multi_array.ndim
multi_array.size

array_calc = multi_array.flatten()
multi_array_calc = array_calc.reshape(2, 3)
print(multi_array_calc)
m = np.matrix(multi_array_calc)
print(m)
m.dtype

m = np.matrix("1 2; 3 4")
m.size
m.diagonal()
np.diagonal(m)
type(np.max(m))
type(m.max())

m1 = np.matrix("1 2; 3 4")
m2 = np.matrix("5 6; 7 8")
print(m1+m2)
print(m1*m2)

# Functions


def greet():
    print("Hello World!")
    print("Good morning...")


greet()


def add_numbers(x, y):
    result = x + y
    print(result)
    return result


output = add_numbers(x=2, y=13)


def add_sub(x, y):
    add = x + y
    sub = x - y
    return add, sub


addition, subtraction = add_sub(x=2, y=13)


def update(x):
    x = 8
    print(x)


update(10)

# Types of arguments


def add(a, b):  # formal arguments
    c = a + b
    print(c)


add(a=10, b=3)  # actual arguments


def person(name, age):
    print(name)
    print(age)


person(name="Alan", age=13)


def person(name, age=18):
    print(name)
    print(age)


person(name="Alan", age=13)
person(name="Alan")


def add(*b):
    c = 0
    for i in b:
        c = c + i

    print(c)


add(5, 6, 13)


# KeyWorded variable length


def person(name, **data):
    print(name)
    print(data)

    for i, j in data.items():
        print(i, j)


person("Alan", age=27, city="Trikala", mob=151999)


# Global KeyWords - Global & Local Variable (scope)
a = 10


def something():
    global a
    a = 15
    print(a)


something()

# List to a function


def count_types(list_of_numbers):
    even = 0
    odd = 0

    for i in list_of_numbers:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


list_nums = [20, 25, 14, 19, 16, 23, 10, 7]
even_nums, odd_nums = count_types(list_nums)
print("Even: {0} and Odd: {1}".format(even_nums, odd_nums))

# Fibonacci Series
# Add the second last and the last number to get the current number


def fibonacci(number):

    a = 0
    b = 1

    if number == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, number):
            c = a + b
            print(c)
            a, b = b, c


fibonacci(10)


# Factorial


def factorial(number):

    f = 1
    for i in range(1, number+1):
        f = f * i

    return f


x = 6
result = factorial(x)
print(result)

# Recursion
import sys
print(sys.getrecursionlimit())

i = 0


def greet():
    global i
    i += 1
    print("Hello!", i)
    greet()


greet()

# Factorial with Recursion


def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number-1)


result = factorial(5)
print(result)

# Anonymous functions - Lambdas


def square(a):
    return a*a


result = square(5)
print(result)

f = lambda a: a*a
result = f(5)
print(result)

# You can pass any number of arguments, but there needs to be one expression
f = lambda a, b: a+b
result = f(5, 6)
print(result)

# Filter, map, reduce
from functools import reduce

nums = [8, 13, 23, 10, 7, 10]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
even_nums

doubles = list(map(lambda x: x * 2, even_nums))
doubles

total = reduce(lambda a, b: a+b, doubles)
total

# Decorators


def div(a, b):
    print(a/b)


def smart_div(function):

    def inner(a, b):
        if a < b:
            a, b = b, a

        return function(a, b)

    return inner


div(2, 8)
div = smart_div(function=div)
div(2, 8)

# Modules
a = 9
b = 7

import CalcModule

c = CalcModule.add(a, b)
print(c)

c = CalcModule.subtract(a, b)
print(c)

c = CalcModule.divide(a, b)
print(c)

c = CalcModule.multiply(a, b)
print(c)

# __name__
print(__name__)
