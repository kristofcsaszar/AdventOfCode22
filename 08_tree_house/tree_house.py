import numpy as np
from collections import Counter

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    l = len(lines)
    forest = np.zeros((l, l),dtype=np.int32)
    visibility = np.zeros((l, l),dtype=np.int32)
    for i_x, row in enumerate(lines):
        for i_y, tree in enumerate(row):
            try:
                forest[i_y][i_x] = int(tree)
            except ValueError:
                # probably \n
                pass

for n in range(4):
    print(f"\n\nRound {n}")
    print(forest)
    # inspect from all 4 sides
    for x in range(l):
        row_max = 0
        for y in range(l):
            if y == 0:
                # if on the side it's visible 
                visibility[x][y] = 1
            if forest[x][y] > row_max:
                visibility[x][y] = 1
                row_max = forest[x][y]



    print("Visibility:")
    print(visibility)
    forest = np.rot90(forest)
    visibility = np.rot90(visibility)

counts = Counter(visibility.flatten())

print(f"Number of trees visible: {counts.get(1)}")