import random
from client import *
import time
random.seed(time.time())
from mutation import *

def sex(parent1, parent2, mutation_prob, deviation):
    child1 = []
    child2 = []
    for i, val in enumerate(parent1):
        if random.randint(0,1) == 1:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child2.append(parent1[i])
            child1.append(parent2[i])
    mutation(child1, mutation_prob, deviation)
    mutation(child2, mutation_prob, deviation)
    return [child1, child2]

def sex_two(parent1,parent2):
    child1 = []
    child2 = []
    u = random.uniform(0,1)
    n_c = 2
    beta = 0
    if u <=0.5:
        beta = (2 * u)**((n_c + 1)**-1)
    else:
        beta = ((2*(1-u))**-1)**((n_c + 1)**-1)
    
    for index,val in enumerate(parent1):
        child1.append(0.5*((1 + beta) * parent1[index] + (1 - beta) * parent2[index]))
        child2.append(0.5*((1 - beta) * parent1[index] + (1 + beta) * parent2[index]))
    
    return [child1,child2]
    