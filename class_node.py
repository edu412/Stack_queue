class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

nodo1 = Nodo(10)
nodo2 = Nodo(20)

nodo1.sig = nodo2
print (f"nodo 1: {nodo1}")
print(f"Nodo 2: {nodo1.sig.dato}")