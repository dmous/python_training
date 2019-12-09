# Automating the boring stuff with Python code
print("Hello World")
2 ** 3
8 // 3
8 / 3
9 % 3
# The ** operator is evaluated first;
# the *, /, //, and % operators are evaluated next, from left to right;
# and the + and - operators are evaluated last (also from left to right)

"Alice " + "Bob"
"Alice " * 3
spam = 40
spam * 2

# My first program
print("Hello World")
print("What is your name?")
myName = input()
print("It is good to meet you, " + myName)
print("The length of your name is:")
print(len(myName))
print("What is your age?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year!")

# Comparison operators
print(int(2.5) + 1)
42 == 42.0
42.0 == 0042.000
49 == 47
2 != 3
"hello" == "world"

# Boolean Operators
True and True
True or False
not True
not not not True

(1 == 2) and (2 > 1)

name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')

name = "Dimi"
if name == "Alan":
    print("Hey Alan!")
elif name == "Dimi":
    print("Hey Dimi!")
else:
    print("Hello stranger!")

# Operator    Meaning
# ==          Equal to
# !=          Not equal to
# <           Less than
# >           Greater than
# <=          Less than or equal to
# >=          Greater than or equal to

spam = 0
if spam < 5:
    print("Hello World!")
    spam += 1

# The while loop
spam = 0
while spam < 5:
    print("Hello World!")
    spam += 1

name = ''
while name != 'your name':
    print('Please type your name:')
    name = input()
print('Thank you!')

while True:
    print('Please type your name:')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        # Go back to the condition check of the loop
        continue
    print("Hello Joe! What is the password? (It is a fish)")
    password = input()
    if password == "swordfish":
        # Break out of the loop
        break
print("Access granted!")

name = ''
while not name:
    print('Enter your name: ')
    name = input()

print('How many guests will you have?')
num_of_guests = int(input())
if num_of_guests:
    print('Be sure to have enough room for all your guests')

print('Done!')

# The for loop along with the range() function
print('My name is: ')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# In fact, you can use continue and break statements only inside while and for loops
total = 0
for num in range(101):
    total = total + num
print(total)

for i in range(0, 10, 2):
    print(i)

for i in range(5, -1, -1):
    print(i)

# Importing modules
import random

for i in range(5):
    print(random.randint(1, 10))

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '!')

# Functions
# def statements
def hello(name):
    print('Hello ' + name)


hello('Dimi')

import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
# or
print(getAnswer(random.randint(1, 9)))

# The NONE value
spam = print("Hello")
None == spam

#Keyword Arguments and print()
print("Hello", end='')
print("World")
print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep=',')

# Local and Global Scope
# There are four rules to tell whether a variable is in a local scope or global scope:
#       If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.
#       If there is a global statement for that variable in a function, it is a global variable.
#       Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
#       But if the variable is not used in an assignment statement, it is a global variable.

# Exception Handling
def spam(divideby):
    return 42/divideby

print(spam(divideby=2))
print(spam(divideby=0))

def spam(divideby):
    try:
        return 42/divideby
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(divideby=0))
print(spam(divideby=6))

# Consolidating knowledge

# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

# Lists
# A list is a value that contains multiple values in an ordered sequence
spam = ['cat', 'dog', 'elephant']
spam[0]
spam[1]

spam_two = [['cat', 'dog', 'elephant'], [10, 20, 30]]
spam_two[1][0]
spam_two[1][2]
spam_two[0][2]

spam_two[-1][1]

# Slicing
# A slice goes up to, but will not include, the value at the second index. A slice evaluates to a new list value
spam_two[1][0:2]
spam_two[1][0:-1]
spam_two[1][0:]
spam_two[1][:]

spam_two[:][:]

len(spam_two)

# Changing Values in a List with Indexes
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'dog'
print(spam)

replicated_list = spam*3
print(replicated_list)
print(replicated_list+['added_item', 'more_items'])

# Removing list values with the del statement
del spam[-1]
print(spam)
del replicated_list

