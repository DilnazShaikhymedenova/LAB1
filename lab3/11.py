#Lambda - small anonym function, take any number of arguments, but can only have one expression

x = lambda a : a + 10
print(x(5))

x = lambda a,b : a * b
print(x(5,6))


x = lambda a, b, c : a+b+c
print(x(5, 6, 2))


def myfunction(n):
    return lambda a : a * n

mydoubler = myfunction(2)

print(mydoubler(11))



def function(n):
    return lambda a : a * n

mytripler = myfunction(3)

print(mytripler(11))

def myfunction(n):
    return lambda a : a * n
mydoubler = myfunction(2)
mytripler = myfunction(3)

print(mydoubler(11))
print(mytripler(11))

