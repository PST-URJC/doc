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

if __name__ == "__main__":
    a = ArbolBinario(5)
    print ("Altura:", a.altura())
    a.insertar(3)
    a.insertar(8)
    print ("Altura:", a.altura())
    a.insertar(10)
    a.insertar(12)
    a.insertar(14)
    print ("Altura:", a.altura())
    a.insertar(11)
    print ("Altura:", a.altura())

    b = ArbolBinario(10)
    print ("Altura:", b.altura())
    b.insertar(8)
    b.insertar(12)
    print ("Altura:", b.altura())
    b.insertar(7)
    b.insertar(6)
    b.insertar(5)
    print ("Altura:", b.altura())
    b.insertar(15)
    print ("Altura:", b.altura())
