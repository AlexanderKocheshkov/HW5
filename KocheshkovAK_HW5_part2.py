def summator(*args):
    summ = 0
    for x in args:
        summ += float(x)
    return summ

print("Введите последовательность через пробел: ", end ="")
vv = input().split(" ")
print("Сумма равна: ", summator(*vv))
