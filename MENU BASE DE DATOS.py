import time
import os

if os.name=="prosix" or os.name=="mac":
    borrar= "clear"
elif os.name== "ce" or os.name== "nt" or os.name== "dos":
    borrar="cls"
#Aplicacion CRUD - LISTA DE TAREAS PENDIENTES
#Dicionario
base_datos={
    '1': {
           'Nombre completo':'Juan Pablo Suarez Ramirez',
           'Cedula':'1004734004',
           'Edad':'21'
}       }        

#funcion menu
def menu():
    print("-- MENU LISTA --")
    print("1. Añadir nuevo miembro")
    print("2. Consultar lista")
    print("3. Actualizar lista")
    print("4. Eliminar miembro")
    print("5. Salir")

#validar si ya existe
def validarCodigo_existente(codigo):
    llaves = list(base_datos.keys()) #convierte a lista y busca el codigo como llave
    if codigo in llaves :   #si codigo esta en llaves 
        return False    #el codigo ya es creado
    else:
        return True     #no esta creado

#1. añadir nuevo miembro
def añadir_code():
    print("Ingrese la nueva informacion.")
    codigo = input(      "Porfavor ingresar el codigo a asignar al nuevo miembro: "      ) 
    if validarCodigo_existente(codigo) :
        nombre_full = input(      "Porfavor ingresar el nombre completo del nuevo miembro: "      ) 
        cedula = input(      "Porfavor ingresar la cedula del nuevo miembro: "      )
        edad = input("Porfavor ingrese la edad del nuevo miembro: ")   
        base_datos.update (
            {
                codigo: {
                    'Nombre completo':nombre_full,
                    'Cedula': cedula,
                    'Edad': edad

                }
            }
        )
        print('El nuevo miembro fue asignado correctamente.')
        time.sleep(4)
    else:
        print('El codigo ya existe en la lista, intente otro por favor.') 
        time.sleep(4)
        consultar_lista()

#2. Consultar lista
def consultar_lista():
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
            input("digite 0 para continuar")
    print("------------------------------------")

#3. Actualizar
def actualizar_lista():
    print("Ingrese la informacion para actualizar la lista.")
    codigo = input("Porfavor ingresar el codigo del miembro a actualizar: ")
    if validarCodigo_existente(codigo): 
        print('El codigo no existe en la lista, por favor revise las tareas que actualmente estan creadas.')
        time.sleep(4)
        print('Los miembros actualmente guardados en la lista son:')
        time.sleep(4)
        consultar_lista()
        
    else:
        nombre_full = input("Porfavor ingrese el nombre completo del miembro a actualizar: "      )
        cedula = input(      "Porfavor ingrese la cedula del miembro a actualizar: "      )
        edad = int(    input("Porfavor ingrese la edad del miembro a actualizar: ")   ) 
        base_datos.update(
            { 
                codigo :{
                            'Nombre completo' : nombre_full,
                            'Cedula' : cedula,
                            'Edad' : edad
                        }
            }
        )
        print('La lista fue actualizada correctamente.')
        time.sleep(4)

#ELIMINAR OPERACION
def eliminar_miembro(codigo_miembro): 
    try: 
        base_datos.pop(codigo_miembro)
        return True
    except:
        return False
    
#4. ELIMINAR 
def eliminar():
    print('A continuacion digite el codigo de la lista a eliminar (codigo): ')
    consultar_lista()
    codigomiembro = (input('Porfavor ingresar el codigo del miembro a elminar: '))
    miembroEliminado = eliminar_miembro(codigomiembro)
    
    if miembroEliminado:
        print(f"El miembro con codigo {codigomiembro} ha sido eliminada correctamente.")
        time.sleep(4)
    else:
        print('El miembro no fue Eliminado, porque el codigo no existe.')
        time.sleep(4)

#parte que se va a mostrar al usuario, todo el menu y las opciones (while)
print("base de datos de un club")
opcion = 0
while opcion != '5' :
    menu()
    opcion = input(      'Ingrese la opcion por favor: '     )
    if opcion == '2' :
        consultar_lista()
        os.system(borrar)
    elif opcion == '4' :
        eliminar()
        os.system(borrar)
    elif opcion == '1' :
        añadir_code()
        os.system(borrar)
    elif opcion == '3' :
        actualizar_lista()
        os.system(borrar)
print('Gracias por usar nuestro programa.')
time.sleep(5)
os.system(borrar)
