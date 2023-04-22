# 33. Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# list = [1, 2, 3, 1, 5, 5]

# max = max(list)
# min = min(list)

# for i in range(len(list)):
#     if list[i] == max:
#         list[i] = min

# print(list)

def rek(leng, array, max_v, min_v):
    if leng == 0:
        return array
    if array[leng] == max_v:
        array[leng] = min_v
    return rek(leng - 1, array, max_v, min_v)

array = list(map(int, input('Введите оценки Василия: ').split()))
print(array)

print(rek(len(array) - 1, array, max(array), min(array)))

#Решение препода

def change_marks(marks: list[int]) -> list[int]:
    """Рекурсивная замена макисмальных оценок минимальными"""

    max_mark = max(marks)
    min_mark = min(marks)
    marks[marks.index(max_mark)] = min_mark

    if max_mark not in marks:
        return marks
    return change_marks(marks)


print(change_marks([1, 2, 3, 1, 1, 3, 4, 4, 5, 4]))

a = [1, 2, 3, 1, 1, 3, 4, 5, 5, 5]
print(a.index(5))

a[a.index(5)] = 1000
print(a)