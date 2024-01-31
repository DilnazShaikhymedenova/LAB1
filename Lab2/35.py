#Loop Dictionary

thisdict = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}

for x in thisdict:
    print(x)
#print all key names in dict


thisdict = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
for x in thisdict:
    print(thisdict[x])
#print all values in the dictionary, one by one


thisdict = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}

for x in thisdict.values():
    print(x)
#USE values() method to return values of a dict
    


thisdict = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
for x in thisdict.keys():
    print(x)
#keys() method to return the keys of a dict
    


thisdict = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
for x,y in thisdict.items():
    print(x,y)
#loop through the both keys and values using items() method
    


