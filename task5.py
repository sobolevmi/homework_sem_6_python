# Реализация алгоритма по перемешиванию списка

size = int(input("Введите размер списка: "))
first_list = list(range(1, size + 1))

print(f"Первоначальный список: {first_list}")

result_list = list()
for index, item in enumerate(first_list):
    if index % 2 == 0:
        result_list.append(item)

for index, item in enumerate(first_list):
    if index % 2 != 0:
        result_list.append(item)

print(f"Перемешанный список:{result_list}")
