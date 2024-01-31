#Remove Dictionary Items

thisdict = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.pop("model")
print(thisdict)
#removing the item with specified key by using pop() method



thisdict = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.popitem()
print(thisdict)
#popitem() removes the last inserted item



thisdict = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
del thisdict["model"]
print(thisdict)
#del keyword removes the item with specified key name
#if dictionary is longer, del cannot delete the dictionary completely.Otherwise, it can delete the dictionary completely


thisdict = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.clear()
print(thisdict)
#clear() method empties the dictionary





