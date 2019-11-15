import random
from pprint import pprint


class Path:
    def __init__(self,path_id,node_A,node_B, via_paths):
        self.path_id = path_id
        self.node_A = node_A
        self.node_B = node_B
        self.via_nodes = via_paths
    def print_path(self):
        print(" >Path no: "+str(self.path_id)+" from node: "+str(self.node_A)+" to node: "+str(self.node_B)+ " via paths: ", end = ' ')
        for i in range(len(self.via_nodes)):
            print(str(self.via_nodes[i])+",", end = ' ')
        #print('\b')
        #print('\b')
        print()


class Demand:
    def __init__(self,demand_id,start_node,end_node,paths,volume):
                 #current_module_count,current_module_cost):
        self.demand_id = demand_id
        self.start_node = start_node
        self.end_node = end_node
        self.paths = paths
        self.volume = volume
        #self.current_module_count = current_module_count
        #self.current_module_cost = current_module_cost

    def print_paths(self):
        for i in range (len(self.paths)):
            self.paths[i].print_path()


    def print(self):
        print("Demand no: "+str(self.demand_id)+" , from node: "+str(self.start_node)+
              " to node: "+str(self.end_node)+" of volume: "+ str(self.volume)+
              " and paths: "
              )
        self.print_paths()

class Chromosome:
    def __init__(self, demands):
        self.demands = demands
        self.matrix = dict()




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
              " and module capacity: "+str(self.link_module_cap)
              )


#class containing the structure of network (links)
#and functions associated with it.
class Network:
    def __init__(self):
        self.links = []
        self.demands = []

    def link_add(self,link):
        self.links.append(link)

    def link_print(self):
        for i in range (len(self.links)):
                self.links[i].print()

    def demand_add(self,demand):
        self.demands.append(demand)

    def demand_print(self):
        for i in range (len(self.demands)):
                self.demands[i].print()

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

#base class of simulation
class EA_simulation:
    def __init__(self,links,demands,seed, population_size,
        crossover_prob, mutation_prob):
        self.links = links
        self.demands = demands
        self.seed = seed
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

        for i in range (len(demands)):
            paths = []
            paths.clear()
            for j in range (len(demands[i]["paths"])):
                paths.append(Path(j,demands[i]["start_node"],demands[i]["end_node"],demands[i]["paths"][j]))
                #pprint(demands[i]["paths"][j])
            self.network.demand_add(Demand(demands[i]["id"], demands[i]["start_node"],demands[i]["end_node"],paths,demands[i]["demand_volume"]))
            #pprint(demands[i])


#        demand_types = []
#        for i in range (len(demands)):
            #pprint(demands[i]["type"])
#            demand_types.append(demands[i]["type"])
                #print("------------")
                #print(i)
                #print("------------\n")
                #pprint(demands[i])
                #for j in range (len(demands[i])):
                #   print(str(j)+"  =>")
                #   pprint(demands[i][j])
            #remove duplicates
        #demand_types = sorted(list(dict.fromkeys(demand_types))).copy()
#        demand_types = list(dict.fromkeys(demand_types)).copy()
#        for j in range (len(demand_types)):
#            for i in range (len(demands)):
#                if demands[i]["type"]== demand_types[j]:
#                    pprint (demands[i])
#                    pprint(1)
#                    paths = []
#                    k= 1
#                    if "demand_path_id" in demand_types[j] and ( k> len(demands) or "demand_path_id" not in demand_types[j+1] ):
#                        if demands[i]["demand_path_id"] == k:
#                            paths.append(demands[k])
#                            k = k+1
                    #else:
                        #pprint(paths)
                    #for j in range(len(demands[i].))
                    #self.network.demands.append(Demand(i,demands[i]["demand_start_node"],demands[i]["demand_end_node"],
                    #demands[i][]
                    #                                   ))


        for i in range (len(links)):
                #pprint(links[i])
                self.network.link_add(Link( i+1,
                                        links[i]["start_node"]
                                      , links[i]["end_node"]
                                      , links[i]["module_cost"]
                                      ,links[i]["number_of_modules"]
                                      , links[i]["link_module"]
                                      ))
        #for j in range (len(demands)):
            #self.network.demands.add(Demand(j,demands[j].))
        self.network.link_print()
        self.network.demand_print()
        #self.network.
        print("are unit tests completed successfully?")
        pprint(self.unit_tests_net4())




    #unit tests for file: net4
    def unit_tests_net4(self):
        return self.network.are_nodes_connected_directly_direction_wise(1,2) \
               & self.network.are_nodes_connected_directly_direction_wise(1,3) \
               & (~self.network.are_nodes_connected_directly_direction_wise(1,4)) \
               & ~self.network.are_nodes_connected_directly_direction_wise(2,1) \
               & ~self.network.are_nodes_connected_directly_direction_wise(3,1) \
               & ~self.network.are_nodes_connected_directly_direction_wise(4,1) \
               & self.network.are_nodes_connected_directly_ignoring_direction(1,2) \
               & self.network.are_nodes_connected_directly_ignoring_direction(1,3) \
               & ~self.network.are_nodes_connected_directly_ignoring_direction(1,4) \
               & self.network.are_nodes_connected_directly_ignoring_direction(2,1) \
               & self.network.are_nodes_connected_directly_ignoring_direction(3,1) \
               & ~self.network.are_nodes_connected_directly_ignoring_direction(4,1)




    #these methods may become handy when in need to change global random generator
    #https://docs.python.org/3/library/random.html#functions-for-integers
    def get_random_int_range(self,range_from,range_to):
        return self.random.randint(range_from,range_to)

    #https://docs.python.org/3/library/random.html#random.random
    def get_random_float(self):
        return self.random.random()

    #https://docs.python.org/3/library/random.html#random.sample
    def get_random_sample(self,population,k):
        return self.random.sample(population,k)

    #https://docs.python.org/3/library/random.html#random.shuffle
    def get_random_shuffle(self,x,r):
        return self.random.shuffle(x,r)


