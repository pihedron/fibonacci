import time
import sys

sys.set_int_max_str_digits(1 >> 128)

def fibonacci(n):
    if n == 0: # base case
        return [0, 2]
    
    if n & 1: # n is odd
        F, L = fibonacci(n - 1)
        return [(F + L) >> 1, (5 * F + L) >> 1]
    
    # n is even
    n >>= 1 # divide n by 2
    k = n % 2 * 2 - 1
    F, L = fibonacci(n)
    return [F * L, L ** 2 + 2 * k]

n = int(input())
start = time.time()
F_n, L_n = fibonacci(n)
end = time.time()

print(f"time: {(end - start) * 1000} ms")
print(f"answer: {F_n}")