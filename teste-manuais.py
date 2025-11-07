import math

valor = int(input("Fale um número: "))
raiz = math.sqrt(valor)

if raiz == int(raiz):
    print("Raiz de ", valor, ":", raiz)
elif raiz != int(raiz):
    print("Essa não é uma raiz exata")

casas_pi = int(input("Quantas casas você quer?: "))
pi = round(math.pi, casas_pi)
print(pi)
#Valor aproximado

n_1 = float(input("Número 1: "))
n_2 = float(input("Número 2: "))

ceil = math.ceil(n_1/n_2)
floor = math.floor(n_1/n_2)

print("ceil:", ceil)
print("floor:", floor)