def my_function(*,x):
    print(x)

my_function(x=3)
#the result will be 3


def my_function(x):
    print(x)

my_function(3)
#when here we add *, / we will get an error


#Positional Only and Keyword Only
def my_function(a,b,/,*,c,d):
    print(a+b+c+d)

my_function(5,6,c = 7,d = 8)

