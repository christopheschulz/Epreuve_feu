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

print(f"{y}.xo")
for i in range(y + 1):
    for j in range(x + 1):
        # random.randrange(y) returns an integer from 0 to y-1, similar to Ruby's rand(y)
        print("x" if random.randrange(y) * 2 < density else ".", end="")
    print()
