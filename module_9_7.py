def is_prime(func): #  распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае
    def wrapper(*args):
        res = func(*args)
        if res % 2:
            print(f'Простое')
        else:
            print(f'Составное')
        return res
    return wrapper


@is_prime
def sum_three(*args): # складывает 3 числа
    sum_nums = 0
    for nums in args:
        sum_nums += nums
    return sum_nums


result = sum_three(2, 3, 6)
result1 = sum_three(2, 3, 7)
print(result)
print(result1)
