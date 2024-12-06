class AdministradorDePedidos:
    _instancia = None
    _contador_ids = 1  # Contador para asignar IDs únicos.

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.pedidos = []
        return cls._instancia

    def agregar_pedido(self, pedido):
        # Asignar un ID único al pedido y establecer su estado inicial.
        pedido.id = AdministradorDePedidos._contador_ids
        AdministradorDePedidos._contador_ids += 1
        pedido.estado = "En proceso"
        self.pedidos.append(pedido)

    def mostrar_pedidos(self):
        if not self.pedidos:
            print("No hay pedidos registrados.")
        else:
            for pedido in self.pedidos:
                print(
                    f"ID: {pedido.id}, Categoría: {pedido.categoria}, Estado: {pedido.estado}, Detalles: {pedido.mostrar_informacion()}"
                )

    def actualizar_estado(self, id_pedido, nuevo_estado):
        # Buscar el pedido por ID y actualizar su estado.
        for pedido in self.pedidos:
            if pedido.id == id_pedido:
                pedido.estado = nuevo_estado
                return True
        return False
