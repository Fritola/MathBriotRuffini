coeficientes = []
raiz = int(input("Qual a raiz da sua equacao? "))
grau = int(input("Qual o grau da sua equacao? "))
termoI = int(input("Digite o termo independente: "))
msgTermo = "O termo independente é: "+str(termoI)
n = 0; n1= 0; n2= 0; n3= 0; n4= 0

def inserirCf(novo_coef):#função para incluir coeficientes no array vazio
    novo_coef = input("Insira o coeficiente: ")
    coeficientes.append(novo_coef)
    return novo_coef

def repGrau(grau):#função para repetir o processo de inclusão de acordo com o grau inserido
    for grau in range(0,grau):
        inserirCf(coeficientes)

def valCtest():
    c1 = coeficientes[0]
    c2 = coeficientes[1]
    c3 = coeficientes[2]
    global n ;global n1 ;global n2 ;global n3 ;global n4 ;global raiz ;global termoI
    if grau == 3:
        n = (int(c1)*raiz)+int(c2)
        n1 = (n*raiz)+int(c3)
        n2 = (n1*raiz)+int(termoI) 
    elif grau == 4:
        c4 = coeficientes[3]
        n = (int(c1)*raiz)+int(c2)
        n1 = (n*raiz)+int(c3)
        n2 = (n1*raiz)+int(c4)
        n3 = (n2*raiz)+int(termoI)        
    elif grau == 5:
        c4 = coeficientes[3]
        c5 = coeficientes[4]
        n = (int(c1)*raiz)+int(c2)
        n1 = (n*raiz)+int(c3)
        n2 = (n1*raiz)+int(c4)
        n3 = (n2*raiz)+int(c5)
        n4 = (n3*raiz)+int(termoI)   
        
def Calc3(coeficiente,n,n1,n2):#função para calcular os novos coeficientes
    valC(coeficiente,n,n1,n2)
    msg = "Seus novos coeficientes sao: " +str(n)+"|"+str(n1)+"|"+str(n2)
    return msg

def Calc4(coeficiente,n,n1,n2,n3):# = Calc3
    valC(coeficiente,n,n1,n2,n3)
    msg = "Seus novos coeficientes sao: "+str(n)+"|"+str(n1)+"|"+str(n2)+"|"+str(n3)
    return msg

def Calc5(coeficiente,n,n1,n2,n3,n4):# = Calc4
    valC(coeficiente,n,n1,n2,n3,n4)
    msg = "Seus novos coeficientes sao: "+str(n)+"|"+str(n1)+"|"+str(n2)+"|"+str(n3)+"|"+str(n4)
    return msg

if grau == 3:
    repGrau(grau)#chamando a função e passando o argumento 'grau'
    print("Seus coeficientes são: "+str(coeficientes[0])+"|"+str(coeficientes[1])+"|"+str(coeficientes[2]))
    print(msgTermo)
    valCtest()
    print([n,n1,n2])

elif grau == 4:
    repGrau(grau)
    print("Seus coeficientes são: "+str(coeficientes[0])+"|"+str(coeficientes[1])+"|"+str(coeficientes[2])
    +"|"+str(coeficientes[3]))
    valCtest()
    print([n,n1,n2,n3])

elif grau == 5:
    repGrau(grau)
    print("Seus coeficientes são: "+str(coeficientes[0])+"|"+str(coeficientes[1])+"|"+str(coeficientes[2])+"|"+
    str(coeficientes[3])+"|"+str(coeficientes[4]))
    valCtest()
    print([n,n1,n2,n3,n4])