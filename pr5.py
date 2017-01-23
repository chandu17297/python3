#use of zip function

a=[1,2,3] #list
b=(7,8,9) #tuple

for i,j in zip(a,b):   #zip is used to aggregate values in a n b
    print(i+j)

#
import string
file=open('new.txt','w')
for l,k in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]):
    file.write(l + k + "\n" )
file.close()

#abc3.txt

import string
letters=string.ascii_lowercase + ' '
slice1=letters[0::3]
slice2=letters[1::3]
slice3=letters[2::3]

with open('abc3.txt','w') as f:
    for s1,s2,s3 in zip(slice1,slice2,slice3):
        f.write(s1 + s2 +s3 + "\n")

#txt26.txt

#import string

