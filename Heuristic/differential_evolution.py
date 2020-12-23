from random import uniform
from random import random
from random import shuffle
import math


def differential(function, args, generations, left, right, n, mutation_control, crossover_chance):
    
    agents = []
    
    # initialize population with random agents
    for i in range(n):
        vars = []
        for j in range(args):
            vars.append(uniform(left, right))
        agents.append(vars)

 
    # main loop 
    for y in range(generations):

        # mutation vectors
        vectors = []

        # for every agent in population
        for i in range(n):
            
            rand_agent_indexes = []
            for j in range(n):
                if j == i: continue
                rand_agent_indexes.append(j)

            shuffle(rand_agent_indexes)

            ag_index_a = rand_agent_indexes.pop(-1)
            ag_index_b = rand_agent_indexes.pop(-1)
            ag_index_c = rand_agent_indexes.pop(-1)

            mut_v = agents[ag_index_b].copy()
            
            for k in range(len(mut_v)):
                mut_v[k] -= agents[ag_index_c][k]
            
            for k in range(len(mut_v)):
                mut_v[k] *= mutation_control

            for k in range(len(mut_v)):
                mut_v[k] += agents[ag_index_a][k]

            vectors.append(mut_v)

        # crossover
        crossed = []
        for i in range(len(agents)):
            crossed.append(agents[i].copy())

        for i in range(n):
            for j in range(args):
                if crossover_chance >= random():
                    crossed[i][j] = vectors[i][j]

        # check if new are better
        for i in range(n):
            if all(left <= x <= right for x in crossed[i]):
                if function(*agents[i]) < function(*crossed[i]):
                    agents[i] = crossed[i]
        
        
        # uncomment to see every population
        # print("generation", y+1, "->", agents)
    
    best = agents[0]
    for i in range(len(agents)):
        if function(*best) < function(*agents[i]):
            best = agents[i]
    return best

# example:

def function(x, y):
    return math.exp(math.cos(x)) * x - y

# differential evolution is trying to maximize given function for arguments from <left range> to <right range>
print(differential(function, 2, 500, -10, 10, 10, 0.5, 0.5))
# differential(<function>, <argument amount>, <generations>, <left range>, <right range>, <population size (>=3)>, <mutation size>, <crossover chance>)
