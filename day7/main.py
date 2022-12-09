
with open("day7/input.txt") as fp:
    lines = [line.strip() for line in fp.readlines()]

for i, l in enumerate(lines):
    if l == "$ cd ..":
        lines[i] = "],"
    elif l.startswith("$ cd"):
        lines[i] = "["
    elif (t := l.split()[0]).isdigit():
        lines[i] = t+","
    else:
        lines[i] = ""
temp = "".join(lines)
file_structure = eval(temp + "]" *
                      (temp.count("[") - temp.count("]")))


def recurse_filter(s, test, i=0):
    results = [(ss, []) if type(ss) is int else recurse_filter(
        ss, test, i+1) for ss in s]
    print([x for r in results for x in r[1] if test(x)])
    return sum([r[0] for r in results]), [r[0] for r in results]+[x for r in results for x in r[1] if test(x)]


total_current_used, found1 = recurse_filter(
    file_structure, lambda x: x < 100000)
total_extra_needed = total_current_used - 40000000
total_current_used, found2 = recurse_filter(
    file_structure, lambda x: x > total_extra_needed)

print("q1:", sum(found1))
print("q2:", min(found2))
