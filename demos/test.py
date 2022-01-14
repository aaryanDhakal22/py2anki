# Program that checks if the number is palindrome

# You check the first and the last digit using mod by 10 and log10(x)
# compare them and then continue checking and remove the last and first
# digit and move the mod mask by 100 because u removed 2 digits

# O(n/2)
# O(1)

import math


def is_palindrome(x):
    if x <= 0:
        return x == 0
    num_digit = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digit - 1)

    for i in range(num_digit // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100

    return True
