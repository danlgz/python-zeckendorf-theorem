from fibonacci import get_fibonacci_list_smaller_than

def zeckendorf(n):
    fibonacci_list = get_fibonacci_list_smaller_than(n)[::-1]
    result = []

    i = 0
    sub_accomulator = n

    while sum(result) < n and len(result) < len(fibonacci_list):
        current_fibo = fibonacci_list[i]
        result.append(current_fibo)
        sub_accomulator -= current_fibo

        for j in range(i, len(fibonacci_list)):
            if fibonacci_list[j] <= sub_accomulator:
                i = j
                break

    return result[::-1]
