import random


class Demand:
    def __init__(self, parsed_demand, id):
        self.volume = parsed_demand['demand_volume']
        self.paths = parsed_demand['paths']
        self.id = id

    def __str__(self):
        return "Demand id: " + str(self.id) + ", volume: " + str(self.volume) + ", paths: " + str(self.paths)


class Link:
    def __init__(self, parsed_ink, id):
        self.module_cost = parsed_ink['module_cost']
        self.module_volume = parsed_ink['link_module']
        self.number_of_modules = parsed_ink['number_of_modules']
        self.max_capacity = self.module_volume * self.number_of_modules
        self.id = id

    def __str__(self):
        return "Link id: " + str(self.id) + ", module_cost: " + str(self.module_cost) +\
               ", module_volume: " + str(self.module_volume) + ", number_of_modules: " + str(self.number_of_modules) +\
                ", max_capacity: " + str(self.max_capacity)


class Gene:
    def __init__(self, demand, mutation_prob, random):
        self.random = random
        self.demand = demand
        self.mutation_prob = mutation_prob
        self.allocations = {}

        for pathNumber in range(0, len(demand.paths)):
            self.allocations[pathNumber] = 0

        for volumeUnit in range(0, demand.volume):
            self.allocations[self.random.randint(0, len(demand.paths)-1)] += 1

    def attempt_mutation(self):
        if len(self.allocations) <= 1:
            return
        random_result = self.random.random()
        if random_result >= self.mutation_prob:
            print("no mutation")
            return
        print("Mutation")
        allocation_to_reduce = self.random.choice(list(self.allocations))
        while self.allocations[allocation_to_reduce] == 0:
            allocation_to_reduce = self.random.choice(list(self.allocations))

        allocation_to_increase = allocation_to_reduce
        while allocation_to_increase == allocation_to_reduce:
            allocation_to_increase = self.random.choice(list(self.allocations))

        self.allocations[allocation_to_reduce] -= 1
        self.allocations[allocation_to_increase] += 1

    def get_links_load(self):
        link_loads = {}
        for allocation in self.allocations:
            for link in self.demand.paths[allocation]:
                if link not in link_loads.keys():
                    link_loads[link] = 0
                link_loads[link] += self.allocations[allocation]
        return link_loads


class Chromosome:
    def __init__(self, demands, links, mutation_prob, random):
        self.random = random
        self.genes = []
        self.links = links
        self.mutation_prob = mutation_prob
        chromosome_valid = False

        while not chromosome_valid:
            for demand in demands:
                new_gene = Gene(demand, mutation_prob, self.random)
                self.genes.append(new_gene)

            chromosome_valid = self.validate()

    def validate(self):
        for gene in self.genes:
            gene_links_load = gene.get_links_load()
            for link in gene_links_load:
                if gene_links_load[link] > self.links[link-1].max_capacity:
                    return False
        return True

    def get_cost(self):
        cost_table = {}
        total_cost = 0
        for link in self.links:
            cost_table[link.id] = 0
        for gene in self.genes:
            gene_links_load = gene.get_links_load()
            for link_load in gene_links_load:
                cost_table[link_load] += gene_links_load[link_load]
        for link_id in cost_table:
            bought_capacity = 0
            while bought_capacity < cost_table[link_id]:
                bought_capacity += self.links[link_id-1].module_volume
                total_cost += self.links[link_id-1].module_cost
        return total_cost

class Offspring(Chromosome):
    def __init__(self, mother, father, links, mutation_prob, random):
        self.links = links
        self.random = random
        self.genes = []

        if len(mother.genes) != len(father.genes):
            raise Exception("Mother and father don't have the same number of genes")

        chromosome_valid = False
        while not chromosome_valid:
            for i in range(0, len(mother.genes)):
                from_mother = self.random.choice([True, False])
                if from_mother:
                    self.genes.append(mother.genes[i])
                else:
                    self.genes.append(father.genes[i])
            for gene in self.genes:
                gene.attempt_mutation()
            chromosome_valid = self.validate()

class EvolutionAlgorithm:
    def __init__(self, links, demands, seed, population_size, mutation_prob):
        self.links = links
        self.demands = demands
        self.seed = seed
        self.population_size = population_size
        self.initial_pairs = population_size / 2
        self.mutation_prob = mutation_prob

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

