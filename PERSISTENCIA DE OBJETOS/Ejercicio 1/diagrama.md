```mermaid
classDiagram
    class Persona {
        -nombre: String
        -edad: int
        -ciudad: String
        +Persona(nombre: String, edad: int, ciudad: String)
        +saludar(): void
        +mayordeedad(): boolean
    }