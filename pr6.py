import string,os
if not os.path.exists("letters1"):
    os.makedirs("letters1")
    for letter in string.ascii_lowercase:
        with open("letters1/" + letter + ".txt", "w") as file:
            file.write(letter + "\n")

#

import glob
l =[]
fl= glob.glob("letters1/*.txt")

for fname in fl:
    with open(fname,"r") as file:
        l.append(file.read().strip("\n"))
print(l)

