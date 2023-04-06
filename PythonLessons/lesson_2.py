#IF STATEMENTS
#FOR LOOPS
#RANGE()
#BREAK AND CONTINUE
#PASS
#MATCH
#FUNCTIONS

#if statements ==================================
# x = int(input("Give me a int: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('you entered 0')
# elif x > 0:
#     print('you entered: ',  x) #concats work different in python than what u r used to..

#for statements =================================
print(' ')
words = ['cat','window','defenestrate']
for word in words:
    print(word, len(word))

users = {
    'adrian' : 'active',
    'gina'   : 'active',
    'gorge'  : 'inactive',
    'bob'    : 'inactive'
}

print(' ')
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users) # returns same list info from above because only actives exist

#range() function =================================
print(' ')
for i in range(5):  #uses airthmetic progressions
    print(i)        # prints 0 through 4

print(' ')
myList = list(range(5,10))
print(myList)

print(' ')
myList = list(range(0,10,2)) #range(start,stop,[step])
print(myList)

print(' ')
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
#0 Mary
#1 had
#2 a
#3 little
#4 lamp

#ITERABLE: We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted.

print('The sum of a range: ',sum(range(4))) # 0 + 1 + 2 + 3
#returns 6

#break and continue statements =================================
# print(' ')
# for n in range(2, 10):
#     print(n)
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

print(' ')
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals')
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# 2 is a prime number
# 3 is a prime number
# 4 equals
# 5 is a prime number
# 6 equals
# 7 is a prime number
# 8 equals
# 9 equals

#pass =================================
# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:

# while True:
#     pass

# class MyEmptyClass:
#     pass

#match =================================
#similar to switch to JS
def what_to_do(myNum):
    match myNum:
        case 0:
            return print("you chose option 0")
        case 1:
            return print("you chose option 1")
        case _:
            return print("no matches found so _ wildcard chosen")

what_to_do(1)

# point = {1,1}

# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"Y={y}")
#     case (x, 0):
#         print(f"X={x}")
#     case (x, y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a point")

# class Point:
#     x: int
#     y: int

# myPoint2 = {1, 2}

# def where_is(point):
#     match point:
#         case Point(x=0, y=0):
#             print("Origin")
#         case Point(x=0, y=y):
#             print(f"Y={y}")
#         case Point(x=x, y=0):
#             print(f"X={x}")
#         case Point():
#             print("Somewhere else")
#         case _:
#             print("Not a point")

# where_is(myPoint2)

#ENUMS =================================
from enum import Enum
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")

#FUNCTIONS =================================
def fib(n): # write Fibonnacci series up to n
    """Im a doc string"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ') #end prints without a new line
        a, b = b, a+b
    print()

fib(100)

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#DEFAULT argument values ==================== [NEEDS FURTHER Research]
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


print(' ')
i = 5
def f(arg=i):
    print(arg)
f()
i = 6
f() # will still return 5 because -> The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes

#DEFAULT argument value 'accumulation' ======
def f(a, L=[]): #overloading is vastly different than C#
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# [1]
# [1, 2]
# [1, 2, 3]



