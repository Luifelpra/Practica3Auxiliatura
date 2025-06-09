#5: Crea una clase genérica Pila<T>
#   a) Implementa un método para apilar
#   b) Implementa un método para des apilar
#   c) Prueba la pila con diferentes tipos de datos
#   d) Muestra los datos de la pila

class Pila:
    def __init__(self):
        self.elementos = []
    
    def apilar(self, elemento):
        self.elementos.append(elemento)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def mostrar(self):
        print("Contenido de la pila:")
        for elem in reversed(self.elementos):
            print(elem)


if __name__ == "__main__":
    pila = Pila()
    pila.apilar(10)
    pila.apilar("Hola")
    pila.apilar(3.14)
    pila.apilar([1, 2, 3])
    pila.mostrar()
    print("\nDesapilando:")
    print(pila.desapilar())
    print(pila.desapilar())
    print("\nPila después de desapilar:")
    pila.mostrar()