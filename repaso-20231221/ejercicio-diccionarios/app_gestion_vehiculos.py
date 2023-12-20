class GestorVehiculos:
    def __init__(self):
        self.dic_vehiculos = {}
    def insertar_vehiculo(self, vehiculo):
        if vehiculo.tipo() not in self.dic_vehiculos:
            self.dic_vehiculos[vehiculo.tipo()] = [vehiculo]
        else:
            self.dic_vehiculos[vehiculo.tipo()].append(vehiculo)
    def mostrar_vehiculos(self):
        for k in self.dic_vehiculos:
            for v in self.dic_vehiculos[k]:
                v.mostrar()

class Vehiculo:
    def __init__(self, n_bastidor, matricula):
        self.n_bastidor = n_bastidor
        self.matricula = matricula

class Coche(Vehiculo):
    def __init__(self, n_bastidor, matricula, sillas_bebe):
        super().__init__(n_bastidor, matricula)
        self.sillas_bebe = sillas_bebe

    def tipo(self):
        return "coche"

    def mostrar(self):
        print('Coche con número de bastidor:', self.n_bastidor,
              '; matrícula:', self.matricula,
              '; Sillas Bebé:', self.sillas_bebe)

class Moto(Vehiculo):
    def __init__(self, n_bastidor, matricula, cupula):
        super().__init__(n_bastidor, matricula)
        self.cupula = cupula

    def tipo(self):
        return "moto"

    def tiene_cupula(self):
        if self.cupula:
            return "Sí"
        return "No"

    def mostrar(self):
        print(' Moto con número de bastidor:', self.n_bastidor,
              '; matrícula:', self.matricula,
              '; Cúpula:', self.tiene_cupula())

if __name__ == '__main__':
    gestor = GestorVehiculos()
    coche = Coche(n_bastidor="900100100", matricula="1234PST", sillas_bebe=2)
    moto  =  Moto(n_bastidor="200100100", matricula="1235PST", cupula=False)
    moto2 =  Moto(n_bastidor="200100121", matricula="1280PST", cupula=True)
    gestor.insertar_vehiculo(coche)
    gestor.insertar_vehiculo(moto)
    gestor.insertar_vehiculo(moto2)
    gestor.mostrar_vehiculos()
