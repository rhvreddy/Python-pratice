def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False

    # Loop throught all the numbers between 2 and the numbers

    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False

    # This return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return True