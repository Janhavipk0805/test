def digitsInFactorial(n: int) -> int:
    if n <= 1:
        return 1
    digits =0
    for i in range(2, n+1):
        import math
        digits += math.log10(i)
    return int(digits) +1