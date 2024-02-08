a = [1, 1, 3, 3]#function must return true
b = [1, 3, 2, 1, 3]#function must return false
def has_33(num):
    ft = False
    i = 0
    while i != len(num):
        if ft == False:
            if num[i] == 3:
                ft = True
        else:
            if num[i] == 3:
                return True
            else:
                ft = False
        i += 1
    return False
print(has_33(a))
print(has_33(b))