# 3. Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав
# его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

my_dict = {'еда': 7, 'вода': 4, 'вещи': 2.3, 'лекарство': 1.4}
max_weight = 15
our_pack = []

for key, value in my_dict.items():
    if value <= max_weight:
        our_pack.append(key)
        max_weight -= value
print(our_pack)