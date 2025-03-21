# Definimos la clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn):
        # Constructor de la clase Libro. Inicializa los atributos título, autor, isbn y disponible.
        self.titulo = titulo  # Título del libro
        self.autor = autor    # Autor del libro
        self.isbn = isbn      # ISBN del libro
        self.disponible = True  # Inicialmente disponible

    # Método_ agregar() que permite introducir un nuevo libro con sus características.
    def agregar(self, titulo, autor, isbn):
        return Libro(titulo, autor, isbn)

    #Método_ que cambie el estado de disponible a False si el libro está disponible, y muestre un mensaje si ya está prestado.
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' se ha prestado ")
        else:
            print(f"Error: El libro '{self.titulo}' ya está prestado.")

    #Método_ que cambie el estado de disponible a True si estaba prestado, y muestre un mensaje si ya estaba disponible.
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' se ha devuelto.")
        else:
            print(f"Error: El libro '{self.titulo}' ya está disponible.")

    #Método_ que devuelva una lista con todos los libros de la biblioteca y los muestre en pantalla con todos sus datos y diga si estás disponible o no.
    def mostrar(self):
        estado = "Disponible: Sí" if self.disponible else "Disponible: No"
        return f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Estado: {estado}"


    #Método_ que busque un libro en concreto por su ISBN y lo muestre en pantalla con todos sus datos y diga si está disponible o no.
    def buscar(libros, isbn):
       for libro in libros:
            if libro.isbn == isbn:
                return libro
       return None

    # Método_ que muestra el menú y gestiona las opciones.
def menu():
    # Lista donse se almacenan los libros
    inventario = []

    # Mostrar el menú
    while True:
        print("\n--- Bienvenido al Sistema de Gestión de Biblioteca ---")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar")
        print("6. Salir")

        # Pedimos al usuario que elija una opción
        opcion = input("Elige una opción: ")

        # Agregar un nuevo libro usando el método_ agregar()
        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            nuevo_libro = Libro("", "", "").agregar(titulo, autor, isbn)
            # Usamos el método_ agregar
            inventario.append(nuevo_libro)
            print(f"Libro '{titulo}' agregado con éxito.")

        elif opcion == "2":
            # Prestar un libro
            isbn = input("Ingresa el ISBN del libro a prestar: ")
            libro = Libro.buscar(inventario, isbn)
            if libro:
                libro.prestar()
            else:
                print("Error: No se encontró ningún libro con ese ISBN.")

        elif opcion == "3":
            # Devolver un libro
            isbn = input("Ingresa el ISBN del libro a devolver: ")
            libro = Libro.buscar(inventario, isbn)
            if libro:
                libro.devolver()
            else:
                print("Error: No se encontró ningún libro con ese ISBN.")

        elif opcion == "4":
            # Mostrar todos los libros
            if inventario:
                print("\n--- Lista de libros ---")
                for libro in inventario:
                    print(libro.mostrar())
            else:
                print("No hay libros registrados en la biblioteca.")

        elif opcion == "5":
            # Buscar un libro por ISBN
            isbn = input("Ingresa el ISBN del libro a buscar: ")
            libro = Libro.buscar(inventario, isbn)
            if libro:
                print(libro.mostrar())
            else:
                print("Error: No se encontró ningún libro con ese ISBN.")

        elif opcion == "6":
            # Salir del programa
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            # Opción inválida
            print("Opción inválida. Por favor, elige una opción del 1 al 6.")


# Llamamos a la función menú
menu()