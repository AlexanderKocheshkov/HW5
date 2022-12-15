def fib(n):
    if n == 0:
        return "Ошибка"
    if n in (1,2):
        return 1
    return fib(n - 1) + fib(n - 2)

print("Введите значение: ", end="")
a = int(input())
print("Значение числа Фибоначчи: ", fib(a))