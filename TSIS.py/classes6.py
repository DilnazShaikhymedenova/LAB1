a = [1, 3, 4, 5, 2, 34, 7, 6]#result we want to see: 1, 3, 5, 2, 7
def filter(b):
    i = 2
    while i < b:
        if b%i == 0:
            return False
        else:
            i += 1
    return True
    
for x in a:
    if filter(x):
        print(x)
    else:
        continue



