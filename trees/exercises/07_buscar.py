class ArbolBinario:
    def __init__(self):
        self.dato = None
        self.izquierdo = None
        self.derecho = None

    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

    def insertar(self, dato):
        if not self.dato:
            self.dato = dato
        elif dato < self.dato:
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
        if self.dato:
            tamanio += 1
        if self.izquierdo:
            tamanio += self.izquierdo.tamanio()
        if self.derecho:
            tamanio += self.derecho.tamanio()
        return tamanio

    def altura(self):
        altura_derecho = 0
        altura_izquierdo = 0
        if not self.dato:
           return 0
        if self.izquierdo:
           altura_izquierdo = self.izquierdo.altura()
        if self.derecho:
            altura_derecho = self.derecho.altura()
        if altura_izquierdo > altura_derecho:
            return 1 + altura_izquierdo
        return 1 + altura_derecho

    def insertar_arbol(self, arbol):
        if not self.dato:
            self.dato = arbol.dato
            self.izquierdo = arbol.izquierdo
            self.derecho = arbol.derecho
        elif arbol.dato < self.dato:
            if not self.izquierdo:
                self.izquierdo = arbol
            else:
                self.izquierdo.insertar_arbol(arbol)
        else:
            if not self.derecho:
                self.derecho = arbol
            else:
                self.derecho.insertar_arbol(arbol)

    def buscar(self, dato):
        if not self.dato:
            return False
        elif self.dato == dato:
            return True
        else:
            if not self.derecho and self.izquierdo:
                return self.izquierdo.buscar(dato)
            elif not self.izquierdo and self.derecho:
                return self.derecho.buscar(dato)
            elif self.izquierdo and self.derecho:
                return self.derecho.buscar(dato) or self.izquierdo.buscar(dato)

if __name__ == "__main__":
    a = ArbolBinario(10)
    a.insertar(4)
    a.insertar(9)
    a.insertar(0)
    a.insertar(6)
    a.insertar(6)
    a.insertar(25)
    a.insertar(2)
    a.insertar(1)
    a.insertar(0)
    print("buscar(3):", a.buscar(3))
    print("buscar(9):", a.buscar(9))
    print("buscar(6):", a.buscar(6))
    print("-----")
