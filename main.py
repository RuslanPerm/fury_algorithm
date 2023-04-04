import random


# создание графа
def graph_creation():
    try:
        vertex_quantity = int(input('Введите кол-во вершин: '))
        l_v = {}  # создаём будущий граф

        # составляем граф, создавая по 1 вершине и прикрепляя к ней связаннные вершины в виде списка
        for vertex in range(vertex_quantity):
            v_name = input('Введите название вершины: ')
            linked_vertex_list = input(f'Введите название вершин, связанных с {v_name} (через пробел): ').split()

            l_v.update({v_name: linked_vertex_list})  # добавляем в словарь к ключу вершины список из связанных вершин

        return l_v

    except ValueError or TypeError:
        print('Введите целое число вершин, попробуйте ещё раз')
        graph_creation()


# проверка на условие эйлеровости
def check_e_condition(link_vertex):
    link_count = 0  # количество чётных связей вершины
    vertex_list = link_vertex.values()  # список вершин

    for vertex in vertex_list:
        if len(vertex) % 2 == 0:  # если длинна списка вершин, связанных с рассматриваемой чётная
            link_count += 1

    if link_count == len(vertex_list):  # все ли вершины чётные
        return ['eiler', link_vertex]  # возвращаем тип графа, сам граф
    elif len(vertex_list) - link_count >= 2:  # если кол-во вершин с нечётной степенью меньше или равно 2
        return ['semi-eiler', link_vertex]  # возвращаем тип графа, сам граф
    else:
        return 'not eiler'


def built_circle(graph):
    if graph[0] == 'eiler':  # если граф эйлеровый
        lst_v = [i for i in graph[1].keys()]  # составляем список вершин
        aa = random.choice(lst_v)  # выбираем случайную вершину
        return aa

    elif graph[0] == 'semi-eiler':  # если граф полуэйлеровый
        pass
    else:
        return 'Граф не является Эйлеровым, невозможно использовать алгоритм Флери'


# l_v = graph_creation()
# эйлеров граф (пример)
a, b, c, d, e, f = 'a', 'b', 'c', 'd', 'e', 'f'
l_v = {
    a: [b, c],
    b: [a, c, d, e],
    c: [b, f, d, a],
    d: [b, e, c, f],
    e: [b, d],
    f: [c, d]
}

is_graph_e = check_e_condition(l_v)
print(built_circle(check_e_condition(l_v)))
