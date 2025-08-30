def my_function():
    print("Hello from my_function")

my_function()

def your_name(name):
    print(f"Hello! {name}")

your_name("Raj")

def full_name(fname,lname):
    print(f"Your full name is {fname} {lname}")

full_name("sumit","raj")

def my_family(*kids):
    print(f"Your 2nd child is {kids[1]}")

my_family("A","B","C")

def my_function(child3,child2,child1):
    print(f"Your youngest child is {child3}")

my_function(child1="A",child2="B",child3="C")

def my_function(**kids):
    print("his last name is" ,{kids["lname"]})

my_function(fname="Sumit",lname="Raj")

def default_function(country="pakistan"):
    print("Your country name is "+country)

default_function("United Kingdom")
default_function()

def my_function(food):
    for x in food:
        print(x)

fruits=["apple","banana","cherry"]
my_function(fruits)

def my_function(x):
    return 5*x

print(my_function(3))
print(my_function(2))
print(my_function(6))
print(my_function(4))

def function1(*,x):
    print(x)

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname=1,lname="2")

function1(x=747)

def myfun(x,/):
    print(x)

myfun(2)

def special_function(a,b,/,*,c,d):
    print(a,b,c,d)

special_function("aa","bb",c=123,d=345)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)


