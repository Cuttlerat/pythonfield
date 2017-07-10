#!/bin/python

def is_prime(x):
    prime = False
    if x > 1:
        prime = True
        k = 2
        n = x ** 0.5
        while k <= n and prime == True:
            if x % k == 0:
                prime = False
            k += 1
    return prime

for i in range(10000):
    if is_prime(i):
        print(str(i))
