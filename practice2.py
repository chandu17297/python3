my_range= range(1,21)
print(list(my_range))

#expected output [10,20....200]

#for i in my_range:
    #i*=10
    #print(i)

#or

print([10*i for i in my_range])

#expected output['1','2','3',....... '20']

print(list(map(str, my_range)))

#given ["1",1,"1",2]
#the output shouldnt have any duplicates in the list ... ["1",2,1]

a=["1",1,"1",2]
print(list(set(a)))

d={'a':1,'b':2}
print(d)
#expected output of d is 2

print(d['b'])

#expected output is sum of values of keys a and b

print(d['a']+d['b'])
print(d.values())
print(d.items())
d['c']=3
print(d)
#calculate the sum of all dictionary values

print(sum(d.values()))

#filter the dictionary with a value greater than 1

d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)

#create a dictionary with values of keys having a list from 1 to 10,10 to 20,20 to 30 respectively

d = dict(a = list(range(1,11)), b = list(range(11,21)), c=list(range(21,31)))
print(d)

#access the third value of dictionary d from b

print(d['b'][3])

for key,value in d.items():
    print(key,"has value",value)


