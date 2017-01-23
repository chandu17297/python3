#def calculate_BMI(new_weight, new_height):
  #  new_bmi = weight / (pow(height, 2))
 #   return new_bmi


#weight = float(input('Enter weight in Kgs'))
#height = float(input('Enter height in meters'))
#bmi = calculate_BMI(weight, height)
#print(bmi)

#Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception.
def div(a,b):
    try:
      return a/b
    except:
        print('zerodivision error')


d=div(10,0)
print(d)

products = {"Chair": 40, "Sofa": 500, "Table": 90, "Monitor": 100, "Carpet": 200}

newproduct = input('Enter product name')

if (newproduct in products):
    print(products.get(newproduct))
else:
    print('Product Not Found')




