name="my name is chandra shekar"
words=name.split()
#split function returns the words from string name
print(name.split())
noofwords=len(words)
print("No of words in a string:",noofwords)

for i in range(noofwords):
    print("no of char in word",[i+1],"is :",len(words[i]))
