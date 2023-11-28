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
                return self.izquierdo.borrar(dato)
            elif not self.izquierdo and self.derecho:
                return self.derecho.borrar(dato)
            elif self.izquierdo and self.derecho:
                return self.derecho.borrar(dato) or self.izquierdo.borrar(dato)

    def como_lista(self):
        if self.dato == None:
            return []
        a = [self.dato]
        if self.izquierdo:
            a += self.izquierdo.como_lista()
        if self.derecho:
            a += self.derecho.como_lista()
        return a

    def borrar(self, dato):
        if self.dato == None:
            return False
        restantes = []
        if self.dato == dato:
            if self.izquierdo:
                restantes += self.izquierdo.como_lista()
            if self.derecho:
                restantes += self.derecho.como_lista()
            if restantes:
                self.dato = restantes.pop()
                self.izquierdo = None
                self.derecho = None
                for r in restantes:
                    self.insertar(r)
            return True
        if not self.derecho and self.izquierdo:
            return self.izquierdo.borrar(dato)
        elif not self.izquierdo and self.derecho:
            return self.derecho.borrar(dato)
        elif self.izquierdo and self.derecho:
            return self.derecho.borrar(dato) or self.izquierdo.borrar(dato)
        return False

if __name__ == "__main__":
    a = ArbolBinario(10)
    a.insertar(4)
    a.insertar(9)
    a.insertar(0)
    a.insertar(6)
    a.insertar(25)
    a.insertar(2)
    a.insertar(1)
    print("tamaño(a):", a.tamanio())
    a.pintar_menor_a_mayor()
    print("borrar(2):", a.borrar(2))
    print("borrar(17):", a.borrar(17))
    print("borrar(2):", a.borrar(2))
    print("-----")
    print("tamaño(a):", a.tamanio())
    a.pintar_menor_a_mayor()
    print("-----")
    print("borrar(10):", a.borrar(10))
    print("tamaño(a):", a.tamanio())
    a.pintar_menor_a_mayor()
