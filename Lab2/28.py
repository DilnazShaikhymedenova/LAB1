#Join Sets

set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = set1.union(set2)

print(set3)
#joining the set by using union() method


set1 = {"a", "b", "c"}
set2 = {1,2,3}
set1.update(set2)

print(set1)
#using update() method inserts the items in set2 into set1


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
#intersection_update() method will keep only items that are present in both sets



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection_update(y)

print(z)
#intersection() method will return a new set, that only contains the items that are present in both sets


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
#keep all, but not duplicates, or keep items that are not present in both sets


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmmetric_difference(y)

print(z)
#method which returns new set, that contains only the elements are not present in both sets


x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple",2}

z = x.intersection_update(y)

print(z)
