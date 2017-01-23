#print english alphabets

import string
for letter in string.ascii_uppercase:
    print(letter)

#print 1 to 10 numbers

for i in range (1,11):
    print(i)

#Create a function that calculates acceleration given initial velocity v1,
#final velocity v2, start time t1, and end time t2.
#The formula for acceleration is: a=v2-v1/t2-t1 , v1,v2,t1,t2 : 0,10,0,20


#alternative way
def acceleration(v1, v2, t1, t2):
    a = (v2 - v1) / (t2 - t1)
    return a


print(acceleration(0, 10, 0, 20))

#program
def foo(a, b):
    return a + b


x = foo(2, 3) * 10
print(x)

#Please write a function that calculates liquid volume in a sphere
#using the following formula.
#The radius r  is always 10, so consider making it a default parameter

from math import pi
def volume(h,r=10):
    vs= ((4*pi*r**3)/3)-((3*pi*r*h**2)-(pi*h))/3
    return vs
print(volume(2))







