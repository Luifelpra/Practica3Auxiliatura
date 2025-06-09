```mermaid
classDiagram
    class Estudiante {
        -nombre: String
        -nota_1: float
        -nota_2: float
        +Estudiante(nombre: String, nota_1: float, nota_2: float)
        +calcularpromedio() float
        +aprobo() boolean
        +resultados() void
    }