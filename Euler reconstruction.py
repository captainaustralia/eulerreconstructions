import math

from sympy import diff, symbols, det, Matrix
from sympy.abc import x, y, d
import numpy

a = {str(i): symbols("y" + "'" * i) for i in range(50)}

funcs = {str(i): "y" + "'" * i for i in range(20)}
matrix = []
first_row = []

def find_determinate(order, array):
    matrix = array[1::]
    new_matrix = []
    new_row = []
    result = []
    string_result = ''
    if order == 1:  # matrix 2 order
        print(str(array[0][0]) + '*' + str(array[1][1]) + ' - ' + str(array[0][1]) + '*' + str(array[1][0]) + ' = 0')
        return str(array[0][0]) + '*' + str(array[1][1]) + ' - ' + str(array[0][1]) + '*' + str(array[1][0]) + ' = 0'
    if order == 2:  # matrix 3 order _| method with minors
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
            if i % 2 == 0 and len(result) - 1 != i:
                string_result += 'y' + "'" * i + '*' + '(' + str(result[i]) + ') + '
            elif i % 2 != 0 and i != len(result) - 1:
                string_result += '( - y' + "'" * i + ')' + '*' + '(' + str(result[i]) + ') + '
            else:
                string_result += '( - y' + "'" * i + ')' + '*' + '(' + str(result[i]) + ') = 0 or ...'
        print(string_result.replace('**', '^'))
        return string_result
    if order >= 3:  # matrix >= 4 order ...
        matrix = Matrix(array)
        print("\t" * 20 + "EULER FORM:")
        print("_" * 250)
        print(str(det(matrix)) + " = 0 or ....")


def find_euler(order=int(input('Enter the order of the equation: '))):
    # порядок уравнения соответствует количеству решений
    visual_row = '\t' * 20 + 'fundamental decision system'.upper() + '\n'
    row, col = order, order
    roots = list(map(int, input('Enter characteristic roots (separated by a space): ').split()))
    roots = [x ** i for i in roots]
    print(roots, ' Substitution of characteristic roots by the formula y = x^k \n\n')
    if len(roots) != order:
        print(
            'The number of roots does not match the order of the equation'
            '\nImpossible to build FDS\n'
            'Unable to compute determinant'
        )
        return find_euler(int(input('\nEnter the order of the equation: ')))
    else:
        for i in range(order + 1):
            # first_row.append('y' + "'" * i)
            first_row.append(a[str(i)])
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
        for i in range(order):
            for j in range(order):
                space = 15
                if len(str(matrix[i][j])) > 1:
                    space = space - (len(str(matrix[i][j])) - 2)
                visual_row += "|    " + str(matrix[i][j]).replace("**", '^').replace("*", '') + " " * space + '|'
            visual_row += '\n'
        print(visual_row)

        find_determinate(order, matrix)


find_euler()
