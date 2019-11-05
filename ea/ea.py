import random
from pprint import pprint

#mockups, maybe will be needed, maybe not
#class Demand:
#    def __init__(self,id,start_node,end_node,paths,module_no,module_cost):


#class Path:
#    def __init__(self,node_A,node_B,):

class Link:
    def __init__(self,link_id, start_node,end_node,module_cost,no_of_modules,link_module_cap):
        self.link_id = link_id
        self.start_node = start_node
        self.end_node = end_node
        self.module_cost = module_cost
        self.no_of_modules = no_of_modules
        self.link_module_cap = link_module_cap

    def print(self):
        print("Link no: "+str(self.link_id)+" , from node: "+str(self.start_node)+
              " to node: "+str(self.end_node)+" of module cost: "+
              str(self.module_cost)+" with max module no: "+str(self.no_of_modules)+
              "and module capacity: "+str(self.link_module_cap)
              )


#class containing the structure of network (links)
#and functions associated with it.
class Network:
    def __init__(self):
        self.links = []

    def link_add(self,link):
        self.links.append(link)

    def link_print(self):
        for i in range (len(self.links)):
                self.links[i].print()

    #checks whether nodes are connected directly (without other nodes) WITH REGARD of the paths direction
    def are_nodes_connected_directly_direction_wise(self,node_A_id, node_B_id):
        for i in range (len(self.links)):
            if (self.links[i]).start_node== node_A_id:
                if (self.links[i]).end_node==node_B_id:
                    return True
        return False

    #checks whether nodes are connected directly (without other nodes) IGNORING the paths direction
    def are_nodes_connected_directly_ignoring_direction(self,node_A_id, node_B_id):
        for i in range (len(self.links)):
            if (self.links[i]).start_node== node_A_id:
                if (self.links[i]).end_node==node_B_id:
                    return True
            if (self.links[i]).start_node== node_B_id:
                if (self.links[i]).end_node==node_A_id:
                    return True
        return False


class EA_simulation:
    def __init__(self,links,demands,seed, population_size,
        crossover_prob, mutation_prob):
        self.links = links
        self.demands = demands
        self.population_size = population_size
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.network = Network()

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
            #demand_types = sorted(list(dict.fromkeys(demand_types))).copy()
            demand_types = list(dict.fromkeys(demand_types)).copy()
            for j in range (len(demand_types)):
                for i in range (len(demands)):
                    if demands[i]["type"]== demand_types[j]:
                        #pprint (demands[i])
                        pprint(1)


            for i in range (len(links)):
                pprint(links[i])
                self.network.link_add(Link( i+1,
                                        links[i]["start_node"]
                                      , links[i]["end_node"]
                                      , links[i]["module_cost"]
                                      ,links[i]["number_of_modules"]
                                      , links[i]["link_module"]
                                      ))
            self.network.link_print()
            pprint(self.network.are_nodes_connected_directly(1,2))
            pprint(self.network.are_nodes_connected_directly(1,3))
            pprint(self.network.are_nodes_connected_directly(1,4))

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


