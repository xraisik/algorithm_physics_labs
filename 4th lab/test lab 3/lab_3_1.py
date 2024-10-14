def get_numbers_in_between(a: list[int], b: list[int]) -> list[int]:
    result = []

    max_a = max(a)
    min_b = min(b)

    for i in range(max_a, min_b + 1):
        is_divisible_by_a = all(i % num == 0 for num in a)

        divides_all_b = all(num % i == 0 for num in b)

        if is_divisible_by_a and divides_all_b:
            result.append(i)

    return result