class Libro:
    def __init__(self, titulo, autor, genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__disponible = True
    
    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def genero(self):
        return self.__genero

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, valor):
        self.__disponible = valor


class Biblioteca:
    def __init__(self):
        self.__libros = []
    
    def agregar_libro(self, libro):
        self.__libros.append(libro)
    
    def buscar_libro(self, titulo):
        for libro in self.__libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None
    
    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro and libro.disponible:
            libro.prestar()
            return f'El libro "{titulo}" ha sido prestado.'
        return f'El libro "{titulo}" no está disponible o no existe en la biblioteca.'
    
    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            libro.devolver()
            return f'El libro "{titulo}" ha sido devuelto.'
        return f'El libro "{titulo}" no existe en la biblioteca.'

    @staticmethod
    def buscar_por_genero(libros, genero):
        return [libro for libro in libros if libro.genero.lower() == genero.lower()]
    
    @property
    def libros(self):
        return self.__libros


def menu():
    biblioteca = Biblioteca()
    
    while True:
        print("\n--- Menú Biblioteca ---")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar libros por género")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            libro = Libro(titulo, autor, genero)
            biblioteca.agregar_libro(libro)
            print(f'Libro "{titulo}" agregado a la biblioteca.')
        
        elif opcion == '2':
            titulo = input("Título: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                estado = "disponible" if libro.disponible else "no disponible"
                print(f'Título: {libro.titulo}\nAutor: {libro.autor}\nGénero: {libro.genero}\nEstado: {estado}')
            else:
                print(f'Libro "{titulo}" no encontrado.')
        
        elif opcion == '3':
            titulo = input("Título: ")
            mensaje = biblioteca.prestar_libro(titulo)
            print(mensaje)
        
        elif opcion == '4':
            titulo = input("Título: ")
            mensaje = biblioteca.devolver_libro(titulo)
            print(mensaje)
        
        elif opcion == '5':
            genero = input("Género: ")
            libros_genero = Biblioteca.buscar_por_genero(biblioteca.libros, genero)
            if libros_genero:
                print(f'Libros del género "{genero}":')
                for libro in libros_genero:
                    estado = "disponible" if libro.disponible else "no disponible"
                    print(f'Título: {libro.titulo}, Estado: {estado}')
            else:
                print(f'No se encontraron libros del género "{genero}".')
        
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")


# Ejecutar el menú
menu()
