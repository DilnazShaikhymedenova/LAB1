#Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print (thistuple[1])

thistuple = ("apple", "banana", "cherry")
print (thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "mango", "melon")
print(thistuple[2:5])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "mango", "melon")
print(thistuple[:4])
#kiwi not included, but starts from beginning


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "mango", "melon")
print(thistuple[2:])
#from cherry to the end


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "mango", "melon")
print(thistuple[-4:-1])
#from index -4(included) to index -1(excluded)


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")



