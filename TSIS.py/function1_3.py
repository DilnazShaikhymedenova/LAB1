numheads = 35
numlegs = 94
def solve(numheads, numlegs):
    numrabbits = (numlegs - numheads)//3
    numchickens = (numlegs - numheads)%3
    print(numrabbits," rabbits, and ",numchickens," chickens")
solve(numheads, numlegs)