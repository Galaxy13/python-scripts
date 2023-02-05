import sys


def rain_water(height: list) -> int:
    water_sum = 0
    left_p = 0
    right_p = len(height) - 1
    max_left_wall = max_right_wall = 0
    while left_p < right_p:
        if height[left_p] <= height[right_p]:
            if height[left_p] >= max_left_wall:
                max_left_wall = height[left_p]
            else:
                water_sum += max_left_wall - height[left_p]
            left_p += 1
        else:
            if height[right_p] >= max_right_wall:
                max_right_wall = height[right_p]
            else:
                water_sum += max_right_wall - height[right_p]
            right_p -= 1
    return water_sum


sys.stdin.readline()
height_arr = [int(num) for num in sys.stdin.readline().rstrip('\n').split()]
print(rain_water(height_arr))
