//1. Crea una clase genérica Caja<T> para guardar algún tipo de objeto
//  a) Agrega métodos guardar() y obtener()
//  b) Crea dos instancias de la caja y almacena 2 datos de diferente tipo
//  c) Muestra el contenido de las cajas
public class Caja<T> {
    private T contenido;
    public void guardar(T item) {
        this.contenido = item;
    }

    public T obtener() {
        return contenido;
    }

    public static void main(String[] args) {
        Caja<String> cajaTexto = new Caja<>();
        cajaTexto.guardar("Contenido de texto");
        Caja<Integer> cajaNumero = new Caja<>();
        cajaNumero.guardar(100);
        System.out.println("Caja de texto: " + cajaTexto.obtener());
        System.out.println("Caja de número: " + cajaNumero.obtener());
    }
}