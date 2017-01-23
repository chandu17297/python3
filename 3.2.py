#Write a function with 3 parameters and return the max with out using max()

def maximum(a,b,c):
    if(a>b and a>c):
        print('the greatest number is',a)
    elif(b>c and b>a):
        print('the greatest no. is',b)
    elif(c>a and c>b):
        print('the greatest no. is',c)

maximum(834681,8364873,938649164)
