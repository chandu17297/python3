str=input('enter the string')
uppercase = 0
lowercase = 0
for i in str:
    if (i.isupper()):
        uppercase += 1
    elif (i.islower()):
        lowercase += 1
    else:
        pass
print("the original string is:", str)
print("No of Uppercase letters:", uppercase)
print("No of lowercase letters:", lowercase)
