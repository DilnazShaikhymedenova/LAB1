#Accessing Items

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = thisdict["model"]
#getting the "model" key


x = thisdict.get("model")


x = thisdict.keys()
#returning key values\


car = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change

car["color"] = "white"

print(x) #after change


x = thisdict.values()
#get a list of the values



car = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change

car["year"] = 2020

print(x) #after change


car = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change

car["color"] = "red"

print(x) #after change
#changing the values of the dictionary



x = thisdict.items()
#getting (key and value)
car = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change

car["year"] = 2020

print(x) #after change



car = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change

car["color"] = "red"

print(x) #after change



car = {
    "brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in car:
    print("Yes, 'model' is one   the keys in dict")
#checking if "model" is in our dict





     