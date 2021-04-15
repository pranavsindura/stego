from random import randint, shuffle
from psnr import psnr
from embedder import embed
import math

population = []
MUTATION_RATE = 1
ITERS = 10
POPULATION_SIZE = 100
LEN = 28 
# Length of chromosome
# Direction  3
# X_off      9
# Y_off      9
# Bit Planes 4
# SB Pole    1
# SB Dir     1
# BP Dir     1
# ------------
#           28

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
    # select 10% bad
    new_population = []
    N = int(0.4 * POPULATION_SIZE)
    new_population += population[:N]

    M = int(0.1 * POPULATION_SIZE)
    new_population += population[-M:]
    population = new_population[::]

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
            chance = randint(1, 100)
            if chance <= MUTATION_RATE:
                population[i] ^= 1 << j

def find_embedding(host, secret):
    global population
    init_population()
    gen = 0
    while gen < ITERS:
        # Generation gen, output every 100th generation to see improvement
        gen += 1
        print("Gen:", gen)
        # Sort the population based on fitness
        # population[0] is the best chromosome in the population
        population.sort(key=lambda x:fitness(host, secret, x), reverse=True)
        print(*population[:10])
        print("Fitness", fitness(host, secret, population[0]))
        # Selection
        selection()
        print("Selection")
        # Crossover
        crossover()
        print("Crossover")
        # Mutation
        mutation()
        print("Mutation")
    population.sort(key=lambda x:fitness(host, secret, x), reverse=True)
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