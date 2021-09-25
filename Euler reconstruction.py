import math

from sympy import diff, symbols
from sympy.abc import x, y

""" Необходимо реализовать алгоритм , который восстанавливает исходную форму уравнения Эйлера, по заданным корням
характеристического уравнения . Алгоритм разделяется на следующие шаги:
1. Необходимо проанализировать корни:
1.1 Корни действительные => подставим их в формулу y = x^k , где k - корень хар.ур-ия
1.2 Корни комплексные => значит переводим их в соответствующую форму (cos/tan/sin etc)
2. Каждый n - корень, формирует n - решение, т.е
y_n(1), y_n(2) , y_n(3)
Из данных корней необходимо составить фундаментальную систему решений - ФСР
| y    y'    y''  y''' ....|
| x^k x^k' x^k'' x^k'''    |
 ..........................|
Таким образом получаем опр.Вронского, раскрытие которого приведёт к исх. ур-ию"""

matrix = []
first_row = []


def find_determinate(order, array):
    matrix = array[1::]
    new_matrix = []
    new_row = []
    result = []
    string_result = ''
    if order == 1:
        print(str(array[0][0]) + '*' + str(array[1][1]) + ' - ' + str(array[0][1]) + '*' + str(array[1][0]) + ' = 0')
        return str(array[0][0]) + '*' + str(array[1][1]) + ' - ' + str(array[0][1]) + '*' + str(array[1][0]) + ' = 0'
    if order == 2:
        for i in range(order + 1):
            for j in range(order):
                for k in range(order + 1):
                    if i == k:
                        pass
                    else:
                        new_row.append(matrix[j][k])
                new_matrix.append(new_row)
                new_row = []
            result.append(new_matrix[0][0] * new_matrix[1][1] - new_matrix[0][1] * new_matrix[1][0])
            new_matrix = []
        for i in range(len(result)):
            string_result += str(result[i]) + 'y' + "'" * i + ' '
        print(string_result)
        return string_result
    if order == 3:
        for i in range(order + 1):
            for j in range(order):
                for k in range(order + 1):
                    if i == k:
                        pass
                    else:
                        new_row.append(matrix[j][k])
                new_matrix.append(new_row)
                new_row = []
        for i in new_matrix:
            print(i)


def find_euler(order=int(input('Введите порядок уравнения: '))):
    # порядок уравнения соответствует количеству решений
    row, col = order, order
    print(row, col)
    roots = list(map(int, input('Введите характеристические корни(через пробел): ').split()))
    roots = [x ** i for i in roots]
    print(roots, ' Подстановка характеристических корней по формуле y = x^k \n\n')
    if len(roots) != order:
        print('Количество корней не соответствует порядку уравнения.\nневозможно построить ФСР')
        return find_euler(int(input('\nВведите порядок уравнения: ')))
    else:
        for i in range(order + 1):
            first_row.append('y' + "'" * i)
        matrix.append(first_row)
        for i in range(len(roots)):
            differentiated_roots = []
            root = roots[i]
            for j in range(col):
                root = diff(root)
                differentiated_roots.append(root)
                if len(differentiated_roots) == order:
                    differentiated_roots.insert(0, roots[i])
                    matrix.append(differentiated_roots)
        for i in matrix:
            print(i)
        find_determinate(order, matrix)


find_euler()
