"""
The user provides a m*n grid

-1 means there's a blockage, stuff can't explode
-2 means the starting point of the explosion
any other number means the explosion radius of that cell

The user will provide a target explosion cell count

The goal is to find the minimum explosion radius to equal that cell count
(the testing data will always have an answer)
"""

import sys
sys.setrecursionlimit(1000000)

def boom():
    pass

height, width, target = [int(requirement) for requirement in input().split(" ")]
grid = []

for _ in range(height):
    grid.append([int(cell) for cell in input().split(" ")])

print(height, width, target)
print(grid)