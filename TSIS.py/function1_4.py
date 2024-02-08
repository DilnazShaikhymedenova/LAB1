def filter_prime(c):
    i = 2
    while i < c:
        if c%i==0:
            return False
        else:
            i += 1
    return True
a = "1 4 3 5 6 8 2 7"#result we want to see: 1, 3, 5, 2, 7
b = []
for x in a:
    if ord(x) != 32:
        b.append(ord(x) - 48)
    else:
        continue
for x in b:
    if filter_prime(x):
        print(x)
    else:
        continue