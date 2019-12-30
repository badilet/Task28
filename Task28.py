# Напишите функцию где дан список целых чисел. Заменить отрицательные на -1,
# положительные - на число 1, ноль оставить без изменений.

num_list = input("Enter list of whole numbers:").split(',')
empty = []
for i in num_list:
    if int(i) > 0:
        empty.append(1)
    elif int(i) < 0:
        empty.append(-1)
    elif int(i) == 0:
        empty.append(0)
    else:
        None
print(empty)

# neg = [-1 if x < 0 else x for x in num_list]
# print("Negative numbers replaced with -1:", neg)
#
# pos = [1 if x > 0 else x for x in num_list]
# print("Positive numbers replaced with 1:", pos)
