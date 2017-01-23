#Count number of words in a given statement (String) and then number of characters in each word


name=input('enter the string')
str=name.split()
print("number of words in string",len(str))

for i in range(len(str)):
    print("number of characters in word:",[i+1],len(str[i]))
