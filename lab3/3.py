#Arbitary Arguments

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "linus")
#If the number of arguments is unknown, add a * before the parameter name



def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#arguments with the  key = value syntax




