A = {}
A['start'] = {}
A['start']['1'] = 5
A['start']['2'] = 2
A['1'] = {}
A['1']['3'] = 4
A['1']['4'] = 2
A['2'] = {}
A['2']['1'] = 8
A['2']['4'] = 7
A['3'] = {}
A['3']['4'] = 6
A['3']['end'] = 3
A['4'] = {}
A['4']['end'] = 1
A['end'] = {}

print(f'Graph 1:\n{A}')

B = {}
B['start'] = {}
B['start']['1'] = 10
B['1'] = {}
B['1']['2'] = 20
B['2'] = {}
B['2']['3'] = 1
B['2']['end'] = 30
B['3'] = {}
B['3']['1'] = 1
B['end'] = {}

print(f'Graph 2:\n{B}')

C = {
    'start': {'1': 2, '2': 2},
    '1': {'end': 2, '3': 2},
    '2': {'1': 2},
    '3': {'2': -1, 'end': 2},
    'end' : {}
     }

print(f'Graph 3:\n{C}')

choice = int(input('Выберите, с каким графам будем работать (1, 2, 3): '))
if choice == 1:
    graph = A
elif choice == 2:
    graph = B
elif choice == 3:
    graph = C
else:
    print('Error')

# 1. Создаем хэш-таблицы весов и родителей, а также список посещенных узлов

costs = {}
parents = {}
visited = []

for n in graph:
    costs[n] = float('inf')
    parents[n] = None
for n in graph:
    if n == 'start':
        for i in graph[n]:
            costs[i] = graph[n][i]
            parents[i] = 'start'
        costs.pop(n)
        parents.pop(n)

# 2. Создадим функцию поиска узла с наименьшей стоимостью

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for n in costs:
        cost = costs[n]
        if cost < lowest_cost and n not in visited:
            lowest_cost = cost
            lowest_cost_node = n

    return lowest_cost_node

# 3. Напишем основной алгоритм:
"""
1. Пока остаются необработанные узлы ->
2. Взять узел, ближайший к началу ->
3. Обновить стоимости его соседей ->
4. Если стоимости каких-либо соседей были обновлены, обновить родителей ->
5. Пометить узел как обработанный ->
6. см. п. 1
"""

node = find_lowest_cost_node(costs) # Выбираем самый дешевый узел

while node is not None: # Пока есть непосещенные узлы:
    cost = costs[node] # Текущий вес узла
    contacts = graph[node] # Соседи узла

    for n in contacts.keys(): # Для каждого соседа
        new_cost = cost + contacts[n] # Определяем новый вес
        if new_cost < costs[n]: # Если новый вес меньше, чем преждний:
            costs[n] = new_cost # Меняем его вес в таблице весов
            parents[n] = node # И добавляем ему родителя
    visited.append(node) # Помечем узел как посещенный
    node = find_lowest_cost_node(costs)  # Выбираем новый самый дешевый узел

def get_parent(parents, node):
    return parents[node]

node = 'end'
way = ['end']
parent = None
while parent != 'start':
    parent = get_parent(parents, node)
    way.append(parent)
    node = parent
way = list(reversed(way))


print(f'{"-"*50}\nCosts: {costs["end"]}\nWay: {way}')

