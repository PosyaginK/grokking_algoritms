# 6.1 Найти длину кратчайшего пути от начального до конечного узла.

graph_1 = {
    0: [1, 2],
    1: [3, 4],
    2: [3, 5],
    3: [],
    5: [4]
    }

# 6.2 Найдите длину кратчайшего пути от "cab" к "bat"

graph_2 = {
    'cab': ['cat', 'car'],
    'car': ['cat', 'bar'],
    'cat': ['mat', 'bat'],
    'bar': ['bat'],
    'mat': ['bat']
}

# Решение без очереди
def get_way(graph, start, end):
    items = []
    for i in graph:
        items.append(i) # Все вершины графа

    way = [start] # Создаем список "путь" и помещаем туда элемент старта
    for item in items: # Для каждой вершины
        if item == end: # Если вершина равна искомой
            way.append(item) # Добавляем ее в список
            return way # И взовращаем список
        else:
            els = graph[item] # Соседи текущей вершины
            for el in els:
                if el == end:
                    way.append(item)
                    way.append(el)
                    return way

r_1 = get_way(graph_1, 0, 4)
print(f'Первый граф. Кратчайший путь от 0 до 4 - {r_1}')
r_2 = get_way(graph_2, "cab", "bat")
print(f'Второй граф. Кратчайший путь от "cab" до "bat" - {r_2}')


# Решение с использованием очереди
from collections import deque

def search(graph, start, end):
    search_queue = deque() # Создаем очередь
    search_queue += graph[start] # Добавляем в очередь первый элемент

    searched = [] # Массив для пройденных вершин
    steps = 0
    while search_queue: # Пока очередь не пуста
        el = search_queue.popleft() # Берем первый элемент
        if not el in searched: # Если его еще нет в списке пройденных
            if el == end: # Если это искомый элемент
                searched.append(el)
                print(f'{end} is {el}, {steps - 1} steps')
                return searched
            else:
                search_queue += graph[el]
                searched.append(el)
                steps += 1
    return steps

r = search(graph_1, 0, 4)
print(r)

# Вообще не понимаю эти очереди! Без них намного проще

