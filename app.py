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
    nova = 0
    novaDesenho = 0
    finura = 0
    pacetasVaziasList = []
    pacetasVaziasVect = []
    count = 0
    pacetasDesenho = ""
    pacetasVaziasVect= ""
    
    
    finura = int(input("Finura: "))
    quantidade = int(input("Quantidade: "))
    numeroVazio = int(input("numero Vazio: "))
    for desenho2 in range(numeroVazio):
                    desenho += CARCTVAZIO
    while paceta < quantidade:
        while(entrada1 != "n"):
            numeroCheio = int(input("numero cheio: "))
            numeroVazio = int(input("numero Vazio: "))
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

    finura = finura * 2
    print("Paceta", novaDesenho)
    for pontas in desenho:
        if nova >= finura :
            print(pontas ,end="")
            novaDesenho +=1
            print()
            print("Paceta", novaDesenho )
            pacetasDesenho += pontas
            pacetasVaziasList.append(pacetasDesenho)
            nova = 0
        else:
            print(pontas ,end="")
            nova += 1
            pacetasDesenho += pontas
    
    
    for pacetasVect in range(finura - 1):
        pacetasVaziasVect.append('-')
    for pacetasList in pacetasVaziasList:
        count = 0
        for vazio in pacetasList:
            if vazio == "I":         
                pacetasVaziasVect[count] = "I"
            count +=1
            if count >= (finura -1):
                count = 0
         
    
    print()
    print("Pacetas Vazias ==")
    print(pacetasVaziasVect)
    
                        
    
    
            
            
             
              
            
    
    
    
   
    
    
if __name__ == "__main__":
     main()