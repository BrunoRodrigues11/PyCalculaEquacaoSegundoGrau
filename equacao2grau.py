# Resolver Equação de 2º Grau
from calcular import *

print("-"*10, "Entrada de Dados", "-"*10)
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))
d = float(input("Informe o valor de d: "))

armazenarValores(a, b, c, d)
printarEquacao(a, b, c, d)
calculaDelta(a, b, c)
