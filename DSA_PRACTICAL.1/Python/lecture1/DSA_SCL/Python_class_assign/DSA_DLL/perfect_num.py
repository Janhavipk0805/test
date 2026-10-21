def checkPerfectNumber(num: int) -> bool:
    # Write your solution here
    # 1 and negative numbers are not perfect number
    if num <= 1:
        return False
    total = 1

    i=2
    while i * i <= num:
         if num % i == 0:
              total += i

              if i != num // i:
                   total += num //i
         i+= 1
    return total == num