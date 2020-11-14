def get_fibonacci(n, cache=dict()):
    if n in cache: return cache[n]
    if n == 0 or n == 1: return n

    result = get_fibonacci(n - 2, cache) + get_fibonacci(n - 1, cache)

    cache[n] = result

    return result


def get_fibonacci_list_smaller_than(n):
    count = 0
    last_result = 0
    fibonacci_list = []

    while True:
        result = get_fibonacci(count)

        if result > n:
            break

        fibonacci_list.append(result)
        count += 1

    return fibonacci_list
