import pandas as pd
import time
import os

from pandas.core.frame import DataFrame

#BORRAR PANTALLA EN CUALQUIER SISTEMA
if os.name=="prosix" or os.name=="mac":
    borrar= "clear"
elif os.name== "ce" or os.name== "nt" or os.name== "dos":
    borrar="cls"

#lista
Nombres=[]
Edad=[]
Cedula=[]
presupuesto = []
Lista_datos= [Nombres, Cedula, Edad]

#MENU   
def menu():
    print("-- MENU LISTA --")
    print("1. Añadir nuevo miembro")
    print("2. Consultar lista")
    print("3. Crear o actualizar excel")
    print("4. Salir")

#HACER ENCUESTA
def añadir_code():
    print("Ingrese la informacion Requerida.")
    nombre_full = input(      "Porfavor ingresar su nombre completo : "      ) 
    Cedula_dig = input(      "Porfavor ingresar su numero de cedula : "      )
    Edad_dig = input("Porfavor ingrese su edad : ")  
    Nombres.append(nombre_full)
    Cedula.append(Cedula_dig) 
    Edad.append(Edad_dig)
    print("Su formulario ha sido guardado")
    consultar_code()
    

#MOSTRAR LISTA
def consultar_code():
    print(Lista_datos)
    input("Ingrese enter para continuar")

def excel():
    #convertir a dataframe    
    datosDataFrame = pd.DataFrame(Lista_datos)
    print(datosDataFrame)

    #GUARDAD EN DISCO DURO COMO EXCEL
    datosDataFrame.to_excel('ARCHIVOS/Tabulación_encuesta.xlsx', sheet_name='Nombres')

    #LEER EXCEL
    datosDataFrame=pd.read_excel(
    'ARCHIVOS/Tabulación_encuesta.xlsx', 
    sheet_name='Nombres',
    header = None,
    skiprows= 1,
    names=[ 'Nombre completo', 'Cedula', 'Edad'],
    )


#INTERFAZ   
print("base de datos de Encuesta") 
opcion1=0         
while opcion1 != '4' :
    menu()
    opcion1 = input(      'Ingrese la opcion1 por favor: '     )
    if opcion1 == '2' :
         consultar_code()
         os.system(borrar)
    elif opcion1 == '1' :
         añadir_code()
         os.system(borrar)
    elif opcion1 == '3' :
         excel()
print('Gracias por usar nuestro programa.')
time.sleep(5)
os.system(borrar)


    


       
        

