
import random
import itertools
import math
from collections import Counter

BUNDLING_FACTOR = 10


class Gene:
    def __init__(self, allocation):
        self.allocation = allocation
        self.total_capacity_used = sum(allocation.values())

    def __str__(self):
        return "Allocation: " + str(self.allocation) + ", Total_cost: " + str(self.total_capacity_used)

    def __gt__(self, other):
        return self.total_capacity_used > other.total_capacity_used


class Demand:
    def __init__(self, parsed_demand, id):
        self.volume = parsed_demand['demand_volume']
        self.paths = parsed_demand['paths']
        self.id = id
        self.all_genes = []
        self.used_gene_index = 0

    def __str__(self):
        return "Demand id: " + str(self.id) + ", volume: " + str(self.volume) + ", paths: " + str(self.paths)

    def __gt__(self, other):
        return len(self.all_genes) > len(other.all_genes)

    def get_gene(self):
        return self.all_genes[self.used_gene_index]

    def skip_gene(self):
        self.used_gene_index += 1

    def get_path_by_id(self, id):
        return self.paths[id]

    def generate_all_genes(self):
        all_path_combinations = itertools.product(range(0, len(self.paths)), repeat=math.floor(self.volume/BUNDLING_FACTOR))

        all_link_combinations = []
        for combination in all_path_combinations:
            all_link_combinations.append(list(map(self.get_path_by_id, combination)))

        flattened_all_link_combinations = []
        for link_combination in all_link_combinations:
            flattened_all_link_combinations.append(list(itertools.chain.from_iterable(link_combination)))

        allocations = []
        for flattened_all_link_combination in flattened_all_link_combinations:
            allocations.append(dict(Counter(flattened_all_link_combination)))

        for allocation in allocations:
            for link in allocation.keys():
                allocation[link] *= BUNDLING_FACTOR

        self.all_genes = []
        for allocation in allocations:
            if self.volume % BUNDLING_FACTOR == 0:
                self.all_genes.append(Gene(allocation))
            else:
                leftover_volume = self.volume % BUNDLING_FACTOR
                for path in self.paths:
                    temp_allocation = {}
                    for link in path:
                        temp_allocation[link] = leftover_volume
                    c = Counter(temp_allocation)
                    c.update(allocation)
                    self.all_genes.append(Gene(dict(c)))

        self.all_genes.sort()


class Link:
    def __init__(self, parsed_ink, id):
        self.module_cost = parsed_ink['module_cost']
        self.module_volume = parsed_ink['link_module']
        self.number_of_modules = parsed_ink['number_of_modules']
        self.max_capacity = self.module_volume * self.number_of_modules
        self.id = id

    def __str__(self):
        return "Link id: " + str(self.id) + ", module_cost: " + str(self.module_cost) + \
               ", module_volume: " + str(self.module_volume) + ", number_of_modules: " + str(self.number_of_modules) + \
               ", max_capacity: " + str(self.max_capacity)


def get_gene_from_demand(demand):
    return demand.get_gene()


def negative_capacity(capacity):
    return capacity < 0


class ChromosomeFactory:

    def __init__(self, demands, links):
        self.demands = demands
        self.genes = list(map(get_gene_from_demand, demands))
        total_alocations = Counter()
        for gene in self.genes:
            total_alocations.update(Counter(gene.allocation))
        self.total_alocations = dict(total_alocations)

        capacity_leftovers = {}
        for link in links:
            capacity_leftovers[link.id] = link.max_capacity
        capacity_leftovers = Counter(capacity_leftovers)

        capacity_leftovers.subtract(total_alocations)
        print(dict(capacity_leftovers))


class EvolutionAlgorithm:
    def __init__(self, links, demands, seed, population_size, generations, mutation_prob):
        self.links = links
        self.demands = demands
        self.seed = seed
        self.population_size = population_size
        self.initial_pairs = population_size / 2
        self.mutation_prob = mutation_prob
        self.generations = generations
        self.chromosomes = [[]]

        if self.population_size % 2 != 0:
            raise Exception('Population size should be even')

        if seed > 0:
            self.random = random.Random(seed)
        else:
            self.random = random.Random()

        # Remove redundant data from links, add necessary data
        for i in range(0, len(links)):
            self.links[i] = Link(links[i], i+1)

        # Remove redundant data from demands, add necessary data
        for i in range(0, len(demands)):
            self.demands[i] = Demand(demands[i], i+1)

        # Generate all genes for all demands
        for demand in self.demands:
            demand.generate_all_genes()
        demands.sort()

        c = ChromosomeFactory(demands, links)
        print(c.total_alocations)
