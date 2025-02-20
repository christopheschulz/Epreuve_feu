# You can run this script from the command line, 
# passing three arguments for x, y, and density.


import sys
import random

if len(sys.argv) != 4:
    print("params needed: x y density")
    sys.exit()

x = int(sys.argv[1])
y = int(sys.argv[2])
density = int(sys.argv[3])

with open('tableau.txt', 'w') as f:
    f.write(f"{y}.xo\n")
    for i in range(y + 1):
        for j in range(x + 1):
            # random.randrange(y) renvoie un entier entre 0 et y-1
            f.write("x" if random.randrange(y) * 2 < density else ".")
        f.write("\n")