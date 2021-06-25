import random
from os import system

## AHORCADO
lis_pal = ["CARROS","CASA","AVION","LAGARTIJA",'ABECEDARIO',"MARMOTA","COLOMBIA","VENTANA"]
pal_usadas = []
progre = []

def run():
    system("cls")
    pal = random.choice(lis_pal)
    for i in range(0, len(pal)):
        progre.append(" _ ")   
    err = 0
    win = False
    while win == False:
        if err >= len(pal):
            win = None
            system("cls")
            print("P E R D I S T E")
            break
        else:
            val = True
            while val == True:
                print(" VAMOS A JUGAR ! \n ADIVINA LA PALABRA: ")
                print(" \n  " + "".join(progre) + " \n")
                let = str(input("ingrese una letra: "))
                if len(let.replace(" ","")) != 1 or let.isdigit():
                    system("cls")
                    print(" Los numero o espacio en blanco no son caracteres validos. \n Intenta nuevamente \n \n")
                else:
                    val = False
            cont = 0 
            for i in range(0, len(pal)):
                if let.upper() == pal[i]:
                    progre[i] = " " + let.upper() + " "
                    cont+= 1
            if cont == 0:
                err+= 1
            if progre.count(" _ ") == 0:
                win = True
            system("cls")
    if win == True:
        print("G A N A S T E")

if __name__ == "__main__":
    run()    