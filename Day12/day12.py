''' Inspired by my last year graph algorithm solution
https://github.com/laojala/AoC2021/blob/main/Day15_Chiton/day15.py '''


import os
import networkx as nx


def read_input():
    #file_path = (os.path.dirname(__file__)) + "/" + 'test.txt'
    file_path = (os.path.dirname(__file__)) + "/" + 'input.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        lines = [d.rstrip() for d in file.readlines()]
    lines = [[item for item in line] for line in lines]
    return lines

def is_route(node:str, neighbour:str) -> bool:
    if ((ord(node) & 31)+ 1) >= (ord(neighbour) & 31):
        return True
    return False

def solve() -> None:
    data = read_input()

    G = nx.DiGraph()
    start = None
    end = None
    possible_start_points = []

    for x, row in enumerate(data):
        for y, node_value in enumerate(row):

            if node_value == 'a':
                possible_start_points.append((x,y))

            if node_value == 'S':
                start = (x,y)
                node_value = 'a'
                data[x][y] = 'a'
                possible_start_points.append((x,y))
                
            if node_value == 'E':
                end = (x,y)
                node_value='z'
                data[x][y] = 'z'

            # set neighbour in top
            top = x-1
            if top >= 0:
                neighbour = (top, y)
                if is_route(node_value, data[top][y]):
                    G.add_edge((x,y), neighbour)

            # set neighbour in bottom
            bottom = x+1
            if bottom <= len(data)-1:
                neighbour = (bottom, y)
                if is_route(node_value, data[bottom][y]):
                    G.add_edge((x,y), neighbour)

            # set neighbour in left
            left = y-1
            if left >= 0:
                neighbour = (x, left)
                if is_route(node_value, data[x][left]):
                    G.add_edge((x,y), neighbour)

            # set neighbour in right
            right = y+1
            if right <= len(data[0])-1:
                neighbour = (x, right)
                if is_route(node_value, data[x][right]):
                    G.add_edge((x,y), neighbour)


    part1 = nx.shortest_path_length(G, start, end) + 2
    print(part1)
    assert part1 in (31,456)

    # part2

    routes = []
    for route in possible_start_points:
        try:
            routes.append(nx.shortest_path_length(G, route, end) + 2)
        except nx.exception.NetworkXNoPath:
            pass

    part2 = min(routes)
    print(part2)
    assert part2 in (29,454)

if __name__ == '__main__':
    solve()

