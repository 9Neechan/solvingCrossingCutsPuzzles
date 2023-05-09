import random
import math

'''
a = 3
b = 6
n = 3
'''

MAXN = 1005
vis = [False for i in range(MAXN)]
start_node = 0
all_cycles = [[]]
aa = 0
bb = 0


class Side:
    def __init__(self, len, angles): #colors_amount, colors,
        #self.colors_amount = colors_amount
        #self.colors = colors # цвета слева на право [color, pix start]
        self.len = len
        self.angles = angles # (l_ang, r_ang) смотрим на сторону с внешней стороны фрагмента


class Piece:
    def __init__(self, sides):
        self.sides = sides
        self.sides_amount = len(sides)


def generate_cuts(num_cuts, a, b):
    """Генерирует разрезы"""
    cuts = []
    choise_x = [a, 0]
    choise_y = [b, 0]
    for i in range(num_cuts):
        cut = []
        # точка на оси х
        ch = random.randint(0, 1)
        x = round(random.uniform(0.9, a - 0.9), 3)
        y = choise_y[ch]
        cut.append([x, y])

        # точка на оси y
        ch = random.randint(0, 1)
        x = choise_x[ch]
        y = round(random.uniform(0.9, b-0.9), 3)
        cut.append([x, y])
        cuts.append(cut)
    return cuts


def line_intersection(line1, line2, a, b):
    """Проверяет пересекаются ли разрезы и находит координаты их пересечения"""
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return False
    else:
        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
    if x < 0 or y < 0 or x > a or y > b:
        return False
    return [round(x, 3), round(y, 3)]


def get_graph_matrix(cuts, a, b):
    """Находит количество пересечений всех разрезов, их координаты,
       Заполняет матрицу смежности графа разрезов"""
    points = [[0, 0], [0, b], [a, 0], [a, b]]
    lines = [[] for _ in range(len(cuts) + 2)]
    m = [[], []]
    intersect = []
    k = 0

    # добавляем все точки в массив points
    for i in range(len(cuts)):
        points.append(cuts[i][0])
        points.append(cuts[i][1])

    # записываем точки, содержащиеся в каждом разрезе в массив lines
    for i in range(len(cuts)):
        for j in range(i + 1, len(cuts)):
            p = line_intersection(cuts[i], cuts[j], a, b)
            if p != False:
                points.append(p)
                intersect.append(p)
                k = k + 1
                lines[i].append(p)
                lines[j].append(p)
        lines[i].append(cuts[i][0])
        lines[i].append(cuts[i][1])

    graph_size = 4 + k + len(cuts) * 2
    graph = [[0 for _ in range(graph_size)] for arr in range(graph_size)]

    for i in range(len(points)):
        if points[i][1] == b:
            m[0].append([points[i][0], points[i][1]])
        if points[i][1] == 0:
            m[1].append([points[i][0], points[i][1]])
        if points[i][0] == a:
            lines[len(cuts)].append([points[i][0], points[i][1]])
        if points[i][0] == 0:
            lines[len(cuts) + 1].append([points[i][0], points[i][1]])

    # сортируем точки на разрезах по определенной координате
    for i in range(len(m)):
        sorted(m[i], key=lambda x: x[0])

    for i in range(len(lines)):
        sorted(lines[i], key=lambda x: x[1])

    # формируем матрицу смежности
    for i in range(len(m)):
        for j in range(1, len(m[i])):
            graph[points.index(m[i][j - 1])][points.index(m[i][j])] = 1
            graph[points.index(m[i][j])][points.index(m[i][j - 1])] = 1

    for i in range(len(lines)):
        for j in range(1, len(lines[i])):
            graph[points.index(lines[i][j - 1])][points.index(lines[i][j])] = 1
            graph[points.index(lines[i][j])][points.index(lines[i][j - 1])] = 1

    return k, intersect, graph, points


def graph_as_a_list_of_lists(graph):
    """Для каждой вершины составляет список ее смежных вершин"""
    graph_size = len(graph)
    graph_as_a_list_of_lists = [[] for i in range(graph_size)]
    for i in range(graph_size):
        for j in range(graph_size):
            if graph[i][j] == 1:
                graph_as_a_list_of_lists[i].append(j)
    print(graph_as_a_list_of_lists)
    return graph_as_a_list_of_lists

