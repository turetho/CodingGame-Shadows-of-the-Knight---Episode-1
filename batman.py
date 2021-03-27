import sys
import math
import itertools

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

# game loop



x, y = x0, y0
tab = [(i,j) for i,j in itertools.product(range(w),range(h))]
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # the location of the next window Batman should jump to.
    print(bomb_dir, file=sys.stderr, flush=True)

    if bomb_dir == "DR":
        tab = [(i,j) for i,j in itertools.product(range(tab[-1][0]+1),range(tab[-1][1]+1)) if i > x and j > y]
        print(len(tab), file=sys.stderr, flush=True)
        move_to = tab[len(tab)//2]
        x = move_to[0]
        y = move_to[1]
        print(str(x) + " " + str(y))
    if bomb_dir == "D":
        tab = [(i,j) for i,j in itertools.product(range(tab[-1][0]+1),range(tab[-1][1]+1)) if i == x and j > y]
        move_to = tab[len(tab)//2]
        x = move_to[0]
        y = move_to[1]
        print(str(x) + " " + str(y))
    if bomb_dir == "U":
        tab = [(i,j) for i,j in itertools.product(range(tab[-1][0]+1),range(tab[-1][1]+1)) if i == x and j < y]
        move_to = tab[len(tab)//2]
        x = move_to[0]
        y = move_to[1]
        print(str(x) + " " + str(y))
    if bomb_dir == "UR":
        tab = [(i,j) for i,j in itertools.product(range(tab[-1][0]+1),range(tab[-1][1]+1)) if i > x and j < y]
        print(len(tab), file=sys.stderr, flush=True)
        move_to = tab[len(tab)//2]
        x = move_to[0]
        y = move_to[1]
        print(str(x) + " " + str(y))
    if bomb_dir == "UL":
        tab = [(i,j) for i,j in itertools.product(range(tab[-1][0]+1),range(tab[-1][1]+1)) if i < x and j < y]
        print(len(tab), file=sys.stderr, flush=True)
        move_to = tab[len(tab)//2]
        x = move_to[0]
        y = move_to[1]
        print(str(x) + " " + str(y))
    if bomb_dir == "DL":
        tab = [(i,j) for i,j in itertools.product(range(tab[-1][0]+1),range(tab[-1][1]+1)) if i < x and j > y]
        print(len(tab), file=sys.stderr, flush=True)
        move_to = tab[len(tab)//2]
        x = move_to[0]
        y = move_to[1]
        print(str(x) + " " + str(y))
    if bomb_dir == "L":
        tab = [(i,j) for i,j in itertools.product(range(tab[-1][0]+1),range(tab[-1][1]+1)) if i < x and j == y]
        move_to = tab[len(tab)//2]
        x = move_to[0]
        y = move_to[1]
        print(str(x) + " " + str(y))
    if bomb_dir == "R":
        tab = [(i,j) for i,j in itertools.product(range(tab[-1][0]+1),range(tab[-1][1]+1)) if i > x and j == y]
        move_to = tab[len(tab)//2]
        x = move_to[0]
        y = move_to[1]
        print(str(x) + " " + str(y))
