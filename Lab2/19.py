#Update tuples

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#tule is unchangable, in order to change it, we can change to the list firstly, then to the tuple again



thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#changing to the list and adding "orange"


thistuple = ("apple", "banana", "cherry")
y = ("orange")
thistuple += y
print(thistuple)


thistuple = ("apple", "banana","cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#convert to the list, remove "apple" and convert it back


thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists




