#Write a program(usingfunctions!) that asks the user for a long string containing multiple words.
#Print back to the user the same string, except with the words in backwards order.


def reverse(x):
  y = x.split()
  y.reverse()
  print(y)
  return " ".join(y) #string elements in sequence are joined by some seprator(eg: " " - etc)

t=reverse(x = input('enter the string'))
print(t)


