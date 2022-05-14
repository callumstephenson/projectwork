import math

def f(x):
    x*x*math.sin(x*x)

def two_sided_diff():
    for x in [10,100,1000,10000]:
        H = [10**-9, 10**-12, 10**-5]
        return_list = []
        for each in H:
            b = f(f(x+each)-f(x-each))/(2*h)
            return_list.append[b]

def complex_step_method():
    for x in [10,100,1000,10000]:
        H = [10**-9, 10**-12, 10**-15]
        return_list = []
        for each in H:
            b = f(x+each*1j).imag/each
            return_list.append[b]
        print(return_list)

if __name__ == "__main__":
    complex_step_method()