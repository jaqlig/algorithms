from random import uniform
from random import random

def cuckoo(function, args, generations, left, right, n, remove_chance):
    
    eggs = []
    
    # initialize and sort population with random eggs
    for i in range(n):
        vars = []
        for j in range(args):
            vars.append(uniform(left, right))
        eggs.append(vars)

    eggs.sort(key=lambda x: function(*x))
 
    # main loop 
    for y in range(generations):

        # create temp eggs and add random value
        temp_eggs = []
        for i in range(len(eggs)):
            temp_eggs.append(eggs[i].copy())
            for j in range(args):
                temp_eggs[i][j] += uniform(left, right)

        temp_eggs.sort(key=lambda x: function(*x))

        # check if temp eggs are better than old
        for i in range(n):
            if all(left <= x <= right for x in temp_eggs[i]):
                if function(*eggs[i]) < function(*temp_eggs[i]):
                    eggs[i] = temp_eggs[i].copy()

        # remove random eggs
        for i in range(n):
            if remove_chance >= random():
                vars = []
                for j in range(args):
                    vars.append(uniform(left, right))
                eggs[i] = vars

        eggs.sort(key=lambda x: function(*x))
        # uncomment to see every population
        # print("generation", y+1, "->", eggs)
    
    return eggs[-1]

# example:

def function(x, y):
    return x * y

# cuckoo algorithm is trying to maximize given function for arguments from <left range> to <right range>
print(cuckoo(function, 2, 50, -10, 10, 500, 0.6))
# cuckoo(<function>, <argument amount>, <generations>, <left range>, <right range>, <population size>, <chance for removing egg>)
