def is_prime(func): #  распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае
    def wrapper(*args):
        res = func(*args)
        if res < 2:
            return False
        for i in range(2, int(res**0.5) + 1):
            if res % i == 0:
                print('Составное чиcло')
                return res
        print('Простое число')
        return res
    return wrapper


@is_prime
def sum_three(*args): # складывает 3 числа
    sum_nums = sum(args)
    return sum_nums


result = sum_three(2, 3, 6)
result1 = sum_three(2, 3, 11)
print(result)
print(result1)
