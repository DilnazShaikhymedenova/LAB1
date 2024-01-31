#IF.... ELSE

a = 33
b = 200
if b > a:
    print("b is greater than a")



a = 33
b = 200
if b >a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
#elif = if previous condition is not true


a = 33
b = 200
if b >a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")  
else:
    print("a is greater than b")
#if elif is not true, then else will work
    


a = 33
b = 200
if b >a:
    print("b is greater than a")
else:
    print("b is not greater than a")
#alse can use else without elif
    

a = 200
b = 33
#SHORTHAND
if a>b: print("a is greater than b")



a = 2
b = 330
print("A") if a > b else print("B")
#If... Else condition


a = 330
b = 330
print("A") if a > b else print("B") if a == b else print("B")
#3 condition in one line



a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
#AND logical operator
    

a = 200
b = 33
c= 500
if a > b or a > c:
    print("At least one of the condition is True")
#OR logical operator
    


a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")
#NOT logical operator
    


x = 41
if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above 20")
    else:
        print("but not above 20")
#Nested IF
        

a = 33
b = 200
if b > a:
    pass
#to avoiding from getting an error use pass







