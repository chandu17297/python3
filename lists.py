#lists
list=[1,2,3]
print(list)
list1=['string',1,'k','the']
print(list1)
#length of the list
print(len(list1))
print(list1[3])
#slicing the list
print(list1[1:])
print(list1[:1])
print(list1[-1:])
#concatinating to the list
print(list1+['chandu'])
#adding to the list
list1=list1 + ['chan']
print(list1)
print(list1*2)
#list methods
#append
list1.append(6)
print(list1)
#pop
print(list1.pop(2))
print(list1)
#the last object is popped out
p=list1.pop()
print(p)
#reverse
list1.reverse()
print(list1)
#nested list
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
d=[a,b,c]
print(d)
print(d[0][1])
print(d[2][2])
print(d.pop())
#list count
l1=[1,1,1,3,2,2,3]
print(l1.count(1))
#list append
l1.append([6,4,5])
print(l1)
#list insert
l1.insert(2,'chan')
print(l1)
#list remove
l1.remove('chan')
print(l1)














