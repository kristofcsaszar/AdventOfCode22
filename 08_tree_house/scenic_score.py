import numpy as np
from collections import Counter

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    l = len(lines)
    forest = np.zeros((l, l),dtype=np.int32)
    view = np.ones((l, l),dtype=np.int32)
    for i_x, row in enumerate(lines):
        for i_y, tree in enumerate(row):
            try:
                forest[i_x][i_y] = int(tree)
            except ValueError:
                # probably \n
                pass


print(forest)
# inspect from all 4 sides
for x in range(l):
    n = 0
    e = 0
    s = 0
    w = 0
    for y in range(l):
        # on the edge the product will be 0
        if (y == 0) or (y == l-1) or (x == 0) or (x == l-1):
            view[x][y] = 0
            continue

        # check each direction
        n = 0
        e = 0
        s = 0
        w = 0
        for d_y in range(y-1, -1, -1):
            if forest[x][y] >= forest[x][d_y]:
                # if tree smaller or equal, increase view distance
                n +=1
            if forest[x][y] <= forest[x][d_y]:
                # if at least same height, stop
                break
        for d_y in range(y+1,l):
            if forest[x][y] >= forest[x][d_y]:
                # if tree smaller or equal, increase view distance
                s +=1
            if forest[x][y] <= forest[x][d_y]:
                # if at least same height, stop
                break
        for d_x in range(x-1, -1, -1):
            if forest[x][y] >= forest[d_x][y]:
                # if tree smaller or equal, increase view distance
                w +=1
            if forest[x][y] <= forest[d_x][y]:
                # if at least same height, stop
                break
        for d_x in range(x+1,l):
            if forest[x][y] >= forest[d_x][y]:
                # if tree smaller or equal, increase view distance
                e +=1
            if forest[x][y] <= forest[d_x][y]:
                # if at least same height, stop
                break
        
        view[x][y] = n * e * s * w
       

print(f"Tree with the biggest scenic score is {max(view.flatten())}")