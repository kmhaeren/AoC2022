

def score(l:str):
    if l == l.upper():
        return ord(l) - ord("A") + 27
    else:
        return ord(l) - ord("a") + 1

with open("day3/input.txt") as fp:
    lines = [line.strip() for line in fp.readlines()]
    compartements = [ [line[:len(line)//2], line[len(line)//2:]] for line in lines]
    compartements_2 = [ [lines[i], lines[i+1],lines[i+2]] for i in range(0, len(lines), 3)]


print(sum([ score(set(l1).intersection(set(l2)).pop()) for (l1, l2) in compartements ]))
print(sum([ score(set(l1).intersection(set(l2)).intersection(set(l3)).pop()) for (l1, l2, l3) in compartements_2 ]))



