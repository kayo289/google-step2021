#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def greedy(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour

def opt_2(path, cities):
    size = len(path)
    while True:
        count = 0
        for i in range(size-2):
            i1 = i + 1
            for j in range(i+2, size):
                if j == size - 1:
                    j1 = 0
                else:
                    j1 = j + 1
                if i != 0 or j1 != 0:
                    l1 = distance(cities[path[i]], cities[path[i1]])
                    l2 = distance(cities[path[j]], cities[path[j1]])
                    l3 = distance(cities[path[i]], cities[path[j]])
                    l4 = distance(cities[path[i1]], cities[path[j1]])
                    if l1 + l2 > l3 + l4:
                        new_path = path[i1:j+1]
                        path[i1:j+1] = new_path[::-1]
                        count += 1
        if count == 0:
            break
    return path

if __name__ == '__main__':
    assert len(sys.argv) > 1
    cities = read_input(sys.argv[1])
    # print(cities)
    tour = greedy(cities)
    print("==greedy==")
    print(tour)
    tour = opt_2(tour, cities)
    print("==opt2==")
    print_tour(tour)
