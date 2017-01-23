

def unique(list):
    a=[]
    for i in list:
        if i not in a:
            a.append(i)
    return a


new=unique(['b','a','d','a','s','s'])
print(new)
