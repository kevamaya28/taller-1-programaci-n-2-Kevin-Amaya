print("Sistema de gestion del consultorio odontologico")

clientes = []

while True:

    print()
    print("MENU PRINCIPAL")
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Buscar cliente por cedula")
    print("4. Mostrar estadisticas")
    print("5. Ordenar clientes por valor de atencion")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        print()
        print("Registro de cliente")

        cedula = input("Ingrese la cedula: ")

        while cedula == "":
            print("La cedula no puede estar vacia.")
            cedula = input("Ingrese la cedula: ")

        existe = False

        for cliente in clientes:
            if cliente["cedula"] == cedula:
                existe = True

        if existe:
            print("Ya existe un cliente con esa cedula.")
            continue

        nombre = input("Ingrese el nombre: ")

        while nombre == "":
            print("El nombre no puede estar vacio.")
            nombre = input("Ingrese el nombre: ")

        telefono = input("Ingrese el telefono: ")

        while telefono == "":
            print("El telefono no puede estar vacio.")
            telefono = input("Ingrese el telefono: ")

        print()
        print("Tipo de cliente:")
        print("1. Particular")
        print("2. EPS")
        print("3. Prepagada")

        opcion_cliente = input("Seleccione una opcion: ")

        while opcion_cliente not in ["1", "2", "3"]:
            print("Opcion no valida. Intente nuevamente.")
            opcion_cliente = input("Seleccione una opcion: ")

        if opcion_cliente == "1":
            tipo_cliente = "Particular"
            valor_cita = 80000
        elif opcion_cliente == "2":
            tipo_cliente = "EPS"
            valor_cita = 5000
        else:
            tipo_cliente = "Prepagada"
            valor_cita = 30000

        print()
        print("Tipo de atencion:")
        print("1. Limpieza")
        print("2. Calzas")
        print("3. Extraccion")
        print("4. Diagnostico")

        opcion_atencion = input("Seleccione una opcion: ")

        while opcion_atencion not in ["1", "2", "3", "4"]:
            print("Opcion no valida. Intente nuevamente.")
            opcion_atencion = input("Seleccione una opcion: ")

        if opcion_atencion == "1":

            tipo_atencion = "Limpieza"

            if tipo_cliente == "Particular":
                valor_atencion = 60000
            else:
                valor_atencion = 0

            cantidad = 1

        elif opcion_atencion == "2":

            tipo_atencion = "Calzas"

            if tipo_cliente == "Particular":
                valor_atencion = 80000
            elif tipo_cliente == "EPS":
                valor_atencion = 40000
            else:
                valor_atencion = 10000

            cantidad = input("Ingrese la cantidad de calzas: ")

            while not cantidad.isdigit() or int(cantidad) <= 0:
                print("La cantidad debe ser mayor que cero.")
                cantidad = input("Ingrese la cantidad de calzas: ")

            cantidad = int(cantidad)

        elif opcion_atencion == "3":

            tipo_atencion = "Extraccion"

            if tipo_cliente == "Particular":
                valor_atencion = 100000
            elif tipo_cliente == "EPS":
                valor_atencion = 40000
            else:
                valor_atencion = 10000

            cantidad = input("Ingrese la cantidad de extracciones: ")

            while not cantidad.isdigit() or int(cantidad) <= 0:
                print("La cantidad debe ser mayor que cero.")
                cantidad = input("Ingrese la cantidad de extracciones: ")

            cantidad = int(cantidad)

        else:

            tipo_atencion = "Diagnostico"

            if tipo_cliente == "Particular":
                valor_atencion = 50000
            else:
                valor_atencion = 0

            cantidad = 1

        total = valor_cita + (valor_atencion * cantidad)

        cliente = {
            "cedula": cedula,
            "nombre": nombre,
            "telefono": telefono,
            "tipo_cliente": tipo_cliente,
            "tipo_atencion": tipo_atencion,
            "cantidad": cantidad,
            "valor_cita": valor_cita,
            "valor_atencion": valor_atencion,
            "total": total
        }

        clientes.append(cliente)

        print()
        print("Cliente registrado correctamente.")
        print("Valor de la cita: $", valor_cita)
        print("Valor de la atencion: $", valor_atencion)
        print("Cantidad:", cantidad)
        print("Total a pagar: $", total)

    elif opcion == "2":

        print()
        print("Lista de clientes")

        if len(clientes) == 0:
            print("No hay clientes registrados.")
        else:

            for cliente in clientes:

                print()
                print("Cedula:", cliente["cedula"])
                print("Nombre:", cliente["nombre"])
                print("Telefono:", cliente["telefono"])
                print("Tipo de cliente:", cliente["tipo_cliente"])
                print("Tipo de atencion:", cliente["tipo_atencion"])
                print("Cantidad:", cliente["cantidad"])
                print("Valor de la cita: $", cliente["valor_cita"])
                print("Valor de la atencion: $", cliente["valor_atencion"])
                print("Total a pagar: $", cliente["total"])

    elif opcion == "3":

        print()
        print("Buscar cliente por cedula")

        if len(clientes) == 0:
            print("No hay clientes registrados.")
        else:

            clientes_ordenados = sorted(
                clientes,
                key=lambda cliente: cliente["valor_atencion"],
                reverse=True
            )

            cedula_buscar = input("Ingrese la cedula que desea buscar: ")

            encontrado = False

            for cliente in clientes_ordenados:

                if cliente["cedula"] == cedula_buscar:

                    print()
                    print("Cliente encontrado")
                    print("Cedula:", cliente["cedula"])
                    print("Nombre:", cliente["nombre"])
                    print("Telefono:", cliente["telefono"])
                    print("Tipo de cliente:", cliente["tipo_cliente"])
                    print("Tipo de atencion:", cliente["tipo_atencion"])
                    print("Cantidad:", cliente["cantidad"])
                    print("Valor de la cita: $", cliente["valor_cita"])
                    print("Valor de la atencion: $", cliente["valor_atencion"])
                    print("Total a pagar: $", cliente["total"])

                    encontrado = True

            if not encontrado:
                print("No se encontro ningun cliente con esa cedula.")

    elif opcion == "4":

        print()
        print("Estadisticas")

        if len(clientes) == 0:
            print("No hay clientes registrados.")
        else:

            total_clientes = len(clientes)
            ingresos_totales = 0
            clientes_extraccion = 0

            for cliente in clientes:

                ingresos_totales = ingresos_totales + cliente["total"]

                if cliente["tipo_atencion"] == "Extraccion":
                    clientes_extraccion = clientes_extraccion + 1

            print("Total de clientes:", total_clientes)
            print("Ingresos totales: $", ingresos_totales)
            print("Clientes que van para extraccion:", clientes_extraccion)

    elif opcion == "5":

        print()
        print("Clientes ordenados por valor de atencion")

        if len(clientes) == 0:
            print("No hay clientes registrados.")
        else:

            clientes_ordenados = sorted(
                clientes,
                key=lambda cliente: cliente["valor_atencion"],
                reverse=True
            )

            for cliente in clientes_ordenados:

                print()
                print("Cedula:", cliente["cedula"])
                print("Nombre:", cliente["nombre"])
                print("Tipo de cliente:", cliente["tipo_cliente"])
                print("Tipo de atencion:", cliente["tipo_atencion"])
                print("Valor de atencion: $", cliente["valor_atencion"])

    elif opcion == "6":

        print()
        print("Gracias por utilizar el sistema.")
        break

    else:

        print()
        print("Opcion no valida. Intente nuevamente.")