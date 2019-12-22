class Menu:

    
    # menu del programa
    def mostrar(self):
        try:
            menu = [
                ['Agenda Personal'],
                ['-------'],
                ['1. Añadir Contacto'],
                ['2. Lista de contactos'],
                ['3. Buscar contacto'],
                ['4. Editar contacto'],
                ['5. Eliminar contacto'],
                ['6. Cerrar agenda']
            ]

            for x in range(len(menu)):
                print(menu[x][0])

            option = int(input("Introduzca la opción deseada: "))
            return self.validarOption(option)

        except ValueError:
            print()
            print('ERROR : Solo esta permitido el ingreso de numero....!!!')
            self.mostrar()

    def validarOption(self, option):
        if option == 6:
            print("Saliendo de la agenda ...")
            exit()
        
        if option >=1  and option <=5:
            return option
            

        # Mensaje de opcion incorrecta y volver a mostrar el menu
        print()
        print("Uhs opcion incorrecta, intente nuevamente")
        self.mostrar()
