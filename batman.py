import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

# game loop

x, y = x0, y0
l, r, t ,b = 0, w - 1, 0, h - 1
#tab = [(i,j) for i,j in itertools.product(range(w),range(h))]
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # the location of the next window Batman should jump to.

    if bomb_dir == "DR":
        l = x + 1
        t = y + 1
        x = (l + r) // 2
        y = (t + b) // 2
        print(str(x) + " " + str(y))
    if bomb_dir == "D":
        t = y + 1
        y = (t + b) // 2
        print(str(x) + " " + str(y))
    if bomb_dir == "U":
        b = y - 1
        y = (t + b) // 2
        print(str(x) + " " + str(y))
    if bomb_dir == "UR":
        b = y - 1
        l = x + 1
        x = (l + r) // 2
        y = (t + b) // 2
        print(str(x) + " " + str(y))
    if bomb_dir == "UL":
        b = y - 1
        r = x - 1
        x = (l + r) // 2
        y = (t + b) // 2
        print(str(x) + " " + str(y))
    if bomb_dir == "DL":
        t = y + 1
        r = x - 1
        x = (l + r) // 2
        y = (t + b) // 2
        print(str(x) + " " + str(y))
    if bomb_dir == "L":
        r = x - 1
        x = (l + r) // 2
        print(str(x) + " " + str(y))
    if bomb_dir == "R":
        l = x + 1
        x = (l + r) // 2
        print(str(x) + " " + str(y))
