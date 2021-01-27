#!env python
f = open("/home/davecore/adventofcode/3.data", "r")
lines = f.read().splitlines()


total = 1
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

for slope in slopes:
    row = 0
    col = 0
    trees = 0
    while row <= len(lines) - 1:
        col = col % len(lines[0])
        if lines[row][col] == "#":
            trees += 1
        row = row + slope[1]
        col = col + slope[0]
    total *= trees

print("total: ", total)
