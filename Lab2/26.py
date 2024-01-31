#Remove Set Items

myset = {"apple", "banana", "cherrry"}
myset.remove("banana")

print(myset)
#removes the "banana" from the set


myset = {"apple", "banana", "cherrry"}
myset.discard("banana")
print(myset)
#remove "banana" by using discard() method


myset = {"apple", "banana", "cherrry"}
x = myset.pop()
print(x)
print(myset)
#removing random item using the pop() method


myset = {"apple", "banana", "cherrry"}
myset.clear()
print(myset)
#clears the set , method which empties the set


myset = {"apple", "banana", "cherrry"}
del myset
print(myset)
#del keyword will delete the set completely




