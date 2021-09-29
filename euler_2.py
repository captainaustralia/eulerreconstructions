from timeit import timeit

from sympy.abc import x, D, k
from sympy import *
from time import *

res = []
subs_dict = {str(x ** i): k for i in range(100)}


def regrouping(array_name, order):
    memory = {}
    for i in array_name:
        local_memory = ''
        if i == '-' or i == '+':
            continue
        for j in range(len(i)):
            if i[j] == 'k' and j == 0:
                memory[i] = 1
                break
            if i[j].isdigit():
                local_memory += i[j]
            else:
                memory[i[j::]] = int(local_memory)
                break

    for i in range(2, order):
        if str(k) + str(i) not in memory.keys():
            memory[str(k) + str(i)] = 0

    return memory


def euler(order=int(input('Введите порядок уравнения: '))):
    print('Порядок - ', order)
    roots = list(map(int, input('Введите корни характеристического уравнения: ( через пробел ): ').split()))
    if len(roots) != order:
        print('Количество корней не совпадает с порядком')
        return euler(order=int(input('Введите порядок уравнения: ')))
    lambdas = [1]
    memory = {}
    a = 1
    counter = -1
    alphas_counter = 0
    for j in roots:
        a *= (k - j)
    a = expand(a)
    print('Характеристическое уравнение :', a, ' = 0')
    a = str(a).replace('*', '')
    a = a.split()
    memory = regrouping(a, order)
    # print(memory, 'LAMBDAS')

    memory_eq = []  # save all D(D-1)(D-2)(D-3)....... for all orders
    for i in range(order):
        eva = 1
        for j in range(order - i):
            eva *= (k - j)
        memory_eq.append(str(expand(eva)).replace('*', ''))

    memory_eq_dict = {}
    for i in range(len(memory_eq)):
        rofl = memory_eq[i].split()
        memory_eq_dict[str(len(memory_eq) - i)] = regrouping(rofl, len(memory_eq))
    if 'k' not in memory.keys():
        memory['k'] = 0
    memory['k1'] = memory['k']
    alphas = [1]
    for i in range(1, order):  # Соответствует количеству необходимых альф, т.е 4 порядок -> 4 коэф найти i = 1 / i = 2
        lambda_i = memory['k' + str(order - i)]  # 4 - 1 -> k3 -> 10
        sum_i = 0
        for j in range(1, i + 1):  # [0,1]
            if order - i == 1:
                sum_i += alphas[j - 1] * memory_eq_dict[str(order - j + 1)]['k']
            else:
                sum_i += alphas[j - 1] * memory_eq_dict[str(order - j + 1)][
                    'k' + str(order - i)]  # 1 * '4'['k3'] = 1 * 6, 0 + 6 = 6
        alphas.append(abs(lambda_i - sum_i))


    while True:
        counter += 1
        if counter == len(a) - 1 and not a[counter].isdigit():
            z = a[counter]
            z = z[0:-1] + 'xy'
            a[counter] = z
            break
        if a[counter] == '+' or a[counter] == '-':
            continue
        elif a[counter].isdigit():
            a[counter] += 'y'
            break
        else:
            a[counter] = str(alphas[alphas_counter]) + 'x' + '^' + str(((len(alphas)) - alphas_counter)) + 'y' + "'" * (
                    (len(alphas)) - alphas_counter)
        if counter == len(a) - 1:
            break
        alphas_counter += 1
    result = ''
    for i in a:
        result += ' ' + i
    print('\t' * 10 + 'EULER FORM')
    print(result[2::], '= 0 or ....')


euler()
print(process_time(), 'sec')
