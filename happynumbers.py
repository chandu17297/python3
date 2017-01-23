p= []
with open('primenumbers.txt') as pf:
    line = pf.readline()
    while line:
        p.append(int(line))
        line = pf.readline()

h = []
with open('happynumbers.txt') as hf:
    line = hf.readline()
    while line:
        h.append(int(line))
        line = hf.readline()

n = []
for elem in p:
    if elem in h:
        n.append(elem)

print(n)