
from utils import read_lines

lines = read_lines("day1/input.txt")

packages = []

current_package = []
for line in lines:
    if line != "":
        current_package.append(int(line))
    else:
        packages.append(sum(current_package))
        current_package = []



print(sum(sorted(packages, reverse=True)[:3]))
    
