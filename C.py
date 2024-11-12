Задача C. Одержимый
                                
# C.py  - решение МОЁ

n, k = map(int, input().split())
a = list(map(int, input().split()))
if len(a) != n: raise ValueError()
list_a_1 = [a[i:j] for i in range(n) for j in range((i+1), n+1)]
list_a_2 = [elem for elem in list_a_1 if sum(elem) <= k]
list_a_3 = [elem for elem in list_a_2 for i in elem if elem.count(i == 0) >= 2]
list_a_4 = [elem for elem in list_a_2 if len(elem) > 1 and sum(elem) == 0]
count_a = len(list_a_2) - len(list_a_3) - len(list_a_4)

print(count_a)
