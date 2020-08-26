nombres = []
telefonos = []
correos = []
print("***Agenda Telefonica***")
while'true':
    print("1. Añadir contacto.")
    print("2. Eliminar contacto.")
    print("3. Mostrar contactos.")
    print("4. Salir del programa.")
    print()
    opcion = input("-->  ")
    print()
    if opcion == "1":
        contactos= str(input("Introduce contacto:  ").capitalize())
        tel= int(input("Introduce número telefonico:  "))
        email= input("Introduce email:  ").lower()
        if contactos in nombres:
            print("Ese contacto ya está en la lista")      
        else:
            nombres.append(contactos)
            telefonos.append(tel)
            correos.append(email)
    elif opcion == "2":
        contactos= input("Introduce contacto:  ").capitalize()
        tel= int(input("Introduce número telefonico:  "))
        email= input("Introduce email:  ").lower()
        if contactos not in nombres:
            print("Ese nombre no está en la agenda.")
        else:
            nombres.remove(contactos)
            telefonos.remove(tel)
            correos.remove(email)
    elif opcion == "3":
        print("Agenda: ")
        for i, nombres in enumerate(nombres):
            print(nombres, telefonos[i], correos[i])
    elif opcion == "4":
        break
    else:
        print("Introduce una opción correcta.")
