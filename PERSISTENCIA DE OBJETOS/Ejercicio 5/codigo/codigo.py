#5.- Sea el siguiente diagrama de clases:
#   a) Crear, leer y mostrar un Archivo de Farmacias
#   b) Mostrar los medicamentos para la tos, de la Sucursal numero X
#   c) Mostrar el número de sucursal y su dirección que tienen el medicamento “Golpex”
import pickle
from typing import List

class Medicamento:
    def __init__(self, nombre: str, codigo: int, tipo: str, precio: float):
        self.nombre = nombre
        self.codigo = codigo
        self.tipo = tipo
        self.precio = precio
    
    def __str__(self) -> str:
        return f"{self.nombre} (Cod: {self.codigo}, Tipo: {self.tipo}, Precio: ${self.precio:.2f})"

class Farmacia:
    def __init__(self, nombre: str, sucursal: int, direccion: str):
        self.nombre = nombre
        self.sucursal = sucursal
        self.direccion = direccion
        self.medicamentos: List[Medicamento] = []
    
    def agregar_medicamento(self, medicamento: Medicamento) -> None:
        self.medicamentos.append(medicamento)
    
    def buscar_medicamento(self, nombre: str) -> Medicamento | None:
        for med in self.medicamentos:
            if med.nombre.lower() == nombre.lower():
                return med
        return None
    
    def medicamentos_por_tipo(self, tipo: str) -> List[Medicamento]:
        return [med for med in self.medicamentos if med.tipo.lower() == tipo.lower()]
    
    def __str__(self) -> str:
        return (f"Farmacia: {self.nombre}\n"
                f"Sucursal: {self.sucursal}\n"
                f"Dirección: {self.direccion}\n"
                f"Medicamentos: {len(self.medicamentos)}")

class ArchivoFarmacia:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
    
    def guardar(self, farmacia: Farmacia) -> None:
        try:
            with open(self.nombre_archivo, 'wb') as f:
                pickle.dump(farmacia, f)
            print(f"Farmacia {farmacia.nombre} guardada correctamente")
        except Exception as e:
            print(f"Error al guardar: {e}")
    
    def cargar(self) -> Farmacia | None:
        try:
            with open(self.nombre_archivo, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("Archivo no encontrado")
            return None
        except Exception as e:
            print(f"Error al cargar: {e}")
            return None
    
    def mostrar_medicamentos_tos(self, sucursal: int = None) -> None:
        farmacia = self.cargar()
        if not farmacia:
            return
        
        if sucursal and farmacia.sucursal != sucursal:
            print(f"Esta farmacia no es la sucursal {sucursal}")
            return
        
        medicamentos = farmacia.medicamentos_por_tipo("tos")
        if not medicamentos:
            print("No hay medicamentos para la tos")
            return
        
        print(f"\nMedicamentos para la tos en {farmacia.nombre}:")
        for med in medicamentos:
            print(f"- {med}")
    
    def buscar_golpex(self) -> None:
        farmacia = self.cargar()
        if not farmacia:
            return
        
        golpex = farmacia.buscar_medicamento("Golpex")
        if golpex:
            print(f"\nGolpex encontrado en:")
            print(f"Sucursal: {farmacia.sucursal}")
            print(f"Dirección: {farmacia.direccion}")
        else:
            print("Golpex no encontrado")


if __name__ == "__main__":
    med1 = Medicamento("Golpex", 101, "tos", 25.50)
    med2 = Medicamento("Antigripal", 102, "resfriado", 18.75)
    med3 = Medicamento("Jarabe", 103, "tos", 15.30)
    
    farmacia = Farmacia("Farmacia Central", 1, "Av. Principal 123")
    farmacia.agregar_medicamento(med1)
    farmacia.agregar_medicamento(med2)
    farmacia.agregar_medicamento(med3)
    archivo = ArchivoFarmacia("farmacia_central.dat")
    archivo.guardar(farmacia)
    print("\n--- Mostrar medicamentos para la tos ---")
    archivo.mostrar_medicamentos_tos(1)
    print("\n--- Buscar Golpex ---")
    archivo.buscar_golpex()
    print("\n--- Datos completos de la farmacia ---")
    farmacia_cargada = archivo.cargar()
    if farmacia_cargada:
        print(farmacia_cargada)
        print("\nMedicamentos:")
        for med in farmacia_cargada.medicamentos:
            print(f"- {med}")