'''
def detect_cycle(node, par, graph_as_a_list_of_lists):
    global aa, bb
    vis[node] = True
    for child in graph_as_a_list_of_lists[node]:
        if vis[child] == False:
            if detect_cycle(child, node, graph_as_a_list_of_lists):
                return True
        elif child != par:
            aa = child
            bb = node
            return True
    return False


def find_simple_cycle(a, b, graph_as_a_list_of_lists):
    simple_cycle = []
    par = [0 for i in range(MAXN)]
    q = [a]
    ok = True
    while len(q) != 0:
        node = q[0]
        q.pop(0)
        vis[node] = True
        for child in graph_as_a_list_of_lists[node]:
            if node == a and child == b:
                continue
            if not vis[child]:
                par[child] = node
                if child == b:
                    ok = False
                    break
                q.append(child)
                vis[child] = True
        if not ok:
            break
    simple_cycle.append(a)
    x = b
    while x != a:
        simple_cycle.append(x)
        x = par[x]
    return simple_cycle


def get_all_cycles(graph, graph_as_a_list_of_lists):
    """Находит вершины, образующие выпуклые кусочки"""
    global aa, bb
    graph_size = len(graph)
    cycles = []
    vis = [False for i in range(graph_size)]
    for i in range(graph_size):
        if detect_cycle(i, -1, graph_as_a_list_of_lists):
            simple_cycle = []
            for j in range(graph_size):
                vis[j] = False
            find_simple_cycle(aa, bb, graph_as_a_list_of_lists)
            if simple_cycle not in cycles:
                cycles.append(simple_cycle)
    return cycles
'''


def len_between_two_points(n1, n2, points):
    """Ищет расстояние между двумя точками"""
    p1, p2 = points[n1], points[n2]
    return round(math.sqrt(math.pow(p2[0]-p1[0], 2) + math.pow(p2[1]-p1[1], 2)), 3)


def angle_between_points(n1, n2, n3, points):
    """Ищет угол между двумя прямыми"""
    p1, p2, p3 = points[n1], points[n2], points[n3]
    ang = (math.atan2(p3[1]-p1[1], p3[0]-p1[0]) - math.atan2(p2[1]-p1[1], p2[0]-p1[0]))
    return round(ang*180/math.pi, 3)


def angle_between_two_lines(n1, n2, n3, n4, points):
    """Ищет угол между двумя прямыми"""
    p1, p2, p3, p4 = points[n1], points[n2], points[n3], points[n4]
    cos_fi = ((p2[0]-p1[0])*(p4[0]-p3[0]) + (p2[1]-p1[1])*(p4[1]-p3[1])) / \
             (len_between_two_points(n1, n2, points) * len_between_two_points(n3, n4, points))
    return round(math.acos(cos_fi)*180/math.pi, 3)


def write_pieces_into_classes(cycles, points):  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!
    """Формирует классы кусочков из наборов точек, принадлежщих им"""
    pieces_as_objects = []
    for el in cycles:
        last = len(el)-2
        le = len_between_two_points(el[last-1], el[last], points)  # !!
        an = angle_between_two_lines(el[last-2], el[last-1], el[last-1], el[last], points)
        #an = angle_between_points(el[last-2], el[last-1], el[last], points)
        sides = [Side(le, [an, -1])]
        #sides = [Side(le, [90, 90])]  # !!
        flag = 0
        for i in range(1, last):
            leng = len_between_two_points(el[i], el[i-1], points)  # !!
            if flag == 0:
                l_ang = angle_between_two_lines(el[last-1], el[i - 1], el[i - 1], el[i], points)
                flag = 1
            else:
                l_ang = angle_between_two_lines(el[i-2], el[i-1], el[i-1], el[i], points)
            #l_ang = angle_between_points(el[i - 1], el[i], el[i + 1], points)
            #sides.append(Side(leng, [90, 90])) # !!
            sides.append(Side(leng, [l_ang, -1]))
            sides[i-1].angles[1] = l_ang
        sides[len(sides)-1].angles[1] = an

        pieces_as_objects.append(Piece(sides))
    return pieces_as_objects


def get_pieces(cycles, points): #n, a, b):
    """Возвращает массив объектов класса Piece
       Вызывается из noNoiseSolution.py"""

    '''
        # генерируем разрезы
        cuts = generate_cuts(n, a, b)
        print(cuts)

        # строим граф-матрицу смежности, массив всех точек
        k, intersection_points, graph, points = get_graph_matrix(cuts, a, b)
        print(points)
        print(graph)
        #for el in graph:
            #print(el)

        # для каждой вершины ищем с какими другими вершинами она соединена
        graph_as_list_of_lists = graph_as_a_list_of_lists(graph)
        # ищем массивы точек, образующих выпуклые кусочки
        cycles = get_all_cycles(graph, graph_as_list_of_lists)


        # записываем кусочки как объекты класса Piece
        pieces_as_obj = write_pieces_into_classes(cycles, points)

        print(cycles)

        return pieces_as_obj, cuts, cycles
        '''

    pieces_as_objects = write_pieces_into_classes(cycles, points)
    return pieces_as_objects