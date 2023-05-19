from random import randint, getrandbits

n = 6

m = [[(randint(1, 9), getrandbits(1)) for _ in range(n)] for _ in range(n)]

print("\\documentclass[tikz]{standalone}")
print("\\usepackage{logicpuzzle}")
print("\\begin{document}")
print("\\begin{center}")
print(f"\\begin{{skyline}}[rows={n}, columns={n}]")
print(f"\\skylineR{{ {', '.join(str(sum(x for x, b in row if b)) for row in m) } }}")
print(f"\\skylineB{{ {', '.join(str(sum(x for x, b in col if b)) for col in zip(*m))} }} ")
for i, row in enumerate(m):
    print(f"\\setrow{{ {i+1} }}{{ {', '.join(map(lambda x: str(x[0]), row))} }}")
print("\\end{skyline}")
print("\\end{center}")
# print("\\newpage")
# print("\\begin{center}")
# print(f"\\begin{{skyline}}[rows={n}, columns={n}]")
# print(f"\\skylineR{{ {', '.join(str(sum(x for x, b in row if b)) for row in m) } }}")
# print(f"\\skylineB{{ {', '.join(str(sum(x for x, b in col if b)) for col in zip(*m))} }} ")
# for i, row in enumerate(m):
#     print(f"\\setrow{{ {i+1} }}{{ {', '.join(str(x) if b else '{}' for x, b in row)} }}")
# print("\\end{skyline}")
# print("\\end{center}")
print("\\end{document}")
