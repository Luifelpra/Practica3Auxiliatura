```mermaid
classDiagram
    class Coche {
        -marca: String
        -modelo: String
        -velocidad: int
        +Coche(marca: String, modelo: String)
        +acelerar(): void
        +frenar(): void
        +mostrarvelocidad(): void
    }