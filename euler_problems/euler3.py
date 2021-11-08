def hpf(number):
    factor_list = []
    prime_list = []
    isPrime = False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            factor_list.append(i)
            factor_list.append(number/i)
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
