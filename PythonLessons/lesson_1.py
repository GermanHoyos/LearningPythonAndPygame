# NUMBERS
# VARIABLES
# STRINGS
# LISTS

#First python code ever written=================
print("My first Hello World in Python")

#Numbers =======================================
print(4 * 3.75 - 1)
print(2 + 2)
print(50 - 5*6)
print(
    (50 - 5*6) / 4
)
print(17 / 3)  # classic division returns a float
print(17 // 3)  # floor division discards the fractional part
print(17 % 3)  # the % operator returns the remainder of the division
print(5 * 3 + 2)  # floored quotient * divisor + remainder
print(5 ** 2)  # 5 squared
print(2 ** 7)  # 2 to the power of 7

#Variables =====================================
width = 10
height = 30
print(width * height)

#Strings =======================================
print('eggs are yummy')
print("eggs in my tummy")
print('"Isn\'t," they said.')
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print(3 * 'un' + 'ium') #MATH done to a string - very interesting
print('Py' 'thon') #auto concat
word = 'OverCome'
print(word[3]) # 0 indexed
print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6])
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
print(word[:2])   # character from the beginning to position 2 (excluded)
print(word[4:])   # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end
print(word[:2] + word[2:])
print(word[:4] + word[4:])
anotherWord = 'HowLongAmI'
print(len(anotherWord))

#Lists   =======================================
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])       # indexing returns the item
print(squares[-1])      # this prevents stackOverflow issues in my OP
print(squares[-3:])     # slicing returns a new list

#All slice operations return a new list containing the requested elements.
#This means that the following slice returns a shallow copy of the list:
squares[:] # <-slice operation returns a "shallow copy"
#SHALLOW copy = constructing a new collection object and then populating
#it with references to the child objects found in the original
squares + [36,49,64.81,100]
print(squares)

cubes = [1,8,27,65,125] #65 should be 64
cubes[3] = 64           #65 was changed to 64
print(cubes)            #lists are mutable, unlike strings which are immutable
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# replace some values
letters[2:5] = ['C', 'D', 'E'] #slices are 0 indexed
print(letters)
# now remove them
letters[2:5] = []
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

moreLetters = ['x','y','z']
print(len(moreLetters))

fibA, fibB = 0, 1
while fibA < 10:
    print(fibA)
    fibA, fibB = fibB, fibA + fibB


