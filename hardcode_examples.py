def example1():
    a = 10
    b = 5
    n = 3
    cuts = [[[0.944, 5], [0, 2.011]], [[6.817, 0], [0, 3.454]], [[5.917, 5], [10, 1.852]]]
    graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]]
    points = [[0, 0], [0, 5], [10, 0], [10, 5], [0.944, 5], [0, 2.011], [6.817, 0], [0, 3.454], [5.917, 5], [10, 1.852], [0.393, 3.255]]
    cycles = [[1, 4, 10, 7, 1, 4],
              [7, 10, 5, 7, 10],
              [5, 10, 6, 0, 5, 10],
              [4, 8, 9, 2, 6, 10, 4, 8],
              [8, 3, 9, 8, 3]]
    return n, a, b, cuts, graph, points, cycles


def example2():
    a = 10
    b = 5
    n = 4
    cuts = [[[5.763, 0], [10, 2.223]], [[2.73, 5], [10, 2.799]], [[7.004, 0], [10, 3.284]], [[2.227, 0], [0, 0.932]]]
    graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0]]
    points = [[0, 0], [0, 5], [10, 0], [10, 5], [5.763, 0], [10, 2.223], [2.73, 5], [10, 2.799], [7.004, 0], [10, 3.284], [2.227, 0], [0, 0.932], [8.143, 1.249], [9.653, 2.904]]
    cycles = [[1, 6, 13, 12, 4, 10, 11, 1, 6],
              [11, 10, 0, 11, 10],
              [6, 3, 9, 13, 6, 3],
              [9, 7, 13, 9, 7],
              [13, 7, 5, 12, 13, 7],
              [12, 8, 4, 12, 8],
              [5, 2, 8, 12, 5, 2]]
    return n, a, b, cuts, graph, points, cycles


def example3():
    a = 10
    b = 5
    n = 5
    cuts = [[[4.433, 5], [10, 2.097]], [[6.242, 0], [0, 1.435]], [[7.582, 0], [10, 1.433]], [[3.294, 5], [0, 1.604]], [[3.796, 5], [10, 2.713]]]
    graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]
    points = [[0, 0], [0, 5], [10, 0], [10, 5], [4.433, 5], [10, 2.097], [6.242, 0], [0, 1.435], [7.582, 0], [10, 1.433], [3.294, 5], [0, 1.604], [3.796, 5], [10, 2.713], [5.969, 4.199]]
    cycles = [[1, 10, 11, 1, 10],
              [10, 12, 14, 5, 9, 8, 6, 7, 11, 10, 12],
              [7, 6, 0, 7, 6],
              [12, 4, 14, 12, 4],
              [4, 3, 13, 14, 4, 3],
              [13, 5, 14, 13, 5],
              [9, 2, 8, 9, 2]]
    return n, a, b, cuts, graph, points, cycles