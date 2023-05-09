import random
import matplotlib.pyplot as plt
from matplotlib import image
from PIL import Image

import pieces_generation as pg
import hardcode_examples as he

pairs = []
true_pairs = []


def compare(piece1, np1, piece2, np2):
    """записывает пары сторон в массивы"""
    n = 0
    for s1 in range(len(piece1.sides)):
        for s2 in range(len(piece2.sides)):
            if piece1.sides[s1].len == piece2.sides[s2].len:
                print(piece1.sides[s1].len, piece2.sides[s2].len)
                if round(piece1.sides[s1].angles[0]+piece2.sides[s2].angles[1]) == 180 and \
                   round(piece1.sides[s1].angles[1]+piece2.sides[s2].angles[0]) == 180 and \
                   [[piece1, s1], [piece2, s2]] not in pairs:
                    pairs.append([[np1, s1], [np2, s2]])
                    n += 1
    if n == 1:
        p = pairs[len(pairs)-1]
        pairs.remove(p)
        if p not in true_pairs:
            true_pairs.append(p)


def draw_solution(cuts, a, b, cycles, points):
    """Отрисоввает изображения исхдной фигуры с разрезами и итерации решения головоломки"""

    # рандомно выбираем фреску
    random_img = random.randint(0, 3)
    img = image.imread(f"frescoes/{random_img}.jpg")

    # рисуем исходную фигуру с разрезами
    snapshot_name = "pictures/initial.png"
    x = [0, 0, a, a, 0]
    y = [0, b, b, 0, 0]
    plt.imshow(img)
    #plt.figure(figsize=(a, b))
    #for xy in zip(x, y):
        #plt.annotate('(%.2f, %.2f)' % xy, xy=xy)

    plt.title('Сгенерированный пазл')
    plt.plot(x, y, 'white', alpha=1, lw=4, mec='g', mew=2, ms=5)
    for i in range(len(cuts)):
        x = [cuts[i][0][0], cuts[i][1][0]]
        y = [cuts[i][0][1], cuts[i][1][1]]
        plt.plot(x, y, 'white', alpha=1, lw=1.5, mec='g', mew=2, ms=5)
        #for xy in zip(x, y):
            #plt.annotate('(%.2f, %.2f)' % xy, xy=xy)
    plt.axis("off")
    plt.savefig(snapshot_name, dpi=95, bbox_inches='tight')
    plt.close()

    # рисуем фрагменты, прибавленные на каждой итерации алгоритма
    x = []
    y = []
    drawed_pieces = []
    for p in range(len(true_pairs)):
        snapshot_name = f"pictures/{p}.png"
        plt.title(f'Номер итерации: {p}')
        #plt.figure(figsize=(a, b))
        #plt.plot([0, a], [0, b], 'white', alpha=1, lw=5, mec='g', mew=2, ms=5)
        plt.imshow(img)

        # фрагменты, соединяющиеся на данной операции
        iter_cycles = [cycles[true_pairs[p][0][0]], cycles[true_pairs[p][1][0]]]
        # добавляем отрисовку границ этих фрагментов
        for c in iter_cycles:
            if c not in drawed_pieces:
                drawed_pieces.append(c)
                new_p_x = []
                new_p_y = []
                for j in range(len(c) - 1):
                    new_p_x.append(points[c[j]][0])
                    new_p_y.append(points[c[j]][1])
                x.append(new_p_x)
                y.append(new_p_y)
        # отрисовываем все фрагменты, добавленные к текущей итерации
        for k in range(len(x)):
            plt.plot(x[k], y[k], 'black', alpha=1, lw=1.5, mec='g', mew=2, ms=5)

        # подсвечиваем стороны фрагментов, которые алгоритм соединил на текущей итерации
        s = true_pairs[p][0][1]
        if s == 0:
            s = len(iter_cycles[0]-1)
        color_x = [points[iter_cycles[0][s-1]][0], points[iter_cycles[0][s]][0]]
        color_y = [points[iter_cycles[0][s-1]][1], points[iter_cycles[0][s]][1]]
        plt.plot(color_x, color_y, 'red', alpha=1, lw=2.5, mec='g', mew=2, ms=5)

        plt.axis("off")
        plt.savefig(snapshot_name, dpi=95, bbox_inches='tight')
        plt.close()


def noNoiseAlgorithm(num_cuts, a, b):
    '''
    # генерируем кусочки
    pieces, cuts, pieces_in_points = pg.get_pieces(num_cuts, a, b)
    '''

    n, a, b, cuts, graph, points, cycles = he.big_example2()
    pieces = pg.get_pieces(cycles, points)

    print("все кусочки")
    for pis in pieces:
        print('new piece')
        for s in pis.sides:
            print(s.len, s.angles)
        print()

    # ищем ребра фрагментов, которые должны быть соединены
    print("все длины сторон, которые были соединены")
    for i in range(len(pieces)):
        for j in range(i+1, len(pieces)):
            if i != j:
                compare(pieces[i], i, pieces[j], j)
    '''
    for i in range(len(tru_pairs)):
        for j in range(i+1, len(tru_pairs)):
            four = [tru_pairs[i], 0, 0]
            four[2] = tru_pairs[j]
            if tru_pairs[i][0][0] != tru_pairs[j][0][0] and \
               tru_pairs[i][0][0] != tru_pairs[j][1][0] and \
               tru_pairs[i][1][0] != tru_pairs[j][0][0] and \
               tru_pairs[i][1][0] != tru_pairs[j][1][0]:

                
                for el in pairs:
                    if (tru_pairs[i][0][0] == el[0][0] and (el[1][0] == tru_pairs[j][0][0] or el[1][0] == tru_pairs[j][1][0]) and el[0][1] == )  or \
                       (tru_pairs[i][0][0] == el[1][0] and (el[0][0] == tru_pairs[j][0][0] or el[0][0] == tru_pairs[j][1][0])): # ищу с кем смержить кусочки из противоположного мержа
                        lenp_i = pieces[tru_pairs[i][0][0]].sides_amount
                        lenp_j = pieces[tru_pairs[j][0][0]].sides_amount
                        if 

                    if (tru_pairs[i][1][0] == el[0][0] and (el[1][0] == tru_pairs[j][0][0] or el[1][0] == tru_pairs[j][1][0])) or \
                       (tru_pairs[i][1][0] == el[1][0] and (el[0][0] == tru_pairs[j][0][0] or el[0][0] == tru_pairs[j][1][0])):
            
            if len(four) == 4 and four[1] != 0:
                pairs.remove(four[1])
                pairs.remove(four[3])
                for elem in four:
                    if elem not in sol:
                        sol.append(elem)
                        '''

    #print(pairs)
    #print('=====')
    print()
    print("стороны фрагментов, которые надо соединить [номер фрагмента, номер стороны этого фрагмента]")
    print(true_pairs)

    draw_solution(cuts, a, b, cycles, points)
    return len(cycles)