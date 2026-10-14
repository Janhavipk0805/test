def reverseInteger(n):
    sign = -1 if n<0 else 1
    result = 0
    while n>0:
        result = result*10+n % 10
        n //=10
        return sign * result