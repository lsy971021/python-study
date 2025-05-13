# Recursion
# liusy088

def factorial_i(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("1! =", factorial_i(1))
print("2! =", factorial_i(2))
print("3! =", factorial_i(3))
print("4! =", factorial_i(4))





def factorial_r(n):
    if n == 1:
        return 1
    else:
        return n * factorial_r(n - 1)

print("recursion: 1! =", factorial_r(1))
print("recursion: 2! =", factorial_r(2))
print("recursion: 3! =", factorial_r(3))
print("recursion: 4! =", factorial_r(4))





def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci:", end=' ')
for i in range(1, 11):
    print(fibonacci(i), end=' ')
print()






def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print("gdc(1220, 516) =", gcd(1220, 516))
print("gdc(192, 270) =", gcd(192, 270))
print("gdc(156, 264) =", gcd(156, 264))