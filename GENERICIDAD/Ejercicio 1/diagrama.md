```mermaid
classDiagram
    class Catalogo~T~ {
        -elementos: List~T~
        +agregar(elemento: T): void
        +buscar(indice: int): T
    }
    
    Catalogo~String~ : Libros
    Catalogo~Double~ : Precios