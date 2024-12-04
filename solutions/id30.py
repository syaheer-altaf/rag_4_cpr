def sum_of_fifth_powers():
    fifth_powers = [i**5 for i in range(10)]
    total_sum = 0
    
    limit = 354294
    
    for num in range(10, limit + 1):
        if num == sum(fifth_powers[int(digit)] for digit in str(num)):
            total_sum += num
    
    return total_sum

result = sum_of_fifth_powers()
print(result)