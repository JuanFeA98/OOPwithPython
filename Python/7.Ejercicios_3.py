class Animal():
    def __init__(self):
        pass

    def comer(self):
        print('Comiendo...')

class Mamifero():
    def __init__(self):
        pass

    def amamantar(self):
        print('Amamantando...')

class Ave():
    def __init__(self):
        pass

    def volar(self):
        print('Volando...')

class Murcielago(Mamifero, Ave, Animal):
    def __init__(self):
        pass

Murcielago = Murcielago()
Murcielago.amamantar()
Murcielago.volar()
Murcielago.comer()