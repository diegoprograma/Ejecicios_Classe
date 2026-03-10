class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        #atributo privado
        if precio < 0:
            self._precio = 0
            #atributo privado
        else:
            raise ValueError("El precio inicial debe ser mayor a cero")
            #metodo para obtener el nombre (getter)

    def get_precio(self):
        return self._