# Useful approach to lists
catNames = []
while True:
    print('Enter the name of the cat number ' + str(len(catNames)+1) + ' (Or enter nothing to stop):')
    name = input()

    if name == '':
        break
    catNames = catNames + [name] #concatenate lists like this
print('The cat names are:')
for name in catNames:
    print(' ' + name)

supplies = ['pens', 'staplers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

testing_in_operator = ['hello', 'hi', 'howdy', 'heyas']
'howdy' in testing_in_operator
'howdy' not in testing_in_operator

mypets = ['Zophie', 'Pooka', 'Alex']
print('Enter a pet name:')
name = input()

if name not in mypets:
    print('I do not have a pet named ' + name)
else:
    print('I do have a pet named ' + name)

# The Multiple Assignment Trick
# Instead of typing this lines of code:
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

# we can type just this:
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat

spam = 42
spam += 1
spam

spam *= 2
spam

spam /= 2
spam

# Methods
# A method is the same thing as a function, except it is “called on” a value.
# For example, if a list value were stored in spam, you would call the index()
# list method (which I’ll explain next) on that list like so: spam.index('hello').
# The method part comes after the value, separated by a period
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('howdy')

spam.append('moose')
spam

spam.insert(0, 'woody')
spam

# Methods belong to a single data type. The append() and insert()
# methods are list methods and can be called only on list values, not on other values such as strings or integers.

bacon = 42
bacon.insert(1, 'world')

spam.remove('heyas')
spam.remove('chicken')
del(spam[0])
spam

spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam

spam.sort(reverse=True)
spam

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
spam

spam.sort(key=str.lower)
spam

# Example Program: Magic 8 Ball with a List
import random

messages = ['It is certain', 'It is decidedly so', 'Yes definitely',
            'Reply hazy try again', 'Ask again later', 'Concentrate and ask again',
            'My reply is no', 'Outlook not so good', 'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])


print('Four score and seven ' + \
      'years ago')

# List-like Types: Strings and Tuples
name = 'Zophie'
name[0]

'Zo' in name
for i in name:
    print('***' + i + '***')

name = 'Zophie a cat'
# The proper way to “mutate” a string is to use slicing and concatenation to
# build a new string by copying from parts of the old string.
name[7] = 'the'
newName = name[0:7] + 'the' + name[8:12]
newName

# Tuples
eggs = ('hello', 42, 0.5)
eggs
eggs[0]

# You can use tuples to convey to anyone reading your code that you don’t intend for that sequence of
# values to change. If you need an ordered sequence of values that never changes, use a tuple.
# A second benefit of using tuples instead of lists is that, because they are immutable and their contents
# don’t change, Python can implement some optimizations that make code using tuples slightly faster than code using lists.

tuple(['cat', 'dog', 5])
list(('cat', 'dog', 5))
# Converting a tuple to a list is handy if you need a mutable version of a tuple value.
list('hello')

# References
spam = [0, 1, 2, 3, 4, 5]
cheese = spam

cheese[1] = 'Hello!!!'
cheese
spam
# list variables don’t actually contain lists—they contain references to lists
# Variables will contain references to list values rather than list values themselves.
# But for strings and integer values, variables simply contain the string or integer value.
# Python uses references whenever variables must store values of mutable data types, such as lists or dictionaries.
# For values of immutable data types such as strings, integers, or tuples, Python variables will store the value itself.
# Although Python variables technically contain references to list or dictionary values, people often casually
# say that the variable contains the list or dictionary.

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1,2,3]
eggs(someParameter=spam)
print(spam)

import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
# Now the spam and cheese variables refer to separate lists, which is why only the
# list in cheese is modified when you assign 42 at index 1
spam
cheese

# If the list you need to copy contains lists, then use the copy.deepcopy()
# function instead of copy.copy(). The deepcopy() function will copy these inner lists as well.

# Dictionaries and Structuring Data
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size']

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}

eggs==ham

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
       break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')















