import glob
k=[]

fl=glob.glob("letters1/*.txt")
c="python"
for  fname in fl:
    with open(fname,"r") as file:
        j=file.read().strip("\n")
        if j in c:
            k.append(j)
print(k)

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
d['employees'][1]['lastname']='smooth'
print(d['employees'][1]['lastname'])
d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
print(d['employees'])
import json

d = {"employees": [{"firstName": "John", "lastName": "Doe"},
                   {"firstName": "Anna", "lastName": "Smith"},
                   {"firstName": "Peter", "lastName": "Jones"}],
     "owners": [{"firstName": "Jack", "lastName": "Petter"},
                {"firstName": "Jessy", "lastName": "Petter"}]}

with open("company1.json", "w") as file:
    json.dump(d, file, indent=4, sort_keys=True)

