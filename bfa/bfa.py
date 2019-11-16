import itertools

class BruteForce():
    def __init__(self, links, demands):
        self._links = links
        self._demands = demands
        self.possible_solutions = []
    
    def solve(self):
        for demand in self._demands:
            self._flows_generator(demand)
        self._solutions_generator()
        
        for i, link in enumerate(self._links):
            link["id"] = i + 1
            link["used_capacity"] = 0
        
        # assign possible flows to demands
        for solution in self.possible_solutions:
            for i in range(len(self._demands)):
#                print(solution[i], self._demands[i]["possible_flows"])
                self._demands[i]["used_paths"] = self._demands[i]["possible_flows"][solution[i]]
            self._objective_function()


    def _flows_generator(self, demand):
        volumes = list(range(demand["demand_volume"] + 1))
        paths_count = len(demand["paths"])
        # get possible flows for demand from cartesian products
        possible_flows = []
        for product in itertools.product(volumes, repeat=paths_count):
            if sum(product) == demand["demand_volume"]:
                possible_flows.append(product)
        demand["possible_flows"] = possible_flows

    def _solutions_generator(self):
        max_flows = max([len(d["possible_flows"]) for d in self._demands])
        l = list(range(max_flows))
        # get possible solutions from cartesian products
        for product in itertools.product(l, repeat=len(self._demands)):
            if all(product[i] < len(self._demands[i]["possible_flows"]) for i in range(len(self._demands))):
                self.possible_solutions.append(product)

    def _objective_function(self):
        used_links = [0 for link in self._links]
        for demand in self._demands:
            for i in range(len(demand["paths"])):
                if demand["used_paths"] != 0:
                    for link in demand["paths"][i]:
                        used_links[link - 1] = used_links[link - 1] + demand["used_paths"][i]

        link_result = []
        for i, link in enumerate(self._links):
            link_result.append(max(0, used_links[i] - (link["link_module"] * link["number_of_modules"])))
        
        for x in link_result:
            print(x)
        return max(link_result)
