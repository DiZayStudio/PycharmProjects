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
##########################################################################
# Task 3_2
def print_sqr(n):
    # формируем строку из N символов
    s1 = "*" * n
    s2 = " " * n
    s_new = "*" + s2[1:n-1] + "*"

    print(s1)
    i = 1
    while i < n - 1:
        print(s_new)
        i += 1
    print(s1)

print_sqr(int(input("Введите целое число больше 1:")))
#############################################################################
# Task 3_2
