#find the error and solve
def foo(a=1, b=2):
    return a + b


x = foo() - 1 #a function should always have paranthesis
print(x)

#alternative
def foo():
    global c
    c = 1
    return c
foo()
print(c)

#create a function that takes any string as input
# and return the number of words in the string

def sentence():
    str='hi how are you'
    i=len(str.split())

    return i
print(sentence())
#words.txt


file=open('words1.txt','r')
nws=file.read()
strl=len(nws.split())
print(strl)
file.close()

#words2.txt
file=open('words2.txt','r')
txt=file.read()
srt=txt.replace(',',' ')
srtw=len(srt.split())
print(srtw)
file.close()

#squareroot
import math
print(math.sqrt(9))

#cosine
import math
print(math.cos(1))

#create a text file and generate english alphabets in it
import string

with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")
file.close()

import string
file=open('english.txt','w')
for letter in string.ascii_uppercase:
    file.write(letter + "\n")

file.close()







