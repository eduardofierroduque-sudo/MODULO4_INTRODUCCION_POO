# 1. Identificación de la clase
# El nombre de la clase siempre empieza con mayúscula en Python (CamelCase).
class Smartphone:
    """
    Representa un teléfono inteligente del mundo real.
    """

    # 2. Definir atributos (Características)
    # El método __init__ es el constructor que inicializa los atributos.
    def __init__(self, marca, modelo, capacidad_bateria):
        self.marca = marca                # Atributo 1
        self.modelo = modelo              # Atributo 2
        self.bateria_actual = capacidad_bateria  # Atributo 3 (Estado inicial)
        self.esta_encendido = False       # Atributo adicional para el estado

    # 2. Definir métodos (Acciones)
    def encender(self):
        self.esta_encendido = True
        print(f"El {self.marca} {self.modelo} se ha encendido.")

    def llamar(self, numero):
        if self.esta_encendido and self.bateria_actual > 0:
            print(f"Llamando al {numero} desde mi {self.modelo}...")
            self.bateria_actual -= 5  # La acción cambia el estado de la batería
        else:
            print("No se puede llamar. Teléfono apagado o sin batería.")

    def cargar(self):
        self.bateria_actual = 100
        print(f"Batería del {self.modelo} cargada al 100%.")

# ---------------------------------------------------------
# 3. Diferenciar atributos y estado
# Atributos: 'marca' y 'modelo' son fijos para la vida del objeto.
# Estado: 'bateria_actual' y 'esta_encendido' cambian según las acciones.
# ---------------------------------------------------------

# 4. Explicar instancias y objetos (3 ejemplos concretos)
print("--- Creación de Instancias ---")

# Objeto 1
telefono_personal = Smartphone("Apple", "iPhone 15", 85)
telefono_personal.encender()

# Objeto 2
telefono_trabajo = Smartphone("Samsung", "Galaxy S23", 100)

# Objeto 3
telefono_antiguo = Smartphone("Nokia", "3310", 10)

# Mostrando los diferentes valores (estados) de cada objeto
print(f"Estado Teléfono 1: {telefono_personal.modelo}, Batería: {telefono_personal.bateria_actual}%")
print(f"Estado Teléfono 2: {telefono_trabajo.modelo}, Batería: {telefono_trabajo.bateria_actual}%")
print(f"Estado Teléfono 3: {telefono_antiguo.modelo}, Batería: {telefono_antiguo.bateria_actual}%")