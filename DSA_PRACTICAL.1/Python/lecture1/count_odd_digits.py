def countOddDigits(n):
    count = 0
    for digits in str(abs(n)):
       if int(digits) %2==1:
         count+=1
    return count
    pass