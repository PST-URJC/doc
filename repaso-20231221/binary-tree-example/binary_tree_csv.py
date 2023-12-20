class ArbolBinario:
    def __init__(self):
        self.init(None)

    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

    def insertar(self, dato):
        if dato < self.dato:
            if not self.izquierdo:
                self.izquierdo = ArbolBinario(dato)
                return True
            else:
                return self.izquierdo.insertar(dato)
        elif dato > self.dato:
            if not self.derecho:
                self.derecho = ArbolBinario(dato)
                return True
            else:
                return self.derecho.insertar(dato)
        else:
            return False


    def como_csv(self):
        return self.arbol_como_csv()[:-1]

    def arbol_como_csv(self):
        csv=""
        if self.izquierdo:
            csv += self.izquierdo.arbol_como_csv()
        csv += self.dato + ","
        if self.derecho:
            csv += self.derecho.arbol_como_csv()
        return csv

def imprimir_separador():
    print("---------")

if __name__ == "__main__":
    a = ArbolBinario("juan")
    a.insertar("luis")
    a.insertar("amelia")
    a.insertar("carla")
    imprimir_separador()
    if False == a.insertar("carla"):
        print("No inserto a carla, ya se encuentra en el árbol")
    print("CSV:", a.como_csv())
    imprimir_separador()
