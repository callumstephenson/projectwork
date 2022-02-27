def hpf(number):
    factor_list = []
    prime_list = []
    isPrime = False
    # Generating list of factors 1->sqrt(num)
    # Can do this due to sqrt(x)*sqrt(x) = x, therefore for each factor, 
    # one factor is always less than or equal to sqrt(x), hence by only
    # checking up to sqrt(x) and generating converse factor, saves time.
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            factor_list.append(i)
    # Generating converse factor to append list with num/factor
            factor_list.append(number/i)
    # Checking for primes in the factor list
    for j in range(len(factor_list)):
        for n in range (2, int(factor_list[j]**(0.5) +1)):
            if factor_list[j] % n == 0:
                isPrime = False
                break
            else:
                isPrime = True
        if isPrime == True:
            prime_list.append(factor_list[j])
    return max(prime_list)

print(hpf(600851475143))