"""Modelos del Sistema de Registro Automotriz."""

class Motor:
    """Componente que forma parte de un vehículo."""

    def __init__(self, tipo, potencia):
        if not isinstance(tipo, str) or not tipo.strip():
            raise ValueError("El tipo de motor no puede estar vacío.")
        if not isinstance(potencia, (int, float)) or potencia <= 0:
            raise ValueError("La potencia debe ser positiva.")
        self.tipo = tipo
        self.potencia = potencia
        self.__encendido = False

    @property
    def encendido(self):
        return self.__encendido

    def encender(self):
        if self.__encendido:
            return "El motor ya se encuentra encendido."
        self.__encendido = True
        return f"Motor {self.tipo} encendido correctamente."

    def apagar(self):
        if not self.__encendido:
            return "El motor ya se encuentra apagado."
        self.__encendido = False
        return "El motor se ha apagado correctamente."

    def mostrar_informacion(self):
        estado = "Encendido" if self.__encendido else "Apagado"
        return f"Tipo: {self.tipo} | Potencia: {self.potencia} HP | Estado: {estado}"


class Vehiculo:
    """Clase base para los vehículos registrados."""

    def __init__(self, marca, modelo, anio, placa, color, motor):
        if not isinstance(marca, str) or not marca.strip():
            raise ValueError("La marca no puede estar vacía.")
        if not isinstance(modelo, str) or not modelo.strip():
            raise ValueError("El modelo no puede estar vacío.")
        if not isinstance(placa, str) or not placa.strip():
            raise ValueError("La placa no puede estar vacía.")
        if not isinstance(anio, int) or anio < 1886:
            raise ValueError("El año del vehículo no es válido.")
        if not isinstance(motor, Motor):
            raise TypeError("El vehículo debe tener un objeto Motor.")

        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.placa = placa.strip().upper()
        self.color = color
        self.motor = motor  # Composición: el vehículo tiene un motor.
        self.__velocidad = 0  # Encapsulamiento.

    @property
    def velocidad(self):
        return self.__velocidad

    def acelerar(self, incremento=20):
        if not self.motor.encendido:
            return f"No se puede acelerar: el vehículo {self.placa} está apagado."
        if not isinstance(incremento, (int, float)) or incremento <= 0:
            raise ValueError("El incremento debe ser positivo.")
        self.__velocidad += incremento
        return f"Velocidad actual de {self.placa}: {self.__velocidad} km/h."

    def frenar(self, reduccion=20):
        if not isinstance(reduccion, (int, float)) or reduccion <= 0:
            raise ValueError("La reducción debe ser positiva.")
        self.__velocidad = max(0, self.__velocidad - reduccion)
        return f"Velocidad actual de {self.placa}: {self.__velocidad} km/h."

    def detener(self):
        self.__velocidad = 0
        return f"El vehículo {self.placa} está detenido."

    def mostrar_informacion(self):
        return (
            f"Placa: {self.placa}\n"
            f"Vehículo: {self.marca} {self.modelo}\n"
            f"Año: {self.anio}\n"
            f"Color: {self.color}\n"
            f"Velocidad: {self.velocidad} km/h"
        )

    def describir(self):
        return "Vehículo registrado en el sistema automotriz."


class Automovil(Vehiculo):
    """Subclase para automóviles."""

    def __init__(self, marca, modelo, anio, placa, color, motor, numero_puertas):
        super().__init__(marca, modelo, anio, placa, color, motor)
        if not isinstance(numero_puertas, int) or numero_puertas < 2:
            raise ValueError("El número de puertas debe ser válido.")
        self.numero_puertas = numero_puertas

    def describir(self):
        return "Este registro corresponde a un automóvil."

    def mostrar_informacion(self):
        return (
            f"{super().mostrar_informacion()}\n"
            f"Tipo: Automóvil\n"
            f"Número de puertas: {self.numero_puertas}\n"
            f"Motor: {self.motor.tipo} ({self.motor.potencia} HP)"
        )


class Motocicleta(Vehiculo):
    """Subclase para motocicletas."""

    def __init__(self, marca, modelo, anio, placa, color, motor, cilindrada):
        super().__init__(marca, modelo, anio, placa, color, motor)
        if not isinstance(cilindrada, (int, float)) or cilindrada <= 0:
            raise ValueError("La cilindrada debe ser positiva.")
        self.cilindrada = cilindrada

    def describir(self):
        return "Este registro corresponde a una motocicleta."

    def mostrar_informacion(self):
        return (
            f"{super().mostrar_informacion()}\n"
            f"Tipo: Motocicleta\n"
            f"Cilindrada: {self.cilindrada} cc\n"
            f"Motor: {self.motor.tipo} ({self.motor.potencia} HP)"
        )


class RegistroAutomotriz:
    """Administra una colección de objetos Vehiculo."""

    def __init__(self, nombre="Sistema de Registro Automotriz"):
        self.nombre = nombre
        self.vehiculos = []

    def registrar_vehiculo(self, vehiculo):
        if not isinstance(vehiculo, Vehiculo):
            raise TypeError("Solo se pueden registrar objetos Vehiculo.")
        if self.buscar_vehiculo(vehiculo.placa) is not None:
            raise ValueError(f"La placa {vehiculo.placa} ya está registrada.")
        self.vehiculos.append(vehiculo)
        return (
            f"{vehiculo.marca} {vehiculo.modelo} registrado "
            f"con placa {vehiculo.placa}."
        )

    def buscar_vehiculo(self, placa):
        placa = placa.strip().upper()
        for vehiculo in self.vehiculos:
            if vehiculo.placa == placa:
                return vehiculo
        return None

    def mostrar_vehiculos(self):
        if not self.vehiculos:
            return "No hay vehículos registrados."
        # Polimorfismo: cada subclase presenta su propia información.
        return "\n\n".join(v.mostrar_informacion() for v in self.vehiculos)

    def encender_vehiculo(self, placa):
        vehiculo = self.buscar_vehiculo(placa)
        if vehiculo is None:
            return f"No se encontró el vehículo {placa}."
        return vehiculo.motor.encender()

    def apagar_vehiculo(self, placa):
        vehiculo = self.buscar_vehiculo(placa)
        if vehiculo is None:
            return f"No se encontró el vehículo {placa}."
        vehiculo.detener()
        return vehiculo.motor.apagar()

    def acelerar_vehiculo(self, placa, incremento=20):
        vehiculo = self.buscar_vehiculo(placa)
        if vehiculo is None:
            return f"No se encontró el vehículo {placa}."
        return vehiculo.acelerar(incremento)

    def cantidad_vehiculos(self):
        return len(self.vehiculos)

    def contar_por_tipo(self):
        return {
            "automoviles": sum(isinstance(v, Automovil) for v in self.vehiculos),
            "motocicletas": sum(isinstance(v, Motocicleta) for v in self.vehiculos)
        }
