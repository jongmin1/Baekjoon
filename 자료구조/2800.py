from itertools import combinations
import sys
input = sys.stdin.readline

expr = list(input().strip())
indices = []
stack = []
answers = set()

for i in range(len(expr)):
    if expr[i] == '(':
        stack.append(i)
    elif expr[i] == ')':
        indices.append((stack.pop(), i))

print(indices)
print()
for i in range(len(indices)):
    # print(combinations(indices, i+1))
    for comb in combinations(indices, i+1):
        print(i, comb)
        t = expr[:]
        for idx in comb:
            t[idx[0]] = t[idx[1]] = ""
        answers.add("".join(t))
            

# for item in sorted(list(answers)):
#     print(item)
