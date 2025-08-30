 thisdict = {
    # key:value 
    "brand":"ford",
    "model":"mustang",
    "year":1964
}

thisdict2 = {
    # key:value 
    "brand":"ford",
    "model":"mustang",
    "year":1964,
    "year":2020
}

print(thisdict)
print(thisdict2)
print(thisdict["brand"])
print(len(thisdict),type(thisdict))

thisdict3=dict(name="sumit",age=22,country="pakistan")
print(thisdict3,type(thisdict3))
x=thisdict["model"]
print(x)
print(thisdict.get("model"))
y=thisdict.keys()
print(y)
z=thisdict.values()
print(z)

personal_info={
    "name":"sumit",
    "age":22,
    "Email":"Skk222111@gmail.com"
}
print(personal_info)
personal_info["number"]=9237272799
print(personal_info)
x=personal_info.items()
print(x)

if "name" in personal_info:
    print("yes name is present in personal_info")

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1993
}
thisdict["year"]=2020
print(thisdict)
thisdict.update({"brand":"ferrari"})
print(thisdict)

thisdict["color"]="red"
print(thisdict)

print(thisdict)
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict['year']
print(thisdict)
del thisdict
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

thisdict={
    "name":"sumit",
    "age":22,
    "school":"Beacon house"
}
for x in thisdict.keys():
    print(x)

for x,y in thisdict.items():
    print(x,y)


mydict=thisdict.copy()
mydict=dict(thisdict)
print(mydict)

myfamily={
    "child1":{
        "name":"Raj",
        "age":22
    },
    "child2":{
        "name":"satya",
        "age":12
    },
    "child3":{
        "name":"suresh",
        "age":10
    }
}

print(myfamily)
myfamily.popitem()
print(myfamily)
for x,y in myfamily.items():
    print(x,y)

child1={
    "name":"Kirtan",
    "year":2010
}
child2={
    "name":"Jitesh",
    "year":2006
}
child3={
    "name":"Pankaj",
    "year":2000
}

myfamily={
    "child1":child1,
    "child2":child2,
    "child3":child3
}

for x,y in myfamily.items():
    print(x,y)
    

for x in myfamily.keys():
    print(x)

for x in myfamily.values():
    print(x)

print(myfamily["child2"]["name"])
        
for x, obj in myfamily.items():
  print(x)

for y in obj:

    print(y + ':', obj[y])
