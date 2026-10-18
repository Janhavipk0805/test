def sum_of_squares(nums):
    n = len(nums)
    total = 0

    # The problem is 1-indexed, so i goes from 1 to n
    for i in range(1, n+1):
        if n % i ==0:
            total += nums[i -1]**2
    return total
    print(total)