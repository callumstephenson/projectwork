def euler2(limit):
    if limit == 0 or limit == 1:
        return 0
    fibsum = 0
    num1 = 1
    num2 = 2
    num3 = 0
    while num3 <= limit:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        if num3 % 2 == 0:
            fibsum += num3
    return fibsum