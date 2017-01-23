#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique(list):
    a=[]
    for i in list:
        if i not in a:
            a.append(i)
    return a


new=unique(['b','a','d','a','s','s'])
print(new)
