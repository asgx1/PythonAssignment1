def is_perfect(number):
    divisors_sum = sum(i for i in range(1, number // 2 + 1) if number % i == 0)
    return divisors_sum == number
perfect_numbers = [num for num in range(1, 1000000) if is_perfect(num)]
print("Perfect numbers less than 1,000,000:", perfect_numbers)
