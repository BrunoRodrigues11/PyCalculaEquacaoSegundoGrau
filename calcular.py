# Resolver Equação de 2º Grau
def armazenarValores(a, b, c, d):
    global valores
    global results
    valores = []
    results = []
    valores.append(a)
    valores.append(b)
    valores.append(c)
    valores.append(d)


def printarEquacao(a, b, c, d):
    print("-"*10, "Equação de 2º Grau", "-"*10)
    # B negativo e C positivo
    if (b < 0) and (c > 0):
        print("Equação: {}x² {}x + {} = {}".format(a, b, c, d))
    # B positivo e C negativo
    elif (b > 0) and (c < 0):
        print("Equação: {}x² + {}x {} = {}".format(a, b, c, d))
    # B e C negativos
    elif (b < 0) and (c < 0):
        print("Equação: {}x² {}x {} = {}".format(a, b, c, d))
    # B e C positivos
    else:
        print("Equação: {}x² + {}x + {} = {}".format(a, b, c, d))


def calculaDelta(a, b, c):
   # B negativo e C positivo
    if (b < 0) and (c > 0):
        print("Δ = ({})² - (4 * {} * {})".format(b, a, c))
    # B positivo e C negativo
    elif (b > 0) and (c < 0):
        print("Δ = {}² - (4 * {} * ({}))".format(b, a, c))
    # B e C negativos
    elif (b < 0) and (c < 0):
        print("Δ = ({})² - (4 * {} * ({}))".format(b, a, c))
    # B e C positivos
    else:
        print("Δ = {}² - (4 * {} * {})".format(b, a, c))

    # Calculando o Delta1 -> valor de B elevado ao quadrado
    delta1 = b*b
    # Calculando o Delta2 -> 4 * valor de A * C
    delta2 = 4*a*c
    # Calculando o Delta3 -> valor do delta1 - valor do delta2
    delta3 = delta1-delta2

    # Delta1 negativo e Delta2 positivo
    if (delta1 < 0) and (delta2 > 0):
        print("Δ = ({}) - {}".format(delta1, delta2))
    # Delta1 positivo e Delta2 negativo
    elif(delta1 > 0) and (delta2 < 0):
        print("Δ = {} - ({})".format(delta1, delta2))
    # Delta1 e Delta2 negativos
    elif (delta1 < 0) and (delta2 < 0):
        print("Δ = ({})- ({})".format(delta1, delta2))
    # Delta1 e Delta2 positivos
    else:
        print("Δ = {} - {}" .format(delta1, delta2))

    if delta3 > 0:
        print("Δ = {}".format(delta3))
    else:
        print("Sem raizes reais.")

    # Calculando a razi do delta
    raiz = delta3 ** 0.5
    div = 2 * a

    # Verificando se o valor de B (soma1) é negativo
    if b < 0:
        # Caso B (soma1) for negativo, ele será transformado em positivo
        # Seguindo a fórmula de Bhaskara, X = -b +- √Δ / 2*A
        b = b * -1
        somax2 = b + raiz
        x1 = somax2 / div

        somax3 = b - raiz
        x2 = somax3 / div
    # Verificando se o valor de B (soma1) é positivo
    elif b > 0:
        # Caso B (soma1) for positivo, ele será transformado em negativo
        b = b * -1
        somax2 = b + raiz
        x1 = somax2 / div

        somax3 = b - raiz
        x2 = somax3 / div

    print("Raiz = {}".format(int(raiz)))
    print("")
    print("x = ({}) +- √{} / 2 * {}".format(b, delta3, valores[0]))
    print("x1 = ({}) + {} / {} = {}".format(b, raiz, div, x1))
    print("x2 = ({}) - {} / {} = {}".format(b, raiz, div, x2))
    print("")
    print("-"*10, "Resultado", "-"*10)
    results.append(x1)
    results.append(x2)
    print("S = {}".format(sorted(results)))
    print("")
