"""Ejecución y pruebas del Sistema de Registro Automotriz."""

from modelos import Motor, Automovil, Motocicleta, RegistroAutomotriz


if __name__ == "__main__":
    print("=" * 55)
    print("             SISTEMA DE REGISTRO AUTOMOTRIZ")
    print("=" * 55)

    # Crear motores.
    motor_corolla = Motor("Gasolina", 150)
    motor_civic = Motor("Gasolina", 158)
    motor_yamaha = Motor("Gasolina", 100)

    # Crear vehículos.
    auto1 = Automovil(
        "Toyota", "Corolla", 2022, "ABC-123-A",
        "Blanco", motor_corolla, 4
    )
    auto2 = Automovil(
        "Honda", "Civic", 2023, "DEF-456-B",
        "Gris", motor_civic, 4
    )
    moto1 = Motocicleta(
        "Yamaha", "FZ", 2021, "GHI-789-C",
        "Azul", motor_yamaha, 150
    )

    # Composición: el registro contiene vehículos.
    registro = RegistroAutomotriz()
    print("\n--- REGISTRO DE VEHÍCULOS ---")
    for vehiculo in (auto1, auto2, moto1):
        print(registro.registrar_vehiculo(vehiculo))

    print(f"\nTotal registrados: {registro.cantidad_vehiculos()}")

    # Herencia y polimorfismo.
    print("\n--- INFORMACIÓN DE LOS VEHÍCULOS ---")
    print(registro.mostrar_vehiculos())

    print("\n--- DESCRIPCIONES POLIMÓRFICAS ---")
    for vehiculo in (auto1, auto2, moto1):
        print(f"{vehiculo.placa}: {vehiculo.describir()}")

    # Delegación: el registro localiza el vehículo y utiliza sus métodos.
    print("\n--- OPERACIONES DEL SISTEMA ---")
    print(registro.encender_vehiculo("ABC-123-A"))
    print(registro.acelerar_vehiculo("ABC-123-A", 40))
    print(registro.acelerar_vehiculo("ABC-123-A", 20))
    print(auto1.frenar(30))
    print(registro.apagar_vehiculo("ABC-123-A"))

    # Búsqueda por placa.
    print("\n--- BÚSQUEDA POR PLACA ---")
    encontrado = registro.buscar_vehiculo("GHI-789-C")
    if encontrado:
        print(encontrado.mostrar_informacion())
    else:
        print("No se encontró el vehículo.")

    # Encapsulamiento: consultar velocidad mediante la propiedad.
    print("\n--- ENCAPSULAMIENTO ---")
    print(f"Velocidad consultada: {auto1.velocidad} km/h")

    # Resumen.
    print("\n--- RESUMEN DEL REGISTRO ---")
    resumen = registro.contar_por_tipo()
    print(f"Automóviles: {resumen['automoviles']}")
    print(f"Motocicletas: {resumen['motocicletas']}")
    print(f"Total: {registro.cantidad_vehiculos()}")
    print("\nPruebas finalizadas correctamente.")
