import math

def find_smallest_blue_discs():
    x0 = 3
    y0 = 1
    x = x0
    y = y0
    while True:
        sqrt_val = 8 * y**2 + 1
        sqrt_s = int(math.isqrt(sqrt_val))
        if sqrt_s * sqrt_s == sqrt_val and (sqrt_s + 1) % 2 == 0:
            blue_discs = (sqrt_s + 1) // 2 + y
            if blue_discs + y > 10**12:
                print(blue_discs)
                break
        next_x = x * x0 + y * y0 * 8
        next_y = x * y0 + y * x0
        x = next_x
        y = next_y

find_smallest_blue_discs()