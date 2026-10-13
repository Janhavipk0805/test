def isPerfectNumber(n):
    sum = 1
    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            sum= sum+ i
            sum += n//i 
    return sum == n
    pass