//5.Crea una clase Estudiante con nombre, nota_1, nota_2
//  a) Agrega un método para calcular el promedio
//  b) Agrega un método para verificar si aprobó (promedio >=6)
//  c) Crea tres estudiantes, muestra sus promedios y si aprobaron
// Empleado.java
import java.io.Serializable;

public class Empleado implements Serializable {
    private String nombre;
    private float salario;

    public Empleado(String nombre, float salario) {
        this.nombre = nombre;
        this.salario = salario;
    }

    // Getters
    public String getNombre() { return nombre; }
    public float getSalario() { return salario; }

    @Override
    public String toString() {
        return "Empleado{" + "nombre='" + nombre + '\'' + ", salario=" + salario + '}';
    }
}

import java.io.*;

public class ArchivoEmpleado {
    private String nombreArchivo;

    public ArchivoEmpleado(String nombreArchivo) {
        this.nombreArchivo = nombreArchivo;
    }

    public void guardarEmpleado(Empleado e) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nombreArchivo, true))) {
            oos.writeObject(e);
            System.out.println("Empleado guardado: " + e.getNombre());
        } catch (IOException ex) {
            System.err.println("Error al guardar empleado: " + ex.getMessage());
        }
    }

    public Empleado buscaEmpleado(String nombre) {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nombreArchivo))) {
            while (true) {
                Empleado emp = (Empleado) ois.readObject();
                if (emp.getNombre().equalsIgnoreCase(nombre)) {
                    return emp;
                }
            }
        } catch (EOFException e) {
            System.out.println("Búsqueda completada");
        } catch (IOException | ClassNotFoundException ex) {
            System.err.println("Error al buscar empleado: " + ex.getMessage());
        }
        return null;
    }

    public Empleado mayorSalario(float sueldo) {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nombreArchivo))) {
            while (true) {
                Empleado emp = (Empleado) ois.readObject();
                if (emp.getSalario() > sueldo) {
                    return emp;
                }
            }
        } catch (EOFException e) {
            System.out.println("Búsqueda completada");
        } catch (IOException | ClassNotFoundException ex) {
            System.err.println("Error al buscar empleado: " + ex.getMessage());
        }
        return null;
    }

    public static void main(String[] args) {
        ArchivoEmpleado archivo = new ArchivoEmpleado("empleados.dat");
        archivo.guardarEmpleado(new Empleado("Juan Pérez", 2500.50f));
        archivo.guardarEmpleado(new Empleado("María Gómez", 3200.75f));
        archivo.guardarEmpleado(new Empleado("Carlos Ruiz", 1800.25f));
        Empleado encontrado = archivo.buscaEmpleado("maría gómez");
        System.out.println("Empleado encontrado: " + encontrado);
        Empleado mayorSalario = archivo.mayorSalario(2000.0f);
        System.out.println("Empleado con salario > 2000: " + mayorSalario);
    }
}