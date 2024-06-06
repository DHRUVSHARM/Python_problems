import heapq


def foo(wins, draws, scored, conceded):
    points, h = [], []
    for index in range(0, len(wins)):
        point = 3 * wins[index] + draws[index]
        gd = scored[index] - conceded[index]
        h.append((-1 * point, -1 * gd, index))

    heapq.heapify(h)
    first = heapq.heappop(h)
    second = heapq.heappop(h)

    return [first[2], second[2]]
