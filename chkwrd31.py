#Check for a given word in a file of text

def checking(fname,word):
    file=open(fname)
    return any(word in line for line in file)
if checking('word.txt','language'):
    print('word found')
else:
    print('word not found')

