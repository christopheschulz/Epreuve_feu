import sys
import random

# In Python, sys.argv[0] is the script name.
# We expect 4 arguments: height, width, characters, and gates.
if len(sys.argv) < 4 or len(sys.argv[3]) < 5:
    print("params needed: height width characters")
else:
    height = int(sys.argv[1])
    width = int(sys.argv[2])
    chars = sys.argv[3]
    #gates = int(sys.argv[4])  # Although 'gates' is not used later

    # Choose random positions for entry points.
    # This mimics Ruby's rand(width - 4) + 2, which gives a value in the range [2, width-3]
    entry = random.randint(2, width - 3)
    entry2 = random.randint(2, width - 3)

    with open('exemple.map', 'w') as f:
        f.write(f"{height}x{width}{chars}\n")
        for y in range(height):
            for x in range(width):
                if y == 0 and x == entry:
                    f.write(chars[3])
                elif y == height - 1 and x == entry2:
                    f.write(chars[4])
                elif 1 <= y <= height - 2 and 1 <= x <= width - 2 and random.randint(0, 99) > 20:
                    f.write(chars[1])
                else:
                    f.write(chars[0])
            f.write("\n")
