//3. Crea una clase genérica Catalogo<T> que almacene productos o libros.
//  a) Agrega métodos para agregar y buscar elemento
//  b) Prueba el catálogo con libros
//  c) Prueba el catálogo con productos

import java.util.ArrayList;

public class Catalogo<T> {
    private ArrayList<T> elementos;

    public Catalogo() {
        elementos = new ArrayList<>();
    }

    public void agregar(T elemento) {
        elementos.add(elemento);
    }

    public T buscar(int indice) {
        if (indice >= 0 && indice < elementos.size()) {
            return elementos.get(indice);
        }
        return null;
    }

    public static void main(String[] args) {
        Catalogo<String> catalogoLibros = new Catalogo<>();
        catalogoLibros.agregar("Cien años de soledad");
        catalogoLibros.agregar("El señor de los anillos");
        catalogoLibros.agregar("1984");
        System.out.println("Libro en posición 1: " + catalogoLibros.buscar(1));        Catalogo<Double> catalogoPrecios = new Catalogo<>();
        catalogoPrecios.agregar(19.99);
        catalogoPrecios.agregar(29.99);
        catalogoPrecios.agregar(9.99);
        System.out.println("Precio en posición 0: " + catalogoPrecios.buscar(0));
    }
}