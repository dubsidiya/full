from time import time
start = time()

# Загрузка точек из файла '27-10'
points = []
with open('27-10') as f:
    for line in f:
        # Заменяем запятую на точку и считываем координаты как float
        x, y = map(float, line.replace(',', '.').split())
        points.append((x, y))
n = len(points)

# Параметры
r = 0.3  # радиус для объединения точек в кластер
r2 = r * r  # квадрат радиуса, чтобы не вычислять sqrt постоянно

# Функция для определения номера ячейки по точке
def get_cell(p):
    # Размер ячейки равен r, чтобы соседние ячейки охватывали расстояния до r
    return (int(p[0] / r), int(p[1] / r))

# Создаем пространственную сетку: для каждой ячейки храним список индексов точек
grid = {}
for i, p in enumerate(points):
    cell = get_cell(p)
    grid.setdefault(cell, []).append(i)

# Готовим смещения для обхода соседних ячеек (3x3)
neighbors_offsets = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]

# Структура union-find (для объединения точек в кластеры)
parent = list(range(n))

def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i

def union(i, j):
    ri = find(i)
    rj = find(j)
    if ri != rj:
        parent[rj] = ri

# Для каждой точки проверяем точки в соседних ячейках
for i, p in enumerate(points):
    cell = get_cell(p)
    for dx, dy in neighbors_offsets:
        neighbor_cell = (cell[0] + dx, cell[1] + dy)
        if neighbor_cell in grid:
            for j in grid[neighbor_cell]:
                # Чтобы избежать проверки пары дважды, сравним индексы
                if i < j:
                    q = points[j]
                    dx_ = p[0] - q[0]
                    dy_ = p[1] - q[1]
                    if dx_*dx_ + dy_*dy_ <= r2:
                        union(i, j)

# Группируем точки в кластеры по корневому родителю
clusters = {}
for i in range(n):
    root = find(i)
    clusters.setdefault(root, []).append(i)

# Для каждого кластера вычисляем "центр" – точку, минимизирующую сумму расстояний до остальных точек кластера
def total_distance(idx, indices):
    p = points[idx]
    s = 0.0
    for j in indices:
        if j != idx:
            q = points[j]
            dx_ = p[0] - q[0]
            dy_ = p[1] - q[1]
            s += (dx_*dx_ + dy_*dy_)**0.5
    return s

centers = []
for indices in clusters.values():
    best = None
    best_val = float('inf')
    for i in indices:
        dist_sum = total_distance(i, indices)
        if dist_sum < best_val:
            best_val = dist_sum
            best = i
    centers.append(points[best])

# Вычисляем среднее значение координат центров кластеров и умножаем на 10000
if centers:
    avg_x = sum(p[0] for p in centers) / len(centers)
    avg_y = sum(p[1] for p in centers) / len(centers)
    avg_x_int = int(avg_x * 10000)
    avg_y_int = int(avg_y * 10000)
else:
    avg_x_int = avg_y_int = 0

# Вывод результатов
print("Центры кластеров:")
for c in centers:
    print(c)
print("Среднее (умноженное на 10000):", avg_x_int, avg_y_int)
print("Время выполнения: {:.3f} секунд".format(time() - start))
