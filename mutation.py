import random
from client import *
import time
import numpy as np
from config import *

random.seed(time.time())

def mutation(person, mutation_prob, deviation):
    new = []
    for i in range(0,MAX_DEG):
        if random.uniform(0,1) < mutation_prob:
            new.append(person[i] + random.uniform(-deviation, deviation))
        else:
            new.append(person[i])
            # person[i] = person[i] + random.uniform(-deviation, deviation)
    return new

def mutation_generation_first():
    new = []
    for i in range(0,MAX_DEG):
        if random.uniform(0,1) < 3/11:
            new.append(INITIAL_ARR[i] * random.uniform(0.3,1.7))
        else:
            new.append(0)
            # person[i] = person[i] + random.uniform(-deviation, deviation)
    return new


def mutation_two(child):
    for index, val in enumerate(child):
        if random.uniform(0,1) < 3/11:
            change = child[index] * random.uniform(0.3,1.7)
            if abs(change) <= 10:
                child[index] =  change
            if child[index] == 0:
                if random.uniform(0,1)<0.6:
                    child[index] += random.uniform(-10**-8, 10**-8)    
    return child