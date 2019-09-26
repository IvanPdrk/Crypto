
def invers(A,B):
    g = [0 for _ in range(20)]
    u = [0 for _ in range(20)]
    v = [0 for _ in range(20)]
    y = [0 for _ in range(20)]

    g[0]=B
    g[1]=A
    u[0]=1
    u[1]=0
    v[0]=0
    v[1]=1
    y[0]=0
    y[1]=0
    i=1
    while g[i] != 0:
        div=int(g[i-1]/g[i])
        y[i+1]=div
        g[i+1]=g[i-1] - y[i+1] * g[i]
        u[i+1]=u[i-1] - y[i+1] * u[i]
        v[i+1]=v[i-1] - y[i+1] * v[i]
        i+=1
    if v[i-1] < 0:
        v[i-1]=v[i-1] + B
    x=v[i-1]
    return x

A=input("Ingresa primer digito: ")
B=input("Ingresa segundo digito: ")
print(invers(int(A),int(B)))

