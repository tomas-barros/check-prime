def check_prime(number):
    if number < 2:
        return False

    root = int(number**0.5) + 1
    for i in range(2, root):
        if number%i == 0:
            return False
    return True