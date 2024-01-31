#List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

    print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi","mango"]

newlist = [x for x in fruits if "a" in x]

print (newlist)


newlist = [x for x in fruits]
#with no if statement


newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5]
print(newlist)



newlist = [x.upper() for x in fruits]
print (newlist)


newlist = ['hello' for x in fruits]
print(newlist)
#set all values in the newlist to 'hello'


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)






