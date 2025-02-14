# Task 3_1
def medium(a, b, c):
    if a > b:
        if b > c:
            return b
        elif a > c:
            return c
        else:
            return a
    else:
        if a > c:
            return a
        else:
            if b > c:
                return c
            else:
                return b

numbers_str = input("Введите три целых числа: ")
numbers = list(map(int, numbers_str.split()))
x1, x2, x3 = numbers

res = medium(x1, x2, x3)
print(res)

# Task 3_2
def print_sqr(n):
    # формируем строку из N символов
    str = ""
    for i in n:
        str += "*"
    print(str)
    for k in range(0, n):
        print("*")

print_sqr(int(input("Введите целое число: ")))