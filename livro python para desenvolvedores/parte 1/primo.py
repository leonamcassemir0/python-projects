def is_prime(n):
    if n < 2:
        return False
    
    for i in range (2, n):
        if not n % i:
            return False
        else:
            return True


for x in range(1,101):
    if is_prime(x):
        print(x)