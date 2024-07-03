
from funciones import *



os.system('cls')

print("Bienvenido a GAXPLOSIVE")
time.sleep(1)

while True:
    print("\n1. Registrar Pedido")
    print("2. Listar todos los Pedidos")
    print("3. Buscar Pedido Por Rut")
    print("4. Imprimir hoja de ruta")
    print("5. Salir")
    
    opc=int(input("\nElija una opción: "))
      

    if opc==1:
       opc1()

    elif opc==2:
        opc2()


    elif opc==3:
        opc3()

    elif opc==4:
        opc4()


    elif opc==5:
        os.system('cls')
        print("GRACIAS POR USARNOS")
        time.sleep(2)
        break

  