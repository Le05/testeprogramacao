qtdarray = input("Digite o tamanho do array(o valor minimo é 1 e maximo de 1000)")
valor = 0
listaNumeros = []
if int(qtdarray) > 1000 or int(qtdarray) < 1:
    print("valor invalido")
else:
    while  valor < int(qtdarray):
        numeroIgual = False
        valor = valor+1
        numero = input("Digite o numero(o valor minimo é -1000 e maximo de 1000)")
        if int(numero) < -1000 or int(numero) > 1000:
            print("valor invalido")
        else:
            if listaNumeros != []:
                for numerolist in listaNumeros:
                    if numerolist == int(numero):
                        numeroIgual = True
            

            if numeroIgual == False:
                listaNumeros.append(int(numero))
    listaNumeros.sort()
    print(listaNumeros)