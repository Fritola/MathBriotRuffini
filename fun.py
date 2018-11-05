coeficientes = []

raiz = int(input("Qual a raiz da sua equacao? "))
grau = int(input("Qual o grau da sua equacao? "))
termoI = int(input("Digite o termo independente: "))

def inserirCf(novo_coef):
    novo_coef = coeficientes.append(input("Insira o coeficiente: "))
    return novo_coef

def calcNovo(coeficiente,n,n1,n2):
    for coeficiente in coeficientes[0]:
        c1 = coeficiente
        for coeficiente in coeficientes[1]:
                c2 = coeficiente
                for coeficiente in coeficientes[2]:
                    c3 = coeficiente
                    n = (int(c1)*raiz)+int(c2)
                    n1 = (n*raiz)+int(c3)
                    n2 = (n1*raiz)+int(termoI)    
    msg = "Seus novos coeficientes sao: " +str(n)+"|"+str(n1)+"|"+str(n2)
    return msg

if grau == 3:
    for x in range(0,3):
        inserirCf(coeficientes)
    print(coeficientes)
    print(termoI)
    print(calcNovo(0,0,0,0))

elif grau == 4:
    for x in range(0,4):
        inserirCf(coeficientes)
    print(coeficientes)
    print(termoI)

elif grau == 5:
    for x in range(0,5):
        inserirCf(coeficientes)
    print(coeficientes)
    print(termoI)

