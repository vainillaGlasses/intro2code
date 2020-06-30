def guardarTelefono(numeroTelefono):
    assert isinstance(numeroTelefono, int)
    print(numeroTelefono)

# caso 1
telefono1 = int(input("Digite su telefono"))
print("caso 1 ")
guardarTelefono(telefono1)

# caso 2
print("caso 2 ")
guardarTelefono(65498762165)

# user.getTelefono
usuarioTel = '654987'
guardarTelefono(usuarioTel)
