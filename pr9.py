def student_discount(price):
    price = price - (price * 10) / 100
    return price


def additional_discount(newprice):
    newprice = newprice - (newprice * 5) / 100
    return newprice


selling_price = 600

# applying both discounts simultaneously

print(additional_discount(student_discount(selling_price)))


#Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.

import math
result= (lambda x:(x*(x+5))**2)(5)
print(result)