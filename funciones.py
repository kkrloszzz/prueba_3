import os, time, csv
ruts = []
nombres = [] 
direcciones = []
comunas = []
cilindros = ['5','15']
elecciones=[]
totales = []
cantidades = []
previocsv = ['Santiago','Colina','Pirque']



def opc1():
    os.system('cls')
    print("REGISTRAR PEDIDO")
    time.sleep(2)
    while True:
        try:
            rut = int(input("Ingrese su RUT: "))
            break
        except:
            print("ERROR! CARÁCTER INVÁLIDO")


    nombre = input("Ingrese su nombre: ")
    direccion = input("Ingrese su dirección: ")
    comuna = input("Ingrese su comuna: ")
    print("¿Que cilindro desea llevar?")
    print(cilindros)
    while True:
        try:
            cilindro = int(input("Elija el cilindro (1,2): "))
            if cilindro in (1,2): 
                cantidad = int(input("¿Cuántos Cilindros desea?: "))        
                if cilindro == 1:
                    total = cantidad*12500
                    print("DATOS GUARDADOS CORRECTAMENTE!")
                    time.sleep(2)
                    print(f"Su total es de {total}")
                    time.sleep(2)
                    os.system('cls')
                    break
                    
                else:
                    total = cantidad*25500
                    print("DATOS GUARDADOS CORRECTAMENTE!")
                    time.sleep(2)
                    print(f"Su total es de {total}")
                    time.sleep(2)  
                    os.system('cls')            
                    break
                
            else:
                os.system('cls')
                print("ERROR! OPCIÓN INVÁLIDA")
                time.sleep(2)
        except:
            os.system('cls') 
            print("ERROR! OPCIÓN INVÁLIDA")
        

    nombres.append(nombre)
    ruts.append(rut)
    direcciones.append(direccion)
    comunas.append(comuna)
    elecciones.append(cilindro)
    cantidades.append(cantidad)
    totales.append(total)



def opc2():
    os.system('cls')
    print("Listar todos los Pedidos")
    time.sleep(2)
    for x in range (len(nombres)):
        print(f"Nombre: {nombres[x]}")
        print(f"RUT: {ruts[x]}")
        print(f"Dirección: {direcciones[x]}")
        print(f"Comuna: {comunas[x]}")
        print(f"CILINDROS: {cantidades[x]}")
        print(f"Total a pagar: {totales[x]}")
        print("")
        
        time.sleep(3)


def opc3():
    os.system('cls')
    print("BUSCAR PEDIDO POR RUT")
    rut_buscar= input("Ingrese el rut a buscar: ")
    if len(rut_buscar) == len(ruts):
        print(f"Nombre: {nombres[ruts.index()]} ")
        print(f"RUT: {ruts[ruts.index()]}")
        print(f"Dirección: {direcciones[ruts.index()]}")
        print(f"Comuna: {comunas[ruts.index()]}")
        print(f"CILINDROS: {cantidades[ruts.index()]}")
        print(f"Total a pagar: {totales[ruts.index()]}")
        
    else:
        print("No se ha encontrado rut!")
        time.sleep(2)






def opc4():
    os.system('cls')
    print("IMPRIMIR HOJA POR RUTA")
    time.sleep(2)
    while True:
        print("Elija su comuna de preferencia ")
        print(previocsv)
        try:
            opcion =int(input("\n¿Cual desea elegir?: "))-1
            if opcion in(0,1,2):
                break
            else:
                print("ERROR! INDIQUE LA COMUNA QUE DESEE")
                time.sleep(2)
        except:
            print("ERROR! OPCIÓN INVÁLIDA ")
            time.sleep(2)

    nombre_archivo = input("Ingrese un nombre para su archvio: ")+".csv"
    
    with open(nombre_archivo,"w",newline="") as archivo:
        escritor = csv.writer(archivo) 
        

  
