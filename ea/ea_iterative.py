# How is this gonna look like:
#
# 0. Load and parse all links
# 1. Load and parse all demands
# 2. For each demand generate set of all possible allocations (genes)
# 3. Iterate through sets of genes and pick one for each demand, composing valid chromosome
# 4. Iterate until finding enough valid chromosomes to fulfill initial population requirement
# 5. Mix parents until generation number requirement is fulfilled (remember to keep all chromosomes valid)
# 6. Save most optimised chromosome
