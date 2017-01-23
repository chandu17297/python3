#Write a function that checks whether a number is in a given range (Inclusive of high and low)



def func(high,low,num):
    if(num<=high and num>=low):
        print(num,':is in bound')
    else:
        print(num,':is out of bound')

func(100,1,-2)


