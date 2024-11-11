class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, num):
        self.registro = num
    
    def asignarTipo(self, tipo):
        tipos = ["electrico", "gasolina"]
        if tipo in tipos:
            self.tipo = tipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cant = 0
        for i in self.asientos:
            if i != None:
                cant += 1
        return cant
    
    def verificarIntegridad(self):
        asientos_reales = []
        for i in self.asientos:
            if i != None:
                asientos_reales.append(i)
        registro_original = asientos_reales[0].registro
        for i in asientos_reales:
            if i.registro != registro_original:
                return "Las piezas no son originales"
            break
        if self.registro != registro_original or self.registro != self.motor.registro:
            return "Las piezas no son originales"
        else:
            return "Auto original"


