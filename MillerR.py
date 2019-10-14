from random import randrange

def isStrongPseudoprime(n, a):
    d, s = n-1, 0
    while d % 2 == 0:
        d, s = d//2, s+1
    t = pow(a,d,n)
    if t == 1:
        return True
    while s > 0:
        if t == n - 1:
            return True
        t, s = pow(t, 2, n), s - 1
    return False

def isPrime(n, k):
    if n % 2 == 0:
        return n == 2
    for i in range(1, k):
        a = int(randrange(2, n))
        if not isStrongPseudoprime(n, a):
            return False
    return True


n=int(input("Escriba un numero a verificar: "))
k=int(input("Escriba el numero de rondas: "))
print(isPrime(n,k))