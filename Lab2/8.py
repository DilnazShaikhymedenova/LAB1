thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#for access items
#NOTE! the first item has index 0;

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#if index is negative, means it will start from the end

thislist = ["apple", "banana","cherry","mango", "kiwi", "melon","orange"]
print(thislist[2:5])

#range of indexes, here returns from third, fourth and fifth item in the list

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#starts from beginning and goes to the range

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#starts from 2nd index and goes to the end

thislist =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#here 4th item from the end and till -1 th element

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


          

