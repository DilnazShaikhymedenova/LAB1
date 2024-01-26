if 5 > 2:
    print("Five is greater than two!")

if 5 > 2:
    print("Five is greater than two!")

x = 5
y = "Hello World"

#This is a comment
print ("Hello World")

print("Hello World") #This is a comment

print("Hello")
#print("Cheers")

#This is 
#a comment
#more than justone line

x = 4
x = "Sally"

print(x)

x = str(3)
y = int(3)
z = float(3)

x = "John"
#is the same as 
x = 'John'

a = 4
A = "sally"
#A will not overwrite a

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#our variable can start with these types
#but cannot start with numbers
#2myvar = "John"

myVariableName = "John" #Camel case
MyVariableName = "John" #Pascal case
my_variable_name = "John"#snake case

x,y,z = "Orange","Banana","Cherry"
print(x)
print(y)
print(z)

x=y=z = "Orange"
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

x = "Python"
y = "is"
z = "awesome"
print(x+y+z)

x = 5
y = 10
print(x+y)

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is" + x)

myfunc()

print("Python is" + x)

#second case when we want to change the x inside the function
x = "awesome"

def myfunc():
    global x
    x = "fantastic"
myfunc()

print("Python is " + x)


x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

x = int(1)
y = int(2.8)
z = ("3")

x = int(1)
y = int(2.8)
z = ("3")
w = ("4.2")
print(x)
print(y)
print(z)
print(w)

x = str("s1")
y = str(2)
z = str(3.0)

print('Hello')
print("hello")

a = "Hello World"
print(a)

a = "Hello World!"
print(a[1])

for x in "banana":
    print(x)

a = "Hello,World!"
print(len(a))

a = "Hello,  World!"
print(a.split("," )) 

a = "Hello"
b = "World"
c = a+b
print(c)

a = "Hello"
b = "World"
c = a+ " " + b
print(c)

b = "Hello World!"
print(b[2:])

b = "Hello World!"
print(b[:5])


b = "Hello World!"
print(b[-5:-2])



age = 36
txt = "My name is John and I am {}"
print(txt.format(age))

quantity = 3
itemno =  567
price = 49.95
myorder = "I want {} pieces of item {} for{} dollars"
print(myorder.format(quantity,itemno,price))

quantity = 3
itemno =  567
price = 49.95
myorder = "I want {0} pieces of item {1} for{2} dollars"
print(myorder.format(quantity,itemno,price))


txt = "We are so-called \"Vikings\" from the north"
print(txt)



