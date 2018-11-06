coeficientes = []
raiz = int(input("Qual a raiz da sua equacao? "))
grau = int(input("Qual o grau da sua equacao? "))
termoI = int(input("Digite o termo independente: "))
msgTermo = "O termo independente é: "+str(termoI)

def inserirCf(novo_coef):
    novo_coef = coeficientes.append(input("Insira o coeficiente: "))
    return novo_coef

def Calc3(coeficiente,n,n1,n2):
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

def Calc4(coeficiente,n,n1,n2):
    for coeficiente in coeficientes[0]:
        c1 = coeficiente
        for coeficiente in coeficientes[1]:
            c2 = coeficiente
            for coeficiente in coeficientes[2]:
                c3 = coeficiente
                for coeficiente in coeficientes[3]:
                    c4 = coeficiente
                    n = (int(c1)*raiz)+int(c2)
                    n1 = (n*raiz)+int(c3)
                    n2 = (n1*raiz)+int(c4)
                    n3 = (n2*raiz)+int(termoI)
            msg = "Seus novos coeficientes sao: "+str(n)+"|"+str(n1)+"|"+str(n2)+"|"+str(n3)
            return msg

def Calc5(coeficiente,n,n1,n2):
    for coeficiente in coeficientes[0]:
        c1 = coeficiente
        for coeficiente in coeficientes[1]:
            c2 = coeficiente
            for coeficiente in coeficientes[2]:
                c3 = coeficiente
                for coeficiente in coeficientes[3]:
                    c4 = coeficiente
                    for coeficiente in coeficientes[4]:
                        c5 = coeficiente
                        n = (int(c1)*raiz)+int(c2)
                        n1 = (n*raiz)+int(c3)
                        n2 = (n1*raiz)+int(c4)
                        n3 = (n2*raiz)+int(c5)
                        n4 = (n3*raiz)+int(termoI)    
                msg = "Seus novos coeficientes sao: "+str(n)+"|"+str(n1)+"|"+str(n2)+"|"+str(n3)+"|"+str(n4)
                return msg

if grau == 3:
    for x in range(0,3):
        inserirCf(coeficientes)
    print("Seus coeficientes são: "+str(coeficientes[0])+"|"+str(coeficientes[1])+"|"+str(coeficientes[2]))
    print(msgTermo)
    print(Calc3(0,0,0,0))

elif grau == 4:
    for x in range(0,4):
        inserirCf(coeficientes)
    print("Seus coeficientes são: "+str(coeficientes[0])+"|"+str(coeficientes[1])+"|"+str(coeficientes[2])
    +"|"+str(coeficientes[3]))
    print(msgTermo)
    print(Calc4(0,0,0,0))

elif grau == 5:
    for x in range(0,5):
        inserirCf(coeficientes)
    print("Seus coeficientes são: "+str(coeficientes[0])+"|"+str(coeficientes[1])+"|"+str(coeficientes[2])+"|"+
    str(coeficientes[3])+"|"+str(coeficientes[4]))
    print(msgTermo)
    print(Calc5(0,0,0,0))
