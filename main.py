from phoneBook import PhoneBook
from menu import Menu


dict1={'Don': {'DNI': 14785236, 'Nombre':'daniel','Apellido' :'puicon','Telefono':147,'Correo':'nuevo@gmail.com'}}


list1=[]

list2=[]
# Llamamos al menu interactivo
menu = Menu()
optionMenu = menu.mostrar()

print(f'Estamos recibiendo la {optionMenu}')



#Instanciamos la Clase
#phoneBook = PhoneBook()



def add(dict1):
    print("Agregando nuevo contacto")
  
    nombre= input("Ingrese Nombre:")
    apellido= input("Ingrese apellido:")
    
    telefono= int(input("Ingrese telefono:"), [9])
    email= input("Ingrese EMAIL:")

    dni = int(input("Ingrese DNI:"))
    list1.append(dni)
    list2.append(nombre)
    list2.append(apellido)
    list2.append(telefono)
    list2.append(email)
    list2.append(dni)
    dict1[dni]=nombre, apellido, telefono, email
    print(dict1)
    menu.mostrar
    
def search():
    print("BUSCAR CONTACTO")
    dnibuscar = input("Ingrese DNI: ")
    for dnibuscar in dict1.keys():
        print("Nombre:", dnibuscar, dict1[dnibuscar])
        print()
    
def lista():
    print("Agenda Telefonica:")
    for x in dict1.keys():
        print("Name:", x, dict1[x])
        print()
        
        
if optionMenu == 1 :
    add(dict1)
elif optionMenu == 2:
    lista()
elif optionMenu == 3:
    search()
elif optionMenu == 4:
    print("BUSCAR CONTACTO PARA EDITAR")
    dnibuscar = input("Ingrese DNI: ")
    for dnibuscar in dict1.keys():
        print("Name:", dnibuscar, dict1[dnibuscar])
        
        nombre= input("Ingrese Nombre:")
        apellido= input("Ingrese apellido:")
        telefono= int(input("Ingrese telefono:"))
        email= input("Ingrese EMAIL:")

        list2.append(nombre)
        list2.append(apellido)
        list2.append(telefono)
        list2.append(email)
        list2.append(dnibuscar)
        dict1[dnibuscar]=nombre, apellido, telefono, email
        print(dict1)
        
elif optionMenu == 5:
    print("ELIMINAR CONTACTO")
    dnibuscar = input("Ingrese DNI: ")
    for dnibuscar in dict1.keys():
        del dict1[dnibuscar]['DNI']
        print()