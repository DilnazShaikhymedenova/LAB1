a = str(input())#you are free
def my_function(a):
    b = list(a.split(" "))
    c = str()
    i = len(b) - 1
    while i != -1:
        if i == len(b) - 1:
            c = c + b[i]
        else:
            c = c + " " + b[i]
        i -= 1
    print(c)
my_function(a)