import PySimpleGUI as psg
import noNoiseSolution


psg.theme('SandyBeach')

#[[psg.Text('Введите размер головоломки x*y', font='Default 12'), psg.InputText(key='a', justification='r'), psg.InputText(key='b', justification='r')]] + \
#[[psg.Text('Введите количество разрезов', font='Default 12'), psg.InputText(key='num_cuts', justification='r')]] + \
#[[psg.Button('Собрать')]] + \

layout = [[psg.Text('Выберите количество разрезов', font='Default 12')]] + \
         [[psg.Button('4 разреза'), psg.Button('5 разрезов'), psg.Button('6 разрезов')]] + \
         [[psg.Image('pictures/initial.png', key='init_img', visible=False, size=(10, 10))]] + \
         [[psg.Image('pictures/0.png', key='i_img', visible=False, size=(10, 10))]] + \
         [[psg.Button('Назад', visible=False, key='back_but'), psg.Button('Далее', visible=False, key='next_but')]]

n = 0
max_n = 0
data = 0
example = 4

window = psg.Window('crossingCutsPuzzles', layout, size=(800, 650), default_element_size=(8, 1), element_padding=(1, 1), return_keyboard_events=True)
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break

    if event == '4 разреза':
        # запускаем алгоритм
        n = 0
        example = 4
        data = noNoiseSolution.noNoiseAlgorithm(example)
        max_n = data - 1

        # отображаем результаты
        window['init_img'].update('pictures/initial.png', visible=True)
        window['i_img'].update('pictures/0.png', visible=True)
        if max_n > 0:
            window['back_but'].update(visible=True, disabled=True)
            window['next_but'].update(visible=True, disabled=False)

    if event == '5 разрезов':
        # запускаем алгоритм
        n = 0
        example = 5
        data = noNoiseSolution.noNoiseAlgorithm(example)
        max_n = data - 1

        # отображаем результаты
        window['init_img'].update('pictures/initial.png', visible=True)
        window['i_img'].update('pictures/0.png', visible=True)
        if max_n > 0:
            window['back_but'].update(visible=True, disabled=True)
            window['next_but'].update(visible=True, disabled=False)

    if event == '6 разрезов':
        # запускаем алгоритм
        n = 0
        example = 6
        data = noNoiseSolution.noNoiseAlgorithm(example)
        max_n = data - 1

        # отображаем результаты
        window['init_img'].update('pictures/initial.png', visible=True)
        window['i_img'].update('pictures/0.png', visible=True)
        if max_n > 0:
            window['back_but'].update(visible=True, disabled=True)
            window['next_but'].update(visible=True, disabled=False)

    # логика кнопки "Назад"
    if event == 'back_but':
        print("pic n", n)
        n -= 1
        window['i_img'].update(f'pictures/{n}.png')
        window['next_but'].update(disabled=False)
        if n == 0:
            window['back_but'].update(disabled=True)

    # логика кнопки "Далее"
    if event == 'next_but':
        print("pic n", n)
        n += 1
        window['i_img'].update(f'pictures/{n}.png')
        window['back_but'].update(disabled=False)
        if n == max_n:
            window['next_but'].update(disabled=True)

window.close()