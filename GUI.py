import PySimpleGUI as sg
import Algorithms


def NTcalculator():
    layout_main = [
        [sg.Button('Алгоритм Евклида', key='gcd')],
        [sg.Button('Расширенный алгоритм Евклида', key='egcd')],
        [sg.Button('Сравнения первой степени', key='cmp')],
        [sg.Button('Решение по Китайской теореме об остатках', key='chinese')],
        [sg.Button('Cравнение по модулю степени простого числа', key='cmp_n')],
        [sg.Button('Вычисление символа Лежандра', key='Legendre')],
        [sg.Button('Алгоритм Шенкса', key='Shenks')],
        [sg.Button('Вычисление первообразного корня по модулю', key='primitive')],
        [sg.Cancel('ВЫХОД')]
    ]
    window_main = sg.Window('Калькулятор теории чисел', layout_main)

    while True:  # The Event Loop
        event, values = window_main.read()
        if event in (None, 'ВЫХОД'):
            break

        if event == 'gcd':
            layout_gcd = [
                [sg.Text('Введите первое число: '), sg.InputText(key='first', change_submits= True,size=(10,1))],
                [sg.Text('Введите второе число: '), sg.InputText(key='second', change_submits= True,size=(10,1))],
                [sg.Text('НОД: '), sg.Output(key = '_output_')],
                [sg.Button('Посчитать', key='run'), sg.Cancel('ВЫХОД')]
            ]
            window_gcd = sg.Window('Алгоритм Евклида', layout_gcd, size=(300,150))
            while True:  # The Event Loop
                event2, values2 = window_gcd.read()
                if event2 in (None, 'ВЫХОД'):
                    window_gcd.close()
                    break
                if event2 == 'run':
                    window_gcd.FindElement('_output_').Update('')
                    if not values2['first'].isdigit() or not values2['second'].isdigit():
                        print("Неверно введены числа!")
                        continue
                    a = int(values2['first'])
                    b = int(values2['second'])
                    result = Algorithms.gcd(a, b)
                    print(result)

        if event == 'egcd':
            layout_egcd = [
                [sg.Text('Введите первое число: '), sg.InputText(key='first', change_submits= True,size=(10,1))],
                [sg.Text('Введите второе число: '), sg.InputText(key='second', change_submits= True,size=(10,1))],
                [sg.Text('РЕЗУЛЬТАТ: '), sg.Output(key= '_output_')],
                [sg.Submit('Посчитать', key='run'), sg.Cancel('ВЫХОД')]
            ]
            window_egcd = sg.Window('Расширенный алгоритм Евклида', layout_egcd,size=(370,150))
            while True:  # The Event Loop
                event3, values3 = window_egcd.read()
                if event3 in (None, 'ВЫХОД'):
                    window_egcd.close()
                    break
                if event3 == 'run':
                    window_egcd.FindElement('_output_').Update('')
                    if not values3['first'].isdigit() or not values3['second'].isdigit():
                        print("Неверно введены числа!")
                        continue
                    a = int(values3['first'])
                    b = int(values3['second'])
                    result = Algorithms.egcd_origin(a, b)
                    print(result)

        if event == 'cmp':
            layout_cmp = [
                [sg.Text('Введите первое число: '), sg.InputText(key='first', change_submits= True,size=(10,1))],
                [sg.Text('Введите второе число: '), sg.InputText(key='second', change_submits= True,size=(10,1))],
                [sg.Text('Введите модуль: '), sg.InputText(key='third', change_submits= True,size=(10,1))],
                [sg.Text('РЕЗУЛЬТАТ: '), sg.Output(key= '_output_')],
                [sg.Submit('Посчитать', key='run'), sg.Cancel('ВЫХОД')]
            ]
            window_cmp = sg.Window('Сравнение первой степени', layout_cmp,size=(340,180))
            while True:  # The Event Loop
                event4, values4 = window_cmp.read()
                if event4 in (None, 'ВЫХОД'):
                    window_cmp.close()
                    break
                if event4 == 'run':
                    window_cmp.FindElement('_output_').Update('')
                    if not values4['first'].isdigit() or not values4['second'].isdigit() or not values4['third'].isdigit():
                        print("Неверно введены числа!")
                        continue
                    a = int(values4['first'])
                    b = int(values4['second'])
                    mod = int(values4['third'])
                    result = Algorithms.compare(a, b, mod)
                    print(result)

        if event == 'chinese':
            layout_chinese = [
                [sg.Text('Число сравнений:'), sg.Combo([i for i in range(1,11)], size=(5, 1), key='count')],
                [sg.Text('x =='), sg.InputText(key='value', change_submits= True,size=(5,1)),
                sg.Text('mod'), sg.InputText(key='mod', change_submits= True,size=(5,1))],
                [sg.Text('РЕЗУЛЬТАТ: '), sg.Output(key='_output_')],
                [sg.Submit('Посчитать', key='run'), sg.Cancel('ВЫХОД')]
            ]
            window_chinese = sg.Window('Китайскай теорема об остатках', layout_chinese,size=(350,120))
            while True:  # The Event Loop
                event5, values5 = window_chinese.read()
                if event5 in (None, 'ВЫХОД'):
                    window_chinese.close()
                    break
                if event5 == 'run':
                    window_chinese.FindElement('_output_').Update('')
                    if not values5['value'].isdigit() or not values5['mod'].isdigit():
                        print("Неверно введены числа!")
                        continue
                    value, mod = [], []
                    value.append(int(values5['value']))
                    mod.append(int(values5['mod']))
                    result = Algorithms.chinese_remainder(value, mod)
                    print(result)

        if event == 'cmp_n':
            layout_cmp_n = [
                [sg.Text('Введите выражение: '), sg.InputText(key='expression', change_submits= True)],
                [sg.Text('Введите простой модуль: '), sg.InputText(key='module', change_submits= True,size=(5,1))],
                [sg.Text('Введите степень модуля: '), sg.InputText(key='degree', change_submits= True,size=(5,1))],
                [sg.Text('РЕЗУЛЬТАТ: '), sg.Output(key= '_output_')],
                [sg.Submit('Посчитать', key='run'), sg.Cancel('ВЫХОД')]
            ]
            window_cmp_n = sg.Window('Cравнение по модулю степени простого числа', layout_cmp_n,size=(450,180))
            while True:  # The Event Loop
                event6, values6 = window_cmp_n.read()
                if event6 in (None, 'ВЫХОД'):
                    window_cmp_n.close()
                    break
                if event6 == 'run':
                    window_cmp_n.FindElement('_output_').Update('')
                    if not values6['module'].isdigit() or not values6['degree'].isdigit():
                        print("Неверно введены числа!")
                        continue
                    str = values6['expression']
                    mod = int(values6['module'])
                    deg = int(values6['degree'])
                    result = Algorithms.compare_n(str, mod, deg)
                    if result == -1:
                        print("Введено неверное выражение!")
                        continue
                    if result == -2:
                        print("Модуль должен быть простым!")
                        continue
                    print(result)

        if event == 'Legendre':
            layout_Legendre = [
                [sg.Text('Введите число: '), sg.InputText(key='value', change_submits= True,size=(5,1))],
                [sg.Text('Введите модуль: '), sg.InputText(key='mod', change_submits= True,size=(5,1))],
                [sg.Text('РЕЗУЛЬТАТ: '), sg.Output(key= '_output_')],
                [sg.Submit('Посчитать', key='run'), sg.Cancel('ВЫХОД')]
            ]
            window_Legendre = sg.Window('Символ Лежандра', layout_Legendre,size=(300,150))

            while True:  # The Event Loop
                event7, values7 = window_Legendre.read()
                if event7 in (None, 'ВЫХОД'):
                    window_Legendre.close()
                    break
                if event7 == 'run':
                    window_Legendre.FindElement('_output_').Update('')
                    if not values7['value'].isdigit() or not values7['mod'].isdigit():
                        print("Неверно введены числа!")
                        continue
                    a = int(values7['value'])
                    b = int(values7['mod'])
                    result = Algorithms.calculateLegendre(a, b)
                    print(result)

        if event == 'Shenks':
            layout_Shenks = [
                [sg.Text('x^2 =='), sg.InputText(key='value', change_submits=True,size=(5,1)),
                sg.Text('mod'), sg.InputText(key='mod', change_submits=True, size=(5,1))],
                [sg.Text('РЕЗУЛЬТАТ: '), sg.Output(key='_output_')],
                [sg.Submit('Посчитать', key='run'), sg.Cancel('ВЫХОД')]
            ]
            window_Shenks = sg.Window('Алгоритм Шенкса', layout_Shenks,size=(300,120))

            while True:  # The Event Loop
                event8, values8 = window_Shenks.read()
                if event8 in (None, 'ВЫХОД'):
                    window_Shenks.close()
                    break
                if event8 == 'run':
                    window_Shenks.FindElement('_output_').Update('')
                    if not values8['first'].isdigit() or not values8['second'].isdigit():
                        print("Неверно введены числа!")
                        continue
                    a = int(values8['first'])
                    b = int(values8['second'])
                    result = Algorithms.RESSOL(a, b)
                    print(result)

        if event == 'primitive':
            layout_primitive = [
                [sg.Text('Введите число: '), sg.InputText(key='value', change_submits=True,size=(5,1))],
                [sg.Text('Введите модуль: '), sg.InputText(key='mod', change_submits=True,size=(5,1))],
                [sg.Text('РЕЗУЛЬТАТ: '), sg.Output(key='_output_')],
                [sg.Submit('Посчитать', key='run'), sg.Cancel('ВЫХОД')]
            ]
            window_primitive = sg.Window('Первообразный корень по модулю', layout_primitive,size=(380,150))

            while True:  # The Event Loop
                event9, values9 = window_primitive.read()
                if event9 in (None, 'ВЫХОД'):
                    window_primitive.close()
                    break
                if event9 == 'run':
                    window_primitive.FindElement('_output_').Update('')
                    if not values9['value'].isdigit() or not values9['mod'].isdigit():
                        print("Неверно введены числа!")
                        continue
                    a = int(values9['value'])
                    b = int(values9['mod'])
                    result = Algorithms.is_primitive_root(a, b)
                    if result == True:
                        print("{0} - первообразный корень по модулю {1}".format(a,b))
                    else:
                        print("{0} - НЕ первообразный корень по модулю {1}!".format(a,b))

NTcalculator()