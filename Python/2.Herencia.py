class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f'{self.nombre} esta hablando.')

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        # Especificammos los atributos que se heredaran
        super().__init__(nombre, edad, nacionalidad)
        
        self.trabajo = trabajo
        self.salario = salario
    
    def trabajar(self):
        print(f'{self.nombre} esta trabajando como {self.trabajo}')

roberto = Empleado('Roberto', 35, 'colombiano', 'programador', 10000)

roberto.hablar()
roberto.trabajar()