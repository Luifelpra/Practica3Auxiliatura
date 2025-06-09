#3. Crea una clase genérica Catalogo<T> que almacene productos o libros.
#  a) Agrega métodos para agregar y buscar elemento
#  b) Prueba el catálogo con libros
#  c) Prueba el catálogo con productos
class Catalogo:
    def __init__(self):
        self.elementos = []
    
    def agregar(self, elemento):
        self.elementos.append(elemento)
    
    def buscar(self, indice):
        try:
            return self.elementos[indice]
        except IndexError:
            return None

if __name__ == "__main__":
    catalogo_libros = Catalogo()
    catalogo_libros.agregar("Cien años de soledad")
    catalogo_libros.agregar("El señor de los anillos")
    catalogo_libros.agregar("1984")
    print(f"Libro en posición 1: {catalogo_libros.buscar(1)}")
    catalogo_precios = Catalogo()
    catalogo_precios.agregar(19.99)
    catalogo_precios.agregar(29.99)
    catalogo_precios.agregar(9.99)
    print(f"Precio en posición 0: {catalogo_precios.buscar(0)}")