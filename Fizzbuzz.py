#Write a program that prints the integers from 1 to 100. But for multiples of three
#print "Fizz" instead of the number, and for the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz"

def fizzbuzz(num):
    for i in range(1,num):
        if (i % 3 == 0 and i % 5 == 0):
            print('fizzbuzz')
        elif (i % 3 == 0):
            print('fizz')
        elif (i % 5 == 0):
            print('buzz')
        else:
            print(i)

fizzbuzz(10)
