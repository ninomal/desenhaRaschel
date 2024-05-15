def main():
    carctCheio = "I"
    carctVazio = "-"
    numeroCheio = 0
    numeroVazio = 0
    desenho = ""
    desenhoSoma = 0
    finura = 0
    quantidade = 0
    entrada1 = "continue"
    nova = 0
    paceta = 0
    novadesneho = 1
    finura = 0
    
    
    finura = int(input("Finura: "))
    quantidade = int(input("Quantidade: "))
    while paceta < quantidade:
        while(entrada1 != "n"):
            numeroCheio = int(input("numero cheio"))
            numeroVazio = int(input("numero Vazio"))
            for desenho1 in range(numeroCheio):
                    desenho += carctCheio
            for desenho2 in range(numeroVazio):
                    desenho += carctVazio
            desenhoSoma += (numeroCheio + numeroVazio) 
            entrada1 = input("Continue? ")  
        desenhoSoma += numeroCheio + numeroVazio
        for desenho1 in range(numeroCheio):
                desenho += carctCheio
        for desenho2 in range(numeroVazio):
                desenho += carctVazio
        paceta+=1
    
    finura = finura * 2
    print("Paceta", novadesneho)
    for teste in desenho:
        if nova >= finura :
            print(teste ,end="")
            novadesneho+=1
            print()
            print("Paceta", novadesneho )
            nova = 0
        else:
            print(teste ,end="")
            nova += 1
            
            
             
              
            
    
    
    
    
    
    
    
if __name__ == "__main__":
     main()