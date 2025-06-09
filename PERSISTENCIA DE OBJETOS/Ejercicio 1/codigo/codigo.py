#1. Sea el siguiente diagrama de clases:
#  a) Implementa el método guardarEmpleado(Empleado e) para almacenarempleados.
#  b) Implementa buscaEmpleado(String n) a traves del nombre, para ver los datosdel Empleado n.
#  c) Implementa mayorSalario(float sueldo), que devuelva al primer empleado consueldo mayor al ingresado.
import pickle

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def __str__(self):
        return f"Empleado(nombre='{self.nombre}', salario={self.salario})"

class ArchivoEmpleado:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
    
    def guardar_empleado(self, empleado):
        try:
            with open(self.nombre_archivo, 'rb') as f:
                empleados = pickle.load(f)
        except (FileNotFoundError, EOFError):
            empleados = []
        empleados.append(empleado)
        with open(self.nombre_archivo, 'wb') as f:
            pickle.dump(empleados, f)
        
        print(f"Empleado guardado: {empleado.nombre}")
    
    def busca_empleado(self, nombre):
        try:
            with open(self.nombre_archivo, 'rb') as f:
                empleados = pickle.load(f)
                for emp in empleados:
                    if emp.nombre.lower() == nombre.lower():
                        return emp
        except FileNotFoundError:
            print("Archivo no encontrado")
        except EOFError:
            print("Archivo vacío")
        return None
    
    def mayor_salario(self, sueldo):
        try:
            with open(self.nombre_archivo, 'rb') as f:
                empleados = pickle.load(f)
                for emp in empleados:
                    if emp.salario > sueldo:
                        return emp
        except FileNotFoundError:
            print("Archivo no encontrado")
        except EOFError:
            print("Archivo vacío")
        return None

if __name__ == "__main__":
    archivo = ArchivoEmpleado("empleados.dat")
    archivo.guardar_empleado(Empleado("Juan Pérez", 2500.50))
    archivo.guardar_empleado(Empleado("María Gómez", 3200.75))
    archivo.guardar_empleado(Empleado("Carlos Ruiz", 1800.25))
    encontrado = archivo.busca_empleado("maría gómez")
    print(f"Empleado encontrado: {encontrado}")
    mayor_salario = archivo.mayor_salario(2000.0)
    print(f"Empleado con salario > 2000: {mayor_salario}")