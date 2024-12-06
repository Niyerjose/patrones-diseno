from productos import FabricaDeProductos, RopaBuilder, AccesorioBuilder, CalzadoBuilder
from pedidos import AdministradorDePedidos

def personalizar_producto(tipo):
    """
    Función reutilizable para personalizar un producto según su tipo.
    """
    if tipo == "ropa":
        builder = RopaBuilder()
        builder.crear_producto_base(categoria="ropa", precio=150)
        color = input("Color: ")
        talla = input("Talla (S/M/L/XL): ")
        marca = input("Marca: ")
        builder.personalizar(color, talla, marca)
    elif tipo == "accesorio":
        builder = AccesorioBuilder()
        builder.crear_producto_base(categoria="accesorio", precio=50)
        diseñador = input("Diseñador (Nombre Apellido): ")
        material = input("Material (natural/sintético/reciclado): ")
        builder.personalizar(diseñador, material)
    elif tipo == "calzado":
        builder = CalzadoBuilder()
        builder.crear_producto_base(categoria="calzado", precio=200)
        capellada = input("Capellada (sintético/textil): ")
        suela = input("Suela (antideslizante/tacón/caucho): ")
        cierre = input("Cierre (broche/corredera/cordón): ")
        builder.personalizar(capellada, suela, cierre)
    else:
        print("Tipo de producto inválido.")
        return None

    return builder.obtener_producto()

def menu_principal():
    admin_pedidos = AdministradorDePedidos()
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear Pedido (con personalización)")
        print("2. Personalizar Producto Existente")
        print("3. Clonar Producto")
        print("4. Mostrar Pedidos")
        print("5. Actualizar Estado de Pedido")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tipo = input("Tipo de producto (ropa/accesorio/calzado): ").lower()
            producto_personalizado = personalizar_producto(tipo)
            if producto_personalizado:
                admin_pedidos.agregar_pedido(producto_personalizado)
                print("Pedido creado y personalizado exitosamente.")

        elif opcion == "2":
            print("\n--- Lista de Pedidos ---")
            admin_pedidos.mostrar_pedidos()
            indice = input("Selecciona el número del producto a personalizar: ")
            try:
                indice = int(indice) - 1
                producto = admin_pedidos.pedidos[indice]
                print("Personalizando el producto seleccionado:")
                for atributo in vars(producto).keys():
                    nuevo_valor = input(f"{atributo} ({getattr(producto, atributo)}): ")
                    if nuevo_valor:
                        setattr(producto, atributo, nuevo_valor)
                print("Producto actualizado exitosamente.")
            except (IndexError, ValueError):
                print("Selección inválida. Intenta nuevamente.")

        elif opcion == "3":
            print("\n--- Lista de Pedidos ---")
            admin_pedidos.mostrar_pedidos()
            indice = input("Selecciona el número del producto a clonar: ")
            try:
                indice = int(indice) - 1
                producto_a_clonar = admin_pedidos.pedidos[indice]
                clon = producto_a_clonar.clonar()
                print("\nClon creado exitosamente. Puedes modificarlo ahora:")
                for atributo in vars(clon).keys():
                    nuevo_valor = input(f"{atributo} ({getattr(clon, atributo)}): ")
                    if nuevo_valor:
                        setattr(clon, atributo, nuevo_valor)
                admin_pedidos.agregar_pedido(clon)
                print("Clon modificado y agregado como nuevo pedido.")
            except (IndexError, ValueError):
                print("Selección inválida. Intenta nuevamente.")

        elif opcion == "4":
            admin_pedidos.mostrar_pedidos()

        elif opcion == "5":
            print("\n--- Actualizar Estado de Pedido ---")
            admin_pedidos.mostrar_pedidos()
            id_pedido = int(input("Ingresa el ID del pedido a actualizar: "))
            print("Estados disponibles: [Procesado, Enviado, Entregado]")
            nuevo_estado = input("Ingresa el nuevo estado: ").capitalize()
            if nuevo_estado not in ["Procesado", "Enviado", "Entregado"]:
                print("Estado inválido. Intenta nuevamente.")
            else:
                if admin_pedidos.actualizar_estado(id_pedido, nuevo_estado):
                    print(f"Estado del pedido {id_pedido} actualizado a '{nuevo_estado}'.")
                else:
                    print(f"No se encontró un pedido con ID {id_pedido}.")

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    menu_principal()
