def isprime(num):
    for i in range(2,num):
        if(num % i == 0):
            return False
    return True

for x in range (1,10000000000):
    if isprime(x):
        print(x)
