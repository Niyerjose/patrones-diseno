import copy

class ProductoBase:
    def __init__(self, categoria, precio):
        self.categoria = categoria
        self.precio = precio
        self.id = None  # ID único asignado por el sistema.
        self.estado = None  # Estado del pedido.

    def mostrar_informacion(self):
        atributos = vars(self)
        info = ", ".join(f"{key}: {value}" for key, value in atributos.items() if key not in ["id", "estado"])
        return f"{info}"

    def clonar(self):
        return copy.deepcopy(self)

class Ropa(ProductoBase):
    pass

class Accesorio(ProductoBase):
    pass

class Calzado(ProductoBase):
    pass

class FabricaDeProductos:
    @staticmethod
    def crear_producto(tipo, **kwargs):
        if tipo == "ropa":
            return Ropa(**kwargs)
        elif tipo == "accesorio":
            return Accesorio(**kwargs)
        elif tipo == "calzado":
            return Calzado(**kwargs)
        else:
            raise ValueError("Tipo de producto desconocido")
            
class ProductoBuilder:
    def __init__(self):
        self.producto = None

    def crear_producto_base(self, categoria, precio):
        self.producto = ProductoBase(categoria, precio)

    def agregar_atributo(self, atributo, valor):
        setattr(self.producto, atributo, valor)

    def obtener_producto(self):
        return self.producto


class RopaBuilder(ProductoBuilder):
    def __init__(self):
        super().__init__()

    def personalizar(self, color, talla, marca):
        self.agregar_atributo("color", color)
        self.agregar_atributo("talla", talla)
        self.agregar_atributo("marca", marca)


class AccesorioBuilder(ProductoBuilder):
    def __init__(self):
        super().__init__()

    def personalizar(self, diseñador, material):
        self.agregar_atributo("diseñador", diseñador)
        self.agregar_atributo("material", material)


class CalzadoBuilder(ProductoBuilder):
    def __init__(self):
        super().__init__()

    def personalizar(self, capellada, suela, cierre):
        self.agregar_atributo("capellada", capellada)
        self.agregar_atributo("suela", suela)
        self.agregar_atributo("cierre", cierre)
