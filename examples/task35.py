# 35. Напишите функцию, которая принимает
# одно число и проверяет, является ли оно простым

# *Напоминание: Простое число - это число,
# которое имеет 2 делителя: 1  и n(само число)*

def primary(n, temp_div = None) -> bool:
    if temp_div is None:
        temp_div = n - 1
    while temp_div >= 2:
        if n % temp_div == 0:
            return False
        return primary(n, temp_div - 1)
    return True


n = int(input())
print(primary(n))

#Решение препода

def is_prime(n: int, divider: int) -> bool:
    """рекурсивная проверка простоты числа"""
    if divider == 1:
        return True
    if n % divider == 0:
        return False
    return is_prime(n, divider - 1)


n = 11
print(is_prime(n, n//2 + 1))

for i in range(n//2 + 1, 1, -1):
    print(i, n % i)