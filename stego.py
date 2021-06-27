from random import randint, shuffle
from psnr import psnr
from embedder import embed
import math
import numpy as np
from datetime import datetime

population = []
MUTATION_RATE = 0.1
ITERS = 1
POPULATION_SIZE = 1
LEN = 35  
# Chromosome
# Gene       | Length
# -------------------
# x0         |    10
# X_off      |     9
# Y_off      |     9
# Bit Planes |     4
# SB Pole    |     1
# SB Dir     |     1
# BP Dir     |     1
# ------------------
#            |    35

def init_population():
    global population
    population = []
    for i in range(POPULATION_SIZE):
        p = randint(1, 1 << LEN) - 1
        population.append(p)

def fitness(host, secret, chromosome):
    """more the psnr, more fit the stego image is"""
    stego = embed(host, secret, chromosome)
    if stego is None:
        return -math.inf
    return psnr(host, stego)

def selection():
    global population
    # select 40% good
    N = int(0.4 * POPULATION_SIZE)
    while len(population) > N:
        population.pop()

def crossover():
    global population
    new_population = population[::]
    while len(new_population) < POPULATION_SIZE:
        L = randint(1, len(population) - 1) - 1
        R = randint(L + 1, len(population)) - 1
        if randint(0, 1):
            L, R = R, L
        P = population[L]
        Q = population[R]
        child = 0
        mask = randint(1, 1 << LEN) - 1
        revmask = (1 << LEN) - 1 - mask
        child = (P & mask) | (Q & revmask)
        new_population.append(child)
    population = new_population[::]

def mutation():
    global population
    for i in range(POPULATION_SIZE):
        for j in range(LEN):
            chance = randint(1, 10000)
            chance /= 10000
            if chance <= MUTATION_RATE:
                population[i] ^= 1 << j

def find_embedding(host, secret):
    global population
    init_population()
    gen = 0
    while gen < ITERS:
        assert len(population) == POPULATION_SIZE
        gen += 1
        print("Gen:", gen)
        # Sort the population based on fitness
        # population[0] is the best chromosome in the population
        # population.sort(key=lambda x:fitness(host, secret, x))
        before_timestamp = datetime.now()
        population = [(fitness(host, secret, x), x) for x in population]
        population.sort(reverse=True)
        population = [x[1] for x in population]
        after_timestamp = datetime.now()

        print('Took', (after_timestamp - before_timestamp).total_seconds(), 's')

        print(*population[:10])
        print("Fitness", fitness(host, secret, population[0]))
        if gen == ITERS:
            break
        # Selection
        selection()
        print("Selection")
        # Crossover
        crossover()
        print("Crossover")
        # Mutation
        mutation()
        print("Mutation")
                         
    return population[0]

def encrypt(host_img, secret_img):
    # Convert both to relevant format
    host = host_img
    secret = secret_img
    # Pass on to genetic algorithm
    key = find_embedding(host, secret)

    stego_img = embed(host_img, secret_img, key)
    # Encrypt key if needed
    return stego_img, key

def decrypt(stego_img, key):
    # Use key as a genome to retieve data
    host_img = stego_img
    secret_img = stego_img
    return host_img, secret_img


if __name__ == '__main__':
    print('Hello Stego')