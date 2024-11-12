Задача A. Известный художник

# A.py  - решение МОЁ

n = int(input(''))  # количество дней
a = list(map(int, input().split()))  # список значений яркости
a_i = max(a)
a_j = min(a)
a_max = max([i for i in range(len(a)) if a[i] == a_i])
a_min = min([i for i in range(len(a)) if a[i] == a_j])

print(a_max+1, a_min+1)
