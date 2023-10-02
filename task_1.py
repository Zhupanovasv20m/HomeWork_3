# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]

my_list = [1, 2, 3, 1, 2]
new_list = []
res = []

for i in my_list:
    count = my_list.count(i)
    if count > 1:
        new_list.append(i)

for i in new_list:
    if i not in res:
        res.append(i)

print(res)