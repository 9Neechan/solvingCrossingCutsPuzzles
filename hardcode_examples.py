def big_example6():
    a = 800
    b = 400
    n = 6
    cuts = [[[659.232, 400], [800, 350.405]], [[446.257, 0], [800, 229.727]], [[161.97, 0], [800, 195.09]], [[627.6, 400], [0, 26.957]], [[618.207, 0], [800, 265.127]], [[48.647, 0], [0, 331.366]]]
    graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
    points = [[0, 0], [0, 400], [800, 0], [800, 400], [659.232, 400], [800, 350.405], [446.257, 0], [800, 229.727], [161.97, 0], [800, 195.09], [627.6, 400], [0, 26.957], [618.207, 0], [800, 265.127], [48.647, 0], [0, 331.366], [699.208, 164.271], [756.241, 201.309], [739.237, 176.511], [41.103, 51.388]]
    cycles = [[0, 14, 19, 11, 0, 14],
              [11, 19, 15, 11, 19],
              [19, 10, 1, 15, 19, 10],
              [14, 8, 16, 17, 13, 5, 4, 10, 19, 14, 8],
              [8, 6, 16, 8, 6],
              [6, 12, 18, 16, 6, 12],
              [12, 2, 9, 18, 12, 2],
              [18, 17, 16, 18, 17],
              [18, 9, 7, 17, 18, 9],
              [7, 13, 17, 7, 13],
              [5, 3, 4, 5, 3]]

    print("cuts", cuts)
    print("points", points)
    for el in cycles:
        print(el)

    return n, a, b, cuts, graph, points, cycles


def big_example4():
    a = 800
    b = 400
    n = 4
    cuts = [[[487.604, 400], [800, 305.415]], [[453.341, 0], [0, 263.493]], [[111.461, 400], [800, 242.173]], [[209.836, 400], [800, 347.634]]]
    graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]]
    points = [[0, 0], [0, 400], [800, 0], [800, 400], [487.604, 400], [800, 305.415], [453.341, 0], [0, 263.493], [111.461, 400], [800, 242.173], [209.836, 400], [800, 347.634], [602.753, 365.136]]
    cycles = [[0, 6, 7, 0, 6],
              [6, 2, 9, 8, 1, 7, 6, 2],
              [9, 5, 12, 10, 8, 9, 5],
              [5, 11, 12, 5, 11],
              [12, 4, 10, 12, 4],
              [11, 3, 4, 12, 11, 3]]

    print("cuts", cuts)
    print("points", points)
    for el in cycles:
        print(el)

    return n, a, b, cuts, graph, points, cycles


def big_example5():
    a = 800
    b = 400
    n = 5
    cuts = [[[274.574, 0], [800, 201.295]], [[123.337, 0], [0, 123.995]], [[210.628, 0], [800, 346.459]], [[97.871, 400], [800, 294.037]], [[550.132, 400], [0, 79.74]]]
    graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0]]
    points = [[0, 0], [0, 400], [800, 0], [800, 400], [274.574, 0], [800, 201.295], [123.337, 0], [0, 123.995], [210.628, 0], [800, 346.459], [97.871, 400], [800, 294.037], [550.132, 400], [0, 79.74], [27.877, 95.969], [729.041, 304.746], [457.025, 345.798]]
    cycles = [[0, 6, 14, 13, 0, 6],
              [13, 14, 7, 13, 14],
              [7, 14, 16, 10, 1, 7, 14],
              [6, 8, 15, 16, 14, 6, 8],
              [8, 4, 5, 11, 15, 8, 4],
              [4, 2, 5, 4, 2],
              [16, 12, 10, 16, 12],
              [15, 9, 3, 12, 16, 15, 9],
              [11, 9, 15, 11, 9]]

    print("cuts", cuts)
    print("points", points)
    for el in cycles:
        print(el)

    return n, a, b, cuts, graph, points, cycles


#######################################################################################################################
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
