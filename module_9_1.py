def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result


def min_num(int_list):
    return min(int_list)


def len_str(int_list):
    return len(int_list)


def sorted_list(int_list):
    return sorted(int_list)


def sum_num(int_list):
    return sum(int_list)


def max_num(int_list):
    return max(int_list)


print(apply_all_func([6, 20, 15, 9], min_num, max_num)) # вывод {'max': 20, 'min': 6}
print(apply_all_func([6, 20, 15, 9], len_str, sum_num, sorted_list)) # выводим {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}



