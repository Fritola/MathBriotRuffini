coeficientes = []
# n e seus derivados sao os novos coeficientes

print("BRIOT RUFFINI - CÁLCULO DE COEFICIENTES")
while True:
    try:
        raiz = int(input("|Qual a raíz da sua equação? "))
        grau = int(input("|Qual o grau da sua equação? "))

        if grau == 3:
            for x in range(0, 3):
                novo_coef = coeficientes.append(input("|Insira o coeficiente "))
            print("\n|")

            for i, item in enumerate(coeficientes, start=1):
                print("|Coeficiente "+str(i)+": "+item)
            termoI = input("|Digite o termo independente ")

            for coeficiente in coeficientes[0]:
                c1 = coeficiente
                for coeficiente in coeficientes[1]:
                    c2 = coeficiente
                    for coeficiente in coeficientes[2]:
                        c3 = coeficiente
                        n = (int(c1)*raiz)+int(c2)
                        n1 = (n*raiz)+int(c3)
                        n2 = (n1*raiz)+int(termoI)
                    print("Seus novos coeficientes sao: " +
                          str(n)+"|"+str(n1)+"|"+str(n2))
            break

        elif grau == 4:
            for x in range(0, 4):
                novo_coef = coeficientes.append(input("|Insira o coeficiente "))
            print("\n")

            for i, item in enumerate(coeficientes, start=1):
                print("|Coeficiente "+str(i)+": "+item)
            termoI = input("|Digite o termo independente ")

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
                    print("|Seus novos coeficientes sao: "+str(n) +
                          "|"+str(n1)+"|"+str(n2)+"|"+str(n3))
            break

        elif grau == 5:
            for x in range(0, 5):
                novo_coef = coeficientes.append(input("|Insira o coeficiente "))
            print("\n|")

            for i, item in enumerate(coeficientes, start=1):
                print("|Coeficiente "+str(i)+": "+item)
            termoI = input("|Digite o termo independente ")

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
                    print("|Seus novos coeficientes sao: "+str(n)+" " +
                          str(n1)+"|"+str(n2)+"|"+str(n3)+"|"+str(n4))
            break

        elif grau >= 6:       
            print("Valor não aceito, digite um valor de 3 a 5")     
    except ValueError:
        print("ERRO VALOR NAO ENCONTRADO")
        
