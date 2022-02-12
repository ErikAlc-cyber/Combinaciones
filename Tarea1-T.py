import math
import random
import matplotlib.pyplot as plt
import os
from os import remove

class Combinacion:
    def __init__(self, combinacion, numero_de_1, largo):
        self.numero = combinacion
        self.numero_de_1 = numero_de_1
        self.largo = largo
 
def contador(numero):
    unos = 0
    for i in numero:
        unos += int(i)
    return unos
 
def bina(decimal):
        
    binario = 0
    mult = 1

    while decimal != 0:
        binario = binario + decimal % 2 * mult
        decimal //= 2
        mult *= 10
    
    strbinario = str(binario)
    unos = contador(strbinario)
    
    return Combinacion(binario, unos, len(strbinario))

def llenas_array(in_file):
    
    array = []
    
    while True:
        file_line = in_file.readline()
        if not file_line:
            in_file.close()
            break
        array.append(file_line.strip('\n'))
    
    return array

def primo(numero):
    if numero == 4:
        return False
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True

def ingerir():
    cadenas = llenas_array(open("combinaciones.txt", "r"))
    out_file = open("resultados.txt", "w")
    out_file.write("L{e")
    
    for i in cadenas:
        out_file.write(", "+str(i))
    
    out_file.write("}\n")
    del cadenas
    cadenas = llenas_array(open("unos.txt", "r"))
    out_file.write("#1's{e")
    
    for i in cadenas:
        out_file.write(", "+str(i))
    
    out_file.write("}\n")
    del cadenas
    cadenas = llenas_array(open("largo.txt", "r"))
    out_file.write("# de Digitos{e")
    
    for i in cadenas:
        out_file.write(", "+str(i))
    
    out_file.write("}\n")
    del cadenas
    out_file.close() 
    
    remove("combinaciones.txt")
    remove("largo.txt")
    remove("unos.txt")

if __name__ == "__main__":
    while True:
        print("1) Realizar un nuevo calculo del universo")
        print("2) Salir")
        opc = int(input("Seleccione una opcion: "))
        
        if opc == 1:
            print("\n")
            print("1) Modo manual: ")
            print("2) Modo automatico: ")
            aux = int(input("Seleccione una opcion: "))
            
            if aux == 1:
                n = int(input("\nIntroduce n, no mayor a 1000 ni menor a 0: "))
                if 1000 < n < 0:
                    print("Error, el numero introducido no es valido")
                    break
            
            elif aux ==2:
                n = random.randrange(0,1000)
            
            else:
                print("Error, seleccione una opcion correcta")
                break
            
            check = True
            count = 1
            
            filec = open("combinaciones.txt", "w")
            fileu = open("unos.txt", "w")
            filel = open("largo.txt", "w")
            filep = open("primos.txt", "w")
            
            while check:
                try:
                    cadena = bina(count)
                    if(primo(count)):
                        filep.write(str(cadena.numero)+"--"+ str(count)+" \n")
                    filec.write(str(cadena.numero)+"\n")
                    fileu.write(str(cadena.numero_de_1)+"\n")
                    filel.write(str(cadena.largo)+"\n")
                    count += 1
                    check = cadena.numero_de_1 != n
                    del cadena
                    
                except BufferError:
                    filec.close()
                    fileu.close()
                    filel.close()
                    filep.close()
                    exit()
                    
                except KeyboardInterrupt:
                    break

            filec.close()
            fileu.close()
            filel.close()
            filep.close()
            del aux
            del opc
            del n
            del count
            ingerir()
            
            
        elif opc == 2:
            exit()
        
        else:
            print("Error, seleccione una opcion correcta\n")