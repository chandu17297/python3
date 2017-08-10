name=input('enter the string to be checked for palinndrome')
name=name.casefold()
reversedname=reversed(name)
print(reversedname)
if(list(name)==list(reversedname)):
    print(name, 'is a palindrome')
else:
    print(name, 'is not a palindrome')
    //gi kosam idhanta