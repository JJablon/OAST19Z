class Parser:
    def __init__(self):
        pass

    @classmethod
    def read_file(cls, filename):
        data = []
        with open(filename, "r", encoding="UTF-8") as f:
            lines = ''
            for line in f:
                data.append(line.rstrip())
        return data
    
    @classmethod
    def mp2k(self, data):
        links = []
        demands = []
        links_counter = None
        demands_counter = None
        is_frist = True

        for i, line in enumerate(data):
            if i == 0:
                links_counter = int(line)
                continue
            
            if line == "-1":
                continue
            
            if links_counter != 0:
                splitted_line = line.split(" ")
                links.append(self._parse_link(splitted_line))
                links_counter = links_counter - 1
                continue
            
            if links_counter == 0 and demands_counter is None and line != "":
                demands_counter = int(line) + 1
                continue
            
            if demands_counter is not None and demands_counter != 0:
                if line == "":
                    demands_counter = demands_counter - 1
                    is_first = True
                    continue
                splitted_line = line.split(" ")
                demands.append(self._parse_demand(splitted_line, is_first, demands_counter))
                is_first = False
        
        merged_demands = self._merge_demands(demands)
        return links, merged_demands

    @classmethod
    def _parse_link(cls, line):
        link = {"type": "link"}
        for i, x in enumerate(line):
            if i == 0:
                link["start_node"] = int(x)
            if i == 1:
                link["end_node"] = int(x)
            if i == 2:
                link["number_of_modules"] = int(x)
            if i == 3:
                link["module_cost"] = float(x)
            if i == 4:
                link["link_module"] = int(x)
        return link

    @classmethod
    def _parse_demand(cls, line, is_first, counter):
        demand = {"type": "demand"}
        demand["id"] = counter
        for i, x in enumerate(line):
            if is_first and len(line) == 3:
                if i == 0:
                    demand["start_node"] = int(x)
                if i == 1:
                    demand["end_node"] = int(x)
                if i == 2:
                    demand["demand_volume"] = int(x)
            elif len(line) == 1:
                demand["number_of_demand_paths"] = int(x)
            else:
                if i == 0:
                    demand["demand_path_id"] = int(x)
                    demand["link_list"] = []
                else:
                    demand["link_list"].append(int(x))

        return demand 


    @classmethod
    def _merge_demands(cls, demands):
        ids = set()
        for demand in demands:
            ids.add(demand["id"])

        
        merge_demands = []
        for i in ids:
            merge_demand = {"type": "demand", "id": i}
            for demand in demands:
                if i == demand["id"] and "start_node" in demand:
                    merge_demand["start_node"] = demand["start_node"]
                    merge_demand["end_node"] = demand["end_node"]
                    merge_demand["demand_volume"] = demand["demand_volume"]
                    merge_demand["paths"] = []
                elif i == demand["id"] and "link_list" in demand:
                     merge_demand["paths"].append(demand["link_list"])
            merge_demand.pop("id")
            merge_demands.append(merge_demand)
        return merge_demands 
