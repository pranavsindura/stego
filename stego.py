from random import randint, shuffle

population = []
MUTATION_RATE = 1
ITERS = 1000
POPULATION_SIZE = 100
LEN = 27

def init_population():
    population = []
    for i in range(POPULATION_SIZE):
        p = 0
        for j in range(LEN):
            b = randint(0, 1)
            p = p | (b << j)
        population.append(p)

def fitness(host, secret, chromosome):
    new_population = []

def selection():
    # select 40% good
    # select 10% bad
    new_population = []
    N = int(0.4 * POPULATION_SIZE)
    new_population += population[:N]

    M = int(0.1 * POPULATION_SIZE)
    new_population += population[-M:]
    population = new_population[::]

def crossover():
    new_population = []

def mutation():
    new_population = []

def find_embedding(host, secret):
    init_population()
    gen = 0
    while gen < ITERS:
        # Generation gen, output every 100th generation to see improvement
        gen += 1
        # Sort the population based on fitness
        # population[0] is the best chromosome in the population
        population.sort(key=lambda x:fitness(host, secret, x))

        # Selection
        selection()
        # Crossover
        crossover()
        # Mutation
        mutation()
    return population[0]



def encrypt(host_img, secret_img):
    # Convert both to relevant format
    host = host_img
    secret = secret_img
    # Pass on to genetic algorithm
    stego_img, key = find_embedding(host, secret)

    # Encrypt key if needed
    return stego_img, key

def decrypt(stego_img, key):
    # Use key as a genome to retieve data
    host_img = stego_img
    secret_img = stego_img
    return host_img, secret_img


if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,10]
    print(A)
    print(A[::])