a = str(input())#you are free
def my_function(a):
    b = list(a.split(" ")) #storing the string in list b
    c = str() #for storing the reversed string
    i = len(b) - 1 #index of the last element of list b
    while i != -1:
        if i == len(b) - 1:
            c = c + b[i] #without any space
        else:
            c = c + " " + b[i] #having preceding space
        i -= 1 #decrement by 1, to move to the prev v
    print(c)
my_function(a)