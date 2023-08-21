class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_nombre(self):
        print(self.nombre)

    def imprimir_edad(self):
        print(self.edad)


class Estudiante(Persona):
    def __init__(self):
        pass

persona = Estudiante('Juan', 25)

persona.imprimir_nombre()
persona.imprimir_edad()