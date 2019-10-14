

def Aexp(x,b,n):
	z=1
	Az=[]
	for i in range(len(b)):
		if(b[i]=='0'):
			z=((z*z)%n)

		if(b[i]=='1'):
			z=(((z*z)*x)%n)
		Az.append(z)
	return(Az)

def tabla(b,Az):
	i=len(b)-1

	print('{:^10}{:^10}{:^10}'.format("i","bi","z"))
	for j in range(len(b)):
		print('{:^10}{:^10}{:^10}'.format(i,b[j],Az[j]))
		i-=1

x=int(input("Dame el valor de x: "))
b=int(input("Dame el valor de b: "))
b=str(bin(b))
b=b[2:]
n=int(input("Dame el valor de n: "))

Az=Aexp(x,b,n)
tabla(b,Az)
print("el resultado es",Az[len(Az)-1])


