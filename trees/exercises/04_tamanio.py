class ArbolBinario:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

    def insertar(self, dato):
        if dato < self.dato:
            if not self.izquierdo:
                self.izquierdo = ArbolBinario(dato)
            else:
                self.izquierdo.insertar(dato)
        else:
            if not self.derecho:
                self.derecho = ArbolBinario(dato)
            else:
                self.derecho.insertar(dato)

    def pintar_menor_a_mayor(self):
        if self.izquierdo:
            self.izquierdo.pintar_menor_a_mayor()
        print(self.dato)
        if self.derecho:
            self.derecho.pintar_menor_a_mayor()

    def pintar_mayor_a_menor(self):
        if self.derecho:
            self.derecho.pintar_mayor_a_menor()
        print(self.dato)
        if self.izquierdo:
            self.izquierdo.pintar_mayor_a_menor()

    def tamanio(self):
        tamanio = 0
        if self.dato != None:
            tamanio += 1
        if self.izquierdo:
            tamanio += self.izquierdo.tamanio()
        if self.derecho:
            tamanio += self.derecho.tamanio()
        return tamanio

if __name__ == "__main__":
    a = ArbolBinario(5)
    a.insertar(3)
    a.insertar(8)
    a.insertar(6)
    a.insertar(3)
    print ("Tamaño arbol:", a.tamanio())
    a.insertar(9)
    a.insertar(12)
    a.insertar(0)
    print ("Tamaño arbol:", a.tamanio())