#Add list Items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#adds element to the end of the list


thislist = ["apple", "banana", "cherry"]
thislist.insert(1,"orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#appending elements from another list to the current list
#adding elements of tropical to thislist


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#adds elements of a tuple to a list



