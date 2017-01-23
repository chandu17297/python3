#find list of the first letters of every word in the string below:



st = 'Create a list of the first letters of every word in this string'
st=st.split()
for i in range(len(st)):
    g=(st[i][0])
    print('the first letter of word',[i+1],'is',g)





