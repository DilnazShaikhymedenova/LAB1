thislist = ["orange", "mango", "kiwi","pineapple", "banana"]
thislist.sort()
print(thislist)
#sort the list alphabetically


thislist = [100,50,65,82,23]
thislist.sort()
print(thislist)


thislist = ["orange", "mango", "kiwi","pineapple","banana"]
thislist.sort(reverse = True)
print(thislist)
#sort list in descending



thislist = [100,50,65,82,23]
thislist.sort(reverse = True)
print(thislist)


def myfunc(n):
    return abs(n-50)

thislist = [100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)



thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#Uppercase letter will be first than lower case letter


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#if we want that lower case words will sorted first



thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#reversing the order of the list





