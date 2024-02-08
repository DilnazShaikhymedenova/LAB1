from itertools import permutations
def print_permutations():
    s = input("String : ")
    a = permutations(s) 
    
    print("All permutations : ")
    for x in a:
        print(''.join(x))
print_permutations() 
