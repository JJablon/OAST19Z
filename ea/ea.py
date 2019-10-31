import random
from pprint import pprint

class EA_simulation:
    def __init__(self,links,demands,seed, population_size,
        crossover_prob, mutation_prob):
        self.links = links
        self.demands = demands
        self.population_size = population_size
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob

        if seed != 0:
            self.random = random.Random(seed)
        else:
            self.random = random.Random()

        #for i in range (len(demands)):
            #for j in range (len(demands[i])):
                #pprint(demands[i][j])




            demand_types = []
            for i in range (len(demands)):
                #pprint(demands[i]["type"])
                demand_types.append(demands[i]["type"])
                    #print("------------")
                    #print(i)
                    #print("------------\n")
                    #pprint(demands[i])
                    #for j in range (len(demands[i])):
                      #  print(str(j)+"  =>")
                       # pprint(demands[i][j])
            #remove duplicates
            demand_types = sorted(list(dict.fromkeys(demand_types))).copy()
            for j in range (len(demand_types)):
                for i in range (len(demands)):
                    if demands[i]["type"]== demand_types[j]:
                        pprint (demands[i])






    #these methods may become handy when in need to change global random generator
    #https://docs.python.org/3/library/random.html#functions-for-integers
    def get_random_int_range(self,range_from,range_to):
        return self.random.randint(range_from,range_to)

    #https://docs.python.org/3/library/random.html#random.random
    def get_random_float(self):
        return random.random()

    #https://docs.python.org/3/library/random.html#random.sample
    def get_random_sample(self,population,k):
        return random.sample(population,k)

    #https://docs.python.org/3/library/random.html#random.shuffle
    def get_random_shuffle(self,x,r):
        return random.shuffle(x,r)


