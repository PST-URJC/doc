import random

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