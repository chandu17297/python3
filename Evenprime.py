def even(num):
    for i in range(num):
        if (i%2==0):
            print('even number',i)

even(20)

def prime(num):

    for i in range(num):
        if(i>1):
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                    print(i)

prime(23)
