import random

class ArbolBinario:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

    def insertar(self, dato):
        if not self.izquierdo:
            self.izquierdo = ArbolBinario(dato)
        elif not self.derecho:
            self.derecho = ArbolBinario(dato)
        else:
            if random.randint(0,1) == 0:
                self.izquierdo.insertar(dato)
            else:
                self.derecho.insertar(dato)
