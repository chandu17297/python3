#writing a program for fizzbuzz

for k in range(1,16):
    if(k%3==0 and k%5==0 ):
        print('fizzbuzz')
    elif(k%3==0):
        print('fizz')
    elif(k%5==0):
        print('buzz')
