i=0
j=1

if __name__ == '__main__':
    for k in range(0,10):
        sum=i+j
        print(sum)
        i=j
        j=sum

#fibonacci no

def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print("fibonacci no", fibo(6))
