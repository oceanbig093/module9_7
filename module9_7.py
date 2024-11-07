def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if result < 2:
            return "Составное"  # 0 и 1 не являются простыми числами
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                return "Составное"
        print(result)
        return "Простое" 
    return wrapper

@ is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6) 
print(result)
