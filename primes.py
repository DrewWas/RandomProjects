def is_prime(n):
    if n == 0 or n == 1 or n == 2:
        return "Prime"
    for i in range(3, n):
        if n % i == 0:
            return False
    else:
        return True


def f(x):
    return (x*x) + x + 41

q = 0
while is_prime(f(q)):
    print(q, f(q))
    q += 1

print("On f(", q, ") ", f(q), " is no longer prime")
