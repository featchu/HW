# exercitiu posibil sting-uri MID

import sys

# biblio ptr max value
list1 = ['Maria', 'Ioan', 'Roxana', 'Gheorghe', 'Ana', 'Georgia', 'Ioan', 'Roxana', 'Maria', 'Ionel', 'Roxana', 'Ioan',
         'Gheorghe', 'Xenia']


# functie sortare lista
def sort_by_name(list2):
    list2.sort()
    return list2


# functie nr aparitii al fiecarui nume din lista
def numar_aparitii(list2):
    # SHORT BODY aparitii = dict((i, list2.count(i)) for i in list2)
    aparitii = {}
    for i in list2:
        aparitii[i] = list2.count(i)
    return aparitii


# functie cel mai frecvent nume din lista
def most_frequent(list2):
    aparitii = numar_aparitii(list2)
    max_freq = 0
    max_name = ''
    lista_most_freq = []
    for i in aparitii:
        if aparitii[i] > max_freq:
            max_freq = aparitii[i]
            max_name = i
    for i in aparitii:
        if aparitii[i] == max_freq:
            lista_most_freq.append(i)
    #   print(max_freq)
    #   frecventa

    if len(lista_most_freq) > 0:
        return lista_most_freq
    else:
        return max_name


# functie cel mai putin frecvent nume din lista


def less_frequent(list2):
    aparitii = numar_aparitii(list2)
    min_freq = sys.maxsize
    min_name = ''
    lista_less_freq = []
    for i in aparitii:
        if aparitii[i] < min_freq:
            min_freq = aparitii[i]
            min_name = i
    for i in aparitii:
        if aparitii[i] == min_freq:
            lista_less_freq.append(i)
    #   print(max_freq)
    #   frecventa

    if len(lista_less_freq) > 0:
        return lista_less_freq
    else:
        return min_name


print(sort_by_name(list1))
print(numar_aparitii(list1))
print(most_frequent(list1))
print(less_frequent(list1))
