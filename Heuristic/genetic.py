from random import uniform
from random import random

def genetic(function, args, generations, left, right, n, mutation_chance, crossover_chance):

    def getFromInterval(interval, number):
        if interval[0] != 0.0:
            interval.insert(0, 0.0)
        for i in range(len(interval)):
            if interval[i] <= number < interval[i+1]:
                return i
    
    individuals = []
    
    for i in range(n):
        vars = []
        for j in range(args):
            vars.append(uniform(left, right))
        individuals.append(vars)
  
    for y in range(generations):

        fitness_total = 0
        for i in individuals:
            fitness_total += function(*i)
            
        fitness = []
        fitness_sum = 0
        for i in individuals:
            chance = function(*i)/fitness_total
            fitness.append(chance + fitness_sum)
            fitness_sum += chance

        # two candidates are chosen every generation
        interval_a = getFromInterval(fitness, random())
        interval_b = getFromInterval(fitness, random())

        ind_a = individuals[interval_a].copy()
        ind_b = individuals[interval_b].copy()
        ind_aC = [] 
        ind_bC = []

        # mutation
        for i in range(args):
            mutation_a = uniform(-(abs(left)+abs(right)), abs(left)+abs(right)) * 1/10
            mutation_b = uniform(-(abs(left)+abs(right)), abs(left)+abs(right)) * 1/10

            if random() <= mutation_chance:
                ind_a[i] += mutation_a
            if random() <= mutation_chance:
                ind_b[i] += mutation_b

        # crossover 
        if random() <= crossover_chance:
            rand = random()            

            # a
            for i in range(len(ind_a)):
                ind_aC.append(ind_b[i] - ind_a[i])
            
            ind_aC = [x * rand for x in ind_aC]

            for i in range(len(ind_aC)):
                ind_aC[i] += ind_a[i]

            # b
            for i in range(len(ind_b)):
                ind_bC.append(ind_a[i] - ind_b[i])
            
            ind_bC = [x * rand for x in ind_bC]

            for i in range(len(ind_bC)):
                ind_bC[i] += ind_b[i]
        else:
            for i in range(len(ind_a)):
                ind_aC.append(ind_a[i])
                ind_bC.append(ind_b[i])

        # check if new are better
        if all(left <= x <= right for x in ind_aC):
            if function(*individuals[interval_a]) < function(*ind_aC):
                individuals[interval_a] = ind_aC

        if all(left <= x <= right for x in ind_bC):
            if function(*individuals[interval_b]) < function(*ind_bC):
                individuals[interval_b] = ind_bC
        
        # uncomment to see every population
        # print("generation:", y+1, individuals)
    
    best = individuals[0]
    for i in range(len(individuals)):
        if function(*best) < function(*individuals[i]):
            best = individuals[i]
    return best

# example:

def function(x, y, z):
    return x*x - y - z

# genetic is trying to maximize given function for arguments from <left range> to <right range>
print(genetic(function, 3, 8000, -10000, 10000, 5, 0.4, 0.5))
# genetic(<function>, <argument amount>, <generations>, <left range>, <right range>, <population size>, <mutation chance>, <crossover chance>)
