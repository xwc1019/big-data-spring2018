msg = "Python is printing me!"
print(msg)

import math
print(math.pi)

from math import pi
print(pi)

import pandas as pd

# I really feel disappointed by this windows system

"""
this is a
multiline
comment
"""
print("comments worked!")

x = 4.0
print(x)
print(x*2)

text = "this is the text we're storing"
print(text)

x += 2
print(x)
x = 3
print(x)

x = x+2
print(x)

x += 22
print(x)
x -= 12
print(x)

x -= 1
print(x)

divi = 12/6
print(divi)
print(type(divi))

print(1 + 2)
print(type(1 + 2))

one = 1
one.bit_length()
big = 13222
big.bit_length()

print(1.0 + .5)
print(3.0 - 2.0)
print(3.0 / 4)
print(type(1.0 + 5))

fit = 2.5
fit.is_integer()
fit += 2
fit.is_integer()
flt = 2/3
flt.is_integer()

x = 12
y = 33
x//y
x += 44
x//y
x += 44
x//y
x % 5
x % 3

s = 'I am a good student'
print(s)

print(s[3])
print(s[3:7])
print(s[2:11])

string = s + "really ?"
print(string)
string += " really really not!"
print(string)

string.find("really")
string.find("am")
string.count("a")

result1 = 2.017e-3
print(f"The result of the operation is {result1}!")

finding1 = 17
print("We find that the value is {}".format(finding1))
finding2 = 13
print("We find that the first value is {} and the second value is {}".format(finding1,finding2))

is_true = True
print(is_true)

x = True
y = False
print(x)
print(x and y)
print (not x or y)
print (x or y)

print(1 == 2)
print(1 == 1)
print(1 != 2)
print("abcd" == "abcd")
x = 1
y = 2
print(x == y)

x = y
print(x)
print(y)
print (x is y)

l_one = []
x = 5
l_two = [1, 2.0, 'a', "abcd", True, x]
l_one.append(1)
l_one.append(2)
print(l_one)

l_three = ['a', 'b', 'c']
l_one.extend(l_three)
print(l_one)

alph = ['a', 'b', 'c', 'd', 'e']
print(alph[4])
print(alph[-1])

print(alph[:2])
print(range(10))
print(range(2,10))
print(range(4, 10, 2))
print(len(range(10)))

squares = []
for i in range(5):
    squares.append(i * i)
    print(squares)

squares = [i * i for i in range(5)]
print(squares)

d_one = {}
d_two = {'key1':1, 'key2':"moose",4:5}
print(d_two)
d_two[6] = False
print(d_two)
print(d_two[6])
if not d_two[6]:
    print("Dicts are fun")
else:
    print("Dicts are not that fun")
print("keys:" +str(list(d_two.keys())))
print("values: "+str(list(d_two.values())))

numbers = {'one':1, 'two':2, 'three': 3}
print(numbers)
print(numbers['one'])

print([i for i in numbers])
print([(k,v) for k,v in numbers.items()])

list(numbers.values())

playlist = list(numbers.values())
print(playlist[1])
print(playlist[0])
print(list(numbers.keys()))

mydict = {k:v for (k,v) in zip(range(5), range(5))}
mydict
dict(a = 1, b = 2)

fun_list = ['are', 'we', 'having', 'fun', 'yet', '?']
fun_list.sort()
print(fun_list)
fun_list.count
print(fun_list.count())
print(count(fun_list))
print([fun_list].count())
more_fun = ['i', 'know', 'that', 'am','!']
more_fun_sort = sorted(more_fun)
print(more_fun_sort)
count(more_fun_sort)

flag = True
if flag:
    x = 1
    print("Flag is True.")
else:
    x = 2
    print("Flag is False")
print(x)

if x == 0:
    print("A")
elif x == 1:
    print('B')
else:
    print("C")

x = range(10)
print(x)

for i in x:
    print(i)
for i in x:
    print(i*2)
for i in range(10):
    if(i > 5):
        break
    print(i)
List = ["This", "That", "Me"]
for i in List:
    print(i)
    print(list.index(i))
guanao = False
if guanao:
    x = 1
    print("guanao is True")
else:
    x = 2
    print("guanao is Flase")
print(x)

if x == 0:
    print("A")
elif x == 1:
    print('B')
else:
    print("C")

x = 3+3
if x == 3:
    print("3+3=3")
elif x == 6:
    print("3+3=6")
else:
    print("none answer")

mylist = ["This", "is", "Python"]
for i in mylist:
    print(i)
    print(mylist.index(i))

x = 0
for i in range(100):
    x += i
print(x)

myclass = ["GIS", "Regional Planning", "Big data and visualization"]
for i in myclass:
    print(f"In Sparing 2018, I am taking: {i}")
    print(myclass.index(i))

x = 0
for i in range(100):
    x += i
print(x)

def for_sum(x,y):
    for i in range(y):
        x += i
    return x

print(for_sum(0,100))
print(for_sum(10,50))

f = for_sum
print(f(0,100))

def execute(funct,x):
    return funct(x,100)
print(execute(f,10))

def print_words(x = "This", y = "Not Eric"):
    print(x)
    print(y)
print_words()

x = "Eric"
y = "Something Else"
print_words(x,y)
import numpy as np
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = []
for i, j in zip(a,b):
    c.append(i + j)
print(c)

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
c = a + b
print(c)

x = 1
x += 3
print(x)

x = rang(10)
x = Range(10)
x = range (10)
for i in x:
    print(i*2)
for i in x:
    if(i>5):
        break
    print(i)
my_list = ['This', 'is', 'Python']
for i in my_list:
    print(i)
    print(my_list.index(i))
#what index position is occupied by list

x = 0
for i in range(100):
    x += i
print(x)
# we want to iterate the
# x = x+i

#all value from certain value to a larger values, and this is a fucntion defination

def for_sum(x,y):
    for i in range(y):
        x += i
    return(x)
for_sum(0,100)

import pandas as pd
import numpy as np
