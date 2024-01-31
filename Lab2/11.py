#Remove List Items

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)



thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)
#removes the first occurance of the "banana"


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#remove 2nd item


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#removes the last item


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#deletes  the 1st element 


thislist = ["apple", "banana", "cherry"]
del thislist
#deletes the list


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#clears the whole list



