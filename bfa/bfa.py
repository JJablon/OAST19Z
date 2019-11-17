import itertools
import math

class BruteForce():
    def __init__(self, links, demands):
        self._links = links
        for i, link in enumerate(self._links):
            link["id"] = i + 1
            link["used_capacity"] = 0
        self._demands = demands
        self.possible_solutions = []
        self.solutions = []
        self._init_debug_files()     
    
    def solve(self):
        print("Bruteforce started!")
        for demand in self._demands:
            self._flows_generator(demand)
        self._solutions_generator()
        self._play()
        print("Number of solutions: {}".format(len(self.solutions)))
        best_solution = min(self.solutions, key=lambda x:x["cost"])
        print("Best solution: {}".format(best_solution))
        self._save_best_solution(best_solution)
        print("Bruteforce ended!")

    def _flows_generator(self, demand):
        volumes = list(range(demand["demand_volume"] + 1))
        paths_count = len(demand["paths"])
        self._debug_fg(demand, volumes, paths_count)
        # get possible flows for demand from cartesian products
        possible_flows = []
        i = 0
        for product in itertools.product(volumes, repeat=paths_count):
            if sum(product) == demand["demand_volume"]:
                self._debug_fg_loop(product, i)
                i = i + 1
                possible_flows.append(product)
        demand["possible_flows"] = possible_flows

    def _solutions_generator(self):
        max_flows = max([len(d["possible_flows"]) for d in self._demands])
        l = list(range(max_flows))
        # self._debug_sg(max_flows)
        # get possible solutions from cartesian products
        for product in itertools.product(l, repeat=len(self._demands)):
            # check if product dont contain higher index of possible_flow than it could be
            if all(product[i] < len(self._demands[i]["possible_flows"]) for i in range(len(self._demands))):
                # self._debug_sg_loop(product)
                self.possible_solutions.append(product)

    def _play(self):
        for solution in self.possible_solutions:
            for i in range(len(self._demands)):
                self._demands[i]["used_paths"] = self._demands[i]["possible_flows"][solution[i]]
                # self._debug_as(self._demands[i], self._demands[i]["used_paths"])
            self._objective_function(solution)

    def _objective_function(self, flows):
        used_links = [0 for link in self._links]
        # calculate used capacity on links
        for demand in self._demands:
            for i in range(len(demand["paths"])):
                if demand["used_paths"][i] != 0:
                    for link in demand["paths"][i]:
                        used_links[link - 1] = used_links[link - 1] + demand["used_paths"][i]
        
        # check if link has enough capacity and calculate solution cost
        cost = 0
        link_result = []
        for i, link in enumerate(self._links):
            link_result.append(max(0, used_links[i] - (link["link_module"] * link["number_of_modules"])))
            cost = cost + math.ceil(used_links[i] / link["link_module"]) * link["module_cost"]

        # if solution is good, save it
        if max(0, max(link_result)) == 0:
            solution = {"flows": flows}
            for i, link in enumerate(used_links): 
                solution["link #{}".format(str(i + 1))] = link
            solution["cost"] = cost

            self.solutions.append(solution)

    def _init_debug_files(self):
        with open("bfa/flows_generator.debug", "w", encoding="UTF-8") as f:
            f.write("")
        # with open("bfa/solutions_generator.debug", "w", encoding="UTF-8") as f:
        #     f.write("")
        # with open("bfa/play.debug", "w", encoding="UTF-8") as f:
        #     f.write("")
        with open("bfa/solutions", "w", encoding="UTF-8") as f:
            f.write("")
        with open("bfa/best_solution", "w", encoding="UTF-8") as f:
            f.write("")

    def _debug_fg(self, demand, volumes, paths_count):
        with open("bfa/flows_generator.debug", "a", encoding="UTF-8") as f:
            f.write("------------------------------------\n")
            f.write("demand: {} \n".format(demand))
            f.write("demand_volumes: {}\n".format(volumes))
            f.write("number of paths: {}\n".format(paths_count))
            f.write("------------------------------------\n")

    def _debug_fg_loop(self, product, i):
        with open("bfa/flows_generator.debug", "a", encoding="UTF-8") as f:
            f.write("{} product: {}\n".format(i, product))
    
    def _debug_sg(self, max_flows):
        with open("bfa/solutions_generator.debug", "a", encoding="UTF-8") as f:
            f.write("------------------------------------\n")
            f.write("max_flows: {} \n".format(max_flows))
            f.write("------------------------------------\n")

    def _debug_sg_loop(self, product):
        with open("bfa/solutions_generator.debug", "a", encoding="UTF-8") as f:
            f.write("product: {}\n".format(product))

    def _debug_as(self, demand, assigned_solution):
        with open("bfa/play.debug", "a", encoding="UTF-8") as f:
            f.write("------------------------------------\n")
            f.write("demand: {}\n".format(demand))
            f.write("assigned solution: {}\n".format(assigned_solution))
            f.write("------------------------------------\n")

    def _save_solutions(self, solution):
        with open("bfa/solutions", "a", encoding="UTF-8") as f:
            f.write("solution: {}\n".format(solution))
    
    def _save_best_solution(self, solution):
        with open("bfa/best_solution", "a", encoding="UTF-8") as f:
            f.write("solution: {}\n".format(solution))
