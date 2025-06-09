//3.- Sea el siguiente diagrama de clases:
//  a) Implementar el diagrama de clases.
//  b) Implementa buscarCliente(int c) a través del id.
//  c) Implementa buscarCelularCliente(int c), que devuelva los datos del cliente junto al número de celular.
import java.io.Serializable;

public class Cliente implements Serializable {
    private int id;
    private String nombre;
    private int telefono;

    public Cliente(int id, String nombre, int telefono) {
        this.id = id;
        this.nombre = nombre;
        this.telefono = telefono;
    }

    public int getId() { return id; }
    public String getNombre() { return nombre; }
    public int getTelefono() { return telefono; }

    @Override
    public String toString() {
        return "Cliente{" + "id=" + id + ", nombre='" + nombre + '\'' + ", telefono=" + telefono + '}';
    }
}

import java.io.*;

public class ArchivoCliente {
    private String nombreArchivo;

    public ArchivoCliente(String nombreArchivo) {
        this.nombreArchivo = nombreArchivo;
    }

    public void guardaCliente(Cliente c) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nombreArchivo, true))) {
            oos.writeObject(c);
            System.out.println("Cliente guardado: " + c.getNombre());
        } catch (IOException ex) {
            System.err.println("Error al guardar cliente: " + ex.getMessage());
        }
    }

    public Cliente buscarCliente(int id) {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nombreArchivo))) {
            while (true) {
                Cliente cliente = (Cliente) ois.readObject();
                if (cliente.getId() == id) {
                    return cliente;
                }
            }
        } catch (EOFException e) {
            System.out.println("Búsqueda completada");
        } catch (IOException | ClassNotFoundException ex) {
            System.err.println("Error al buscar cliente: " + ex.getMessage());
        }
        return null;
    }

    public Cliente buscarCelularCliente(int telefono) {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nombreArchivo))) {
            while (true) {
                Cliente cliente = (Cliente) ois.readObject();
                if (cliente.getTelefono() == telefono) {
                    return cliente;
                }
            }
        } catch (EOFException e) {
            System.out.println("Búsqueda completada");
        } catch (IOException | ClassNotFoundException ex) {
            System.err.println("Error al buscar cliente: " + ex.getMessage());
        }
        return null;
    }

    public static void main(String[] args) {
        ArchivoCliente archivo = new ArchivoCliente("clientes.dat");
        archivo.guardaCliente(new Cliente(1, "Ana Torres", 70123456));
        archivo.guardaCliente(new Cliente(2, "Luis Mendoza", 68754321));
        archivo.guardaCliente(new Cliente(3, "Sofía Castro", 71234567));
        Cliente encontrado = archivo.buscarCliente(2);
        System.out.println("Cliente encontrado por ID: " + encontrado);
        Cliente porTelefono = archivo.buscarCelularCliente(71234567);
        System.out.println("Cliente encontrado por teléfono: " + porTelefono);
    }
}