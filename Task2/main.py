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

#x1, x2, x3 = int(input("Введите целые числа:"))
x1 = 3
x2 = 20
x3 = 1

res = medium(x1, x2, x3)
print(res)
#print(medium(x1, x2, x3))
