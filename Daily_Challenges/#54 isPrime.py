def isPrime(number):
    for num in range(2, number//2):
        if number % num == 0:
            return False
    return True
