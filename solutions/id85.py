target = 2000000
closest_area = 0
closest_difference = float('inf')

for width in range(1, 2000):
    for height in range(1, 2000):
        count = (width * (width + 1) // 2) * (height * (height + 1) // 2)
        difference = abs(count - target)
        if difference < closest_difference:
            closest_difference = difference
            closest_area = width * height
        if count > target:
            break

print(closest_area)