import pandas as pd
from pandas.core.frame import DataFrame
import xlsxwriter as xl
import time
import os

from xlsxwriter.worksheet import Worksheet

#BORRAR PANTALLA EN CUALQUIER SISTEMA
if os.name=="prosix" or os.name=="mac":
    borrar= "clear"
elif os.name== "ce" or os.name== "nt" or os.name== "dos":
    borrar="cls"

#dic
base_datos={
    '1': {
           'Nombre completo':'Juan Pablo Suarez Ramirez',
           'Cedula':'1004734004',
           'Edad':'21',
           'Gastos': 100000,
           'Ingresos': 350000
}       }      

#MENU   
def menu():
    print("-- MENU LISTA --")
    print("1. Añadir nuevo miembro")
    print("2. Consultar lista")
    print("3. Actualizar datos")
    print("______________________________")
    print("4. Crear o actualizar excel")
    print("5. Salir")

#HACER ENCUESTA
def validarCodigo_existente(codigo):
    llaves = list(base_datos.keys()) #convierte a lista y busca el codigo como llave
    if codigo in llaves :   #si codigo esta en llaves 
        return False    #el codigo ya es creado
    else:
        return True     #no esta creado

#2. Consultar lista
def consultar_code():
    print("------------------------------------")
    if len(base_datos)==0:
        print("No hay ningun miembro guardado")
        input("digite 0 para continuar")
    else:
        for lista in base_datos:
            print(f"El miembro con codigo {lista} es:")
            print(f"Nombre completo: {base_datos[lista]['Nombre completo']}")
            print(f"Cedula: {base_datos[lista]['Cedula']}")
            print(f"Edad: {base_datos[lista]['Edad']}")
            print(f"Ingresos  mes: {base_datos[lista]['Ingresos']}")
            print(f"Gastos mes: {base_datos[lista]['Gastos']}")
            input("digite 0 para continuar")
    print("------------------------------------")


#1. añadir nuevo miembro
def añadir_code():
    print("Digite la nueva informacion.")
    codigo = input(      "Porfavor digite el codigo a asignar al nuevo miembro: "      ) 
    if validarCodigo_existente(codigo) :
       nombre_full = input(      "Porfavor digite su nombre completo : "      ) 
       Cedula_dig = input(      "Porfavor digite su numero de cedula : "      )
       Edad_dig = input("Porfavor digite su edad : ")  
       Ingreso_dig = input("Porfavor digite los gastos mensuales : ")  
       gastos_dig = input("Porfavor digite los ingresos mensuales : ")  
       
       base_datos.update(
            {
                codigo: {
                    'Nombre completo':nombre_full,
                    'Cedula': Cedula_dig,
                    'Edad': Edad_dig,
                    'Gastos': gastos_dig,
                    'Ingresos': Ingreso_dig
                    }
            }
        )
        
       print('El nuevo miembro fue asignado correctamente.')
       time.sleep(2)
    else:
        print('El codigo ya existe en la lista, intente otro por favor.') 
        time.sleep(2)
        consultar_code()




#3. Actualizar
def actualizar_lista():
    print("Digite la informacion para actualizar la lista.")
    codigo = input("Porfavor Digite el codigo del miembro a actualizar: ")
    if validarCodigo_existente(codigo): 
        print('El codigo no existe en la lista, por favor revise la base creada.')
        time.sleep(4)
        print('Los miembros actualmente guardados en la lista son:')
        time.sleep(4)
        consultar_code()
        
    else:
        nombre_full = input("Porfavor Digite el nombre completo del miembro a actualizar: "      )
        cedula = input(      "Porfavor Digite la cedula del miembro a actualizar: "      )
        edad = int(    input("Porfavor Digite la edad del miembro a actualizar: ")   ) 
        Ingreso_dig = input("Porfavor digite los gastos mensuales a actualizar : ")  
        gastos_dig = input("Porfavor digite los ingresos mensuales a actualizar: ") 
        base_datos.update(
            { 
                codigo :{
                            'Nombre completo' : nombre_full,
                            'Cedula' : cedula,
                            'Edad' : edad,
                            'Gastos': gastos_dig,
                            'Ingresos': Ingreso_dig
                        }
            }
        )
        print('La lista fue actualizada correctamente.')
        time.sleep(4)


def excel():
    #convertir a dataframe    
    datosDataFrame = pd.DataFrame(base_datos)
    print(datosDataFrame)

    

      
    #GUARDAD EN DISCO DURO COMO EXCEL
    acum =1
    workbook = xl.Workbook('ARCHIVOS/Tabulación_encuesta_presupuesto.xlsx')
    bold = workbook.add_format({'bold': True})
    for i in range(0, len(base_datos)):
        
        worksheet = workbook.add_worksheet(base_datos[str(acum)]['Nombre completo'])
        headings = ['Nombre completo', 'Cedula', 'Edad', 'Ingresos', 'Gastos'] 
        #Items
        worksheet.write(0, 0, headings[0])
        worksheet.write(0, 1, headings[1])
        worksheet.write(0, 2, headings[2])
        worksheet.write(0, 3, headings[3])
        worksheet.write(0, 4, headings[4])   
        #Datos
        worksheet.write(1, 0, base_datos[str(acum)]['Nombre completo'])
        worksheet.write(1, 1, base_datos[str(acum)]['Cedula'])
        worksheet.write(1, 2, base_datos[str(acum)]['Edad'])
        worksheet.write(1, 3, base_datos[str(acum)]['Ingresos'])
        worksheet.write(1, 4, base_datos[str(acum)]['Gastos'])
        acum += 1  

 
    workbook.close ()

#INTERFAZ   

print("base de datos de Encuesta") 
opcion1=0         
while opcion1 != '5' :
    print(len(base_datos))
    menu()
    opcion1 = input(      'Digite la opcion por favor: '     )
    if opcion1 == '2' :
        consultar_code()
        os.system(borrar)
    elif opcion1 == '1' :
        añadir_code()
        os.system(borrar)
    elif opcion1 == '4' :
        excel()
    elif opcion1 == '3' :
        actualizar_lista()
        os.system(borrar)
print('Gracias por usar nuestro programa.')
time.sleep(5)
os.system(borrar)


    


       
        

