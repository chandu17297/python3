#Write a function that accepts a string and calculate the number of upper case letters and lower case letters

def letters(str):

    uc = 0
    lc = 0
    for i in str:
        if (i.isupper()):
            uc += 1
        elif (i.islower()):
            lc += 1
        else:
            pass
    print("the original string is:", str)
    print("No of Uppercase letters:", uc)
    print("No of lowercase letters:", lc)

letters('HRITHIK roshan')
