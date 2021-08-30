'''
В предыдущей главе (Поиск в ширину) мы узнали, как найти путь из точки А в точку Вю
Найденный путь не обязательно окажется самым быстрым. Этот путь считается кратчайшим,
потому что он состоит из наименьшего количества сегментов.

Но если с каждым сегментом связывается продолжительность перемещения, то тогда выясняется, что существует
и более быстрый путь.
'''

'''
Алгоритм Дейкстры.

Каждому ребру назначется время перемещения в минутах. Алгоритм Дейкстры испольуется для поиска пути от начальной точки
к конечной за кратчайшее возможное время.

Алгоритм Дейкстры состоит из четырех шагов:
    1) Найти узел с наименьшей стоимостью (то есть узел, до которого можно добраться за минимальное время)
    2) Обновить стоимость соседей этого узла 
    3) Повторять, пока это не будет сделано для всех узлов графа
    4) Вычислить итоговый путь
    
В алгоритме Дейкстры каждому сегменту присваивается число (вес), а алгоритм Дейкстры находит путь с наименьшим суммарным весом.

Граф с весами называется "Взвешенным графом"
А граф без весов - "Невзвешенным графом"
Алгоритм Дейкстры работает только с НАПРАВЛЕННЫМИ АЦИКЛИЧЕСКИМИ ГРАФАМИ (DAG).

Ключевая идея Алгоритма Дейкстры: в графе ищется путь с наименьшей стоимостью. Пути к этому узлу с меньшими затратами не существует!

'''

# Реализация!
# Задание - найти наименьший путь от начала до конца.

# Взвешенный граф представляем в виде словаря, в котором, у каждого ключа (вершины) есть ребра (связи с другими вершинами)
# и вес этих ребер. Значение ключа (ребра + вес) представляем словарем.

graph = {} # Наш граф

graph['start'] = {} # Веришна старта

graph['start']['a'] = 6 # Ребро (а) и вес ребра (6)
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['end'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5

graph['end'] = {}
print(f'Граф: {graph}')

# Соседей узла можно получить с поломщью следующего выражения:
print(f'Соседи начального узла: {graph["start"].keys()}')
# Веса ребер можно узнать так:
print(f"Веса ребер: {graph['start']['a'], graph['start']['b']}")

# Отдельно создадим хэш-таблицу для хранения стоимостей всех УЗЛОВ

# Если стоимость еще не известна, то заменям ее на бесконечноть:
infinity = float('inf')

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity
print(f'Стоимости узлов: {costs}')

# И создаем отдельную хэш-таблицу для родителей

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None
print(f'Родители: {parents}')

# И создадим массив для отслеживания всех уже обработанных узлов:
processed = []

# Подготовка завершена. Можно переходить к алгоритму

"""
1. Пока остаются необработанные узлы ->
2. Взять узел, ближайший к началу ->
3. Обновить стоимости его соседей ->
4. Если стоимости каких-либо соседей были обновлены, обновить родителей ->
5. Пометить узел как обработанный ->
6. см. п. 1
"""

# Реализуем этот алгоритм!!

# Поиск узла с наименьшей ценой
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) # Ищем узел с наименьшей стоимостью (весом ребра)
while node is not None: # Пока все узлы не обработаны:
    cost = costs[node] # Стоимость узла
    neighbors = graph[node] # Соседи узла

    for n in neighbors.keys(): # Перебираем соседей
        new_cost = cost + neighbors[n] # Новая стоимость складывается из стоипости узла n и расстояния до соседа
        if costs[n] > new_cost: #  Сравним стоимости
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(f'{"-"*50}\nРезультат:\nРодители: {parents}\nСтоимость: {costs}')

def get_parent(parents, node):
    print(f'{node} - {parents[node]}')
    return parents[node]

parent = get_parent(parents, 'end')
print(parent)

node = 'end'
way = ['end']
while parent != 'start':
    parent = get_parent(parents, node)
    way.append(parent)
    node = parent
way = list(reversed(way))
print(f'Way: {way}')