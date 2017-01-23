letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#print out the second item of the list
print(letters[1])
#expected output [d,e,f] using slicing
print(letters[3:6])
#expected output [a,b,c] using slicing
print(letters[:3])
#expected output[i]
print(letters[8:9])
#expected output [i] using negative index
print(letters[-2])
#expected output [h,i,j] usnig negative index
print(letters[-3:])
# expected output [a,c,e,g,i] using slicing
print(letters[::2])

