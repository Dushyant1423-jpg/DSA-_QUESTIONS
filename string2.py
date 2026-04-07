'''Given a route containing 4 directions(E,W,N,S), find the shortest path to reach destination ?"WNEENESENNN"'''
import math

def shortest_path(route):
    x = 0
    y = 0

    for direction in route:
        if direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1
        elif direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1

    return math.sqrt(x**2 + y**2)


print(shortest_path("WNEENESENNN"))