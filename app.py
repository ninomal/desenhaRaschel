"""Copie o codigo clicando em copy raw file a cima ^
    Instale o programa pycharm no celular ou qualquer leitor de python
    cole o codigo dentro do programa e só clicar em iniciar
                                                    """

def main():
    CARCTCHEIO = "I"
    CARCTVAZIO = "-"
    numeroCheio = 0
    numeroVazio = 0
    desenho = ""
    desenhoSoma = 0
    finura = 0
    quantidade = 0
    entrada1 = "continue"
    paceta = 0
    nova = 1
    novaDesenho = 0
    finura = 0
    pacetasDesenhoList = []
    pacetasVaziasVect = []
    count = 0
    pacetasDesenho = ""
    pacetasIguaisCount = []
    pacetasSequencia = 0
    pacetasIguiasFor = 0
    countWhile1= 0
    countWhile2 =0
    pacetasCheck = True
    pacetasVaziaStr = ""
    pacetasVaziasCount = 1
    pacetasCount = 0
    pacetasRepetir = 1
    pontasVazias = 0
    pacetasNumber = 0
    pacetasCountSequence = 1
    pacetasComPontasList = []
    finurasPosivel = [9 ,12 ,14 ,18 ,24]
    finuraOk = True
    
    while True:
        try:
            finura = int(input("Finura: "))
            break
        except ValueError:
            print("Não permetidas Letras")
    
    while finuraOk:
        if finura in finurasPosivel:
            finuraOk = False
        else:
            print(f"Finura {finura} não existe: " )
            print("Digite a finura certa: ")
            finura = 0
            finura = int(input("Finura: "))
    
    while True:
        try:
            quantidade = int(input("Quantidade: "))
            break
        except ValueError :
            print("Não permetido letras")
            
    while True:
        try:
            numeroVazio = int(input("numero Vazio: "))
            break
        except ValueError :
            print("Não permetido letras")
        
    #desenho
    for desenho2 in range(numeroVazio): 
        desenho += CARCTVAZIO
    while paceta < quantidade:
        while(entrada1 != "n"):
            while True :
                try:
                    numeroCheio = int(input("numero cheio: "))
                    break
                except ValueError :
                    print("Não permetido letras")
            while True :
                try:
                    numeroVazio = int(input("numero Vazio: "))
                    break
                except ValueError :
                    print("Não permetido letras")
            for desenho1 in range(numeroCheio):
                    desenho += CARCTCHEIO
            for desenho2 in range(numeroVazio):
                    desenho += CARCTVAZIO
            desenhoSoma += (numeroCheio + numeroVazio) 
            entrada1 = input("Continue? digite n para sair: ")  
            desenhoSoma += numeroCheio + numeroVazio
        for desenho1 in range(numeroCheio):
                desenho += CARCTCHEIO
        for desenho2 in range(numeroVazio):
                desenho += CARCTVAZIO
        desenhoSoma += numeroCheio + numeroVazio
        paceta+=1 
    
    print(" chumbo ------------->")
    print("<--- começo   fim --->")
    finura = finura * 2
    print("Paceta", novaDesenho)
    for pontas in desenho:
        if nova >= finura :
            print(pontas ,end="")
            novaDesenho +=1
            print()
            print("Paceta", novaDesenho )
            pacetasDesenho += pontas
            pacetasDesenhoList.append(pacetasDesenho)
            pacetasDesenho = ""
            nova = 1
        else:
            print(pontas ,end="")
            nova += 1
            pacetasDesenho += pontas
    
    #void pacetas eraser
    for pontasVazias in range(finura):
        pacetasVaziaStr += "-" 
    print()
    print("Pacetas com pontas")   
    for pacetasCount in pacetasDesenhoList:
        if pacetasCount == pacetasVaziaStr:
            continue
        else:
            print("Paceta: ", pacetasVaziasCount)
            print(pacetasCount)
            pacetasVaziasCount += 1
            pacetasComPontasList.append(pacetasCount)
        
    #sequence count
    while(pacetasCheck):
        while(pacetasCheck):
            pacetasRepetir +=1
            if pacetasSequencia >= 3:
                pacetasCheck = False
            elif countWhile2  >= len(pacetasDesenho):
                countWhile1 += 1
                countWhile2 = 0
            elif countWhile1  >= len(pacetasDesenho):
                pacetasCheck = False
            elif pacetasDesenho[countWhile1] == pacetasDesenho[countWhile2]:
                pacetasSequencia += 1
                countWhile2+=1
            countWhile2+=1
   
    #numero de repetiçoes
    pacetasListsSlice = pacetasComPontasList[:pacetasRepetir]
    for pacetasSemRepetir in pacetasListsSlice:
        pacetasNumber +=1
        pacetasCountSequence = 1
        for pacetasRepetidasFor in pacetasComPontasList:
            if(pacetasRepetidasFor == pacetasSemRepetir):
                pacetasCountSequence += 1
        print("Paceta: ", pacetasNumber, pacetasCountSequence)
                        
    #check void point             
    for pacetasVect in range(finura):
        pacetasVaziasVect.append('-')
    for pacetasLists in pacetasDesenhoList:
        count = 0
        for vazio in pacetasLists:
            if vazio == "I":         
                pacetasVaziasVect[count] = "I"
            count +=1
            if count >= (finura -1):
                count = 0
                         
    print()
    print("Pacetas para colocar gesso ==")
    print(pacetasVaziasVect)
    
                        
    
   
    
if __name__ == "__main__":
     main()