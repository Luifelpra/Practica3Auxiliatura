#1. Crea una clase genérica Caja<T> para guardar algún tipo de objeto
#   a) Agrega métodos guardar() y obtener()
#   b) Crea dos instancias de la caja y almacena 2 datos de diferente tipo
#   c) Muestra el contenido de las cajas
class Caja:
    def __init__(self):
        self.contenido = None
    
    def guardar(self, item):
        self.contenido = item
    
    def obtener(self):
        return self.contenido

if __name__ == "__main__":
    caja_texto = Caja()
    caja_texto.guardar("Contenido de texto")
    caja_numero = Caja()
    caja_numero.guardar(100)
    print(f"Caja de texto: {caja_texto.obtener()}")
    print(f"Caja de número: {caja_numero.obtener()}")