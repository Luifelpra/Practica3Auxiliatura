#3.- Sea el siguiente diagrama de clases:
#   a) Implementar el diagrama de clases.
#   b) Implementa buscarCliente(int c) a través del id.
#   c) Implementa buscarCelularCliente(int c), que devuelva los datos del cliente junto al número de celular.
import pickle
class Cliente:
    def __init__(self, id_cliente, nombre, telefono):
        self.id = id_cliente
        self.nombre = nombre
        self.telefono = telefono
    
    def __str__(self):
        return f"Cliente(id={self.id}, nombre='{self.nombre}', telefono={self.telefono})"

class ArchivoCliente:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
    
    def guardar_cliente(self, cliente):
        try:
            with open(self.nombre_archivo, 'rb') as f:
                clientes = pickle.load(f)
        except (FileNotFoundError, EOFError):
            clientes = []
        
        clientes.append(cliente)
        with open(self.nombre_archivo, 'wb') as f:
            pickle.dump(clientes, f)
        
        print(f"Cliente guardado: {cliente.nombre}")
    
    def buscar_cliente(self, id_cliente):
        try:
            with open(self.nombre_archivo, 'rb') as f:
                clientes = pickle.load(f)
                for cli in clientes:
                    if cli.id == id_cliente:
                        return cli
        except FileNotFoundError:
            print("Archivo no encontrado")
        except EOFError:
            print("Archivo vacío")
        return None
    
    def buscar_celular_cliente(self, telefono):
        try:
            with open(self.nombre_archivo, 'rb') as f:
                clientes = pickle.load(f)
                for cli in clientes:
                    if cli.telefono == telefono:
                        return cli
        except FileNotFoundError:
            print("Archivo no encontrado")
        except EOFError:
            print("Archivo vacío")
        return None

if __name__ == "__main__":
    archivo = ArchivoCliente("clientes.dat")
    archivo.guardar_cliente(Cliente(1, "Ana Torres", 70123456))
    archivo.guardar_cliente(Cliente(2, "Luis Mendoza", 68754321))
    archivo.guardar_cliente(Cliente(3, "Sofía Castro", 71234567))
    encontrado = archivo.buscar_cliente(2)
    print(f"Cliente encontrado por ID: {encontrado}")
    por_telefono = archivo.buscar_celular_cliente(71234567)
    print(f"Cliente encontrado por teléfono: {por_telefono}")