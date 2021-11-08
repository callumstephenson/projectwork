def hpf(number):
    factor_list = []
    prime_list = []
    isPrime = False
    # Generating list of factors 1->sqrt(num)
    # Can do this due to sqrt(x)*sqrt(x) = x, therefore for each factor, 
    # one factor is always less than or equal to sqrt(x), hence by only
    # checking up to sqrt(x) and generating converse factor, saves time.
    for potentialFactor in range(2, int(number**0.5)+1):
        if number % potentialFactor == 0:
            factor_list.append(potentialFactor)
    # Generating converse factor to append list with num/factor
            factor_list.append(number/potentialFactor)
    # Checking for primes in the factor list
    for factor in range(len(factor_list)):
        for n in range (2, int(factor_list[factor]**(0.5) +1)):
            if factor_list[factor] % n == 0:
                break
            else:
                isPrime = True
        if isPrime == True:
            prime_list.append(factor_list[factor])
    return max(prime_list)

print(hpf(600851475143))
