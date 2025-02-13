## 1. Definir la clase Alumno y sus atributos:
class Alumno():
    # Construtor
    def __init__(self, nombre='', p_apellido='', dni='', correo=''):
        self.__nombre = nombre
        self.__p_apellido = p_apellido
        self.__dni = dni
        self.__correo = correo

    # Getters de un atributo específico
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__p_apellido

    def get_dni(self):
        return self.__dni

    def get_correo(self):
        return self.__correo

    #Setters de un atributo específico
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, p_apellido):
        self.__p_apellido = p_apellido

    def set_dni(self, dni):
        self.__dni = dni

    def set_correo(self, correo):
        self.__correo = correo

    ## 2.a Método que imprime por pantalla todos los atributos del Alumno
    def print_alumno(self):
        print('\n# ------------ Datos del Alumno ------------ #')
        for atributo, valor in self.__dict__.items():
            print(f'>> {atributo}: {valor}')

## 2.b Método que devuelve un alumno nuevo con los valores que se inserten por teclado
def nuevo_alumno():
    print('# ------------ Nuevo Alumno ------------ #')
    nombre = input('>> Inserta el nombre del alumno: ')
    p_apellido = input('>> Inserta el primer apellido del alumno: ')
    dni = input('>> Inserta el DNI del alumno: ')
    correo = input('>> Inserta el email del alumno: ')
    return Alumno(nombre,p_apellido, dni, correo)

## 3. Crear una clase Alumno_IA que herede de Alumno y añadir atributos específicos
class AlumnoIA(Alumno):
    # Constructor
    def __init__(
        self, nombre='', 
        p_apellido='', 
        dni='', 
        correo='',
        grupo_teoria='', 
        grupo_pratica='', 
        nota_pratica_1=0, 
        nota_pratica_2=0, 
        nota_pratica_3=0, 
        nota_pratica_4=0
    ):
        # Heredar atributos de la clase Alumno
        super().__init__(nombre, p_apellido, dni, correo)
        
        # Atributos específicos de la clase Alumno_IA
        self.__grupo_teoria = grupo_teoria
        self.__grupo_pratica = grupo_pratica
        self.__nota_pratica_1 = nota_pratica_1
        self.__nota_pratica_2 = nota_pratica_2
        self.__nota_pratica_3 = nota_pratica_3
        self.__nota_pratica_4 = nota_pratica_4

    # Getters de un atributo específico
    def get_grupo_teoria(self):
        return self.__grupo_teoria

    def get_grupo_practicas(self):
        return self.__grupo_pratica

    def get_nota_p1(self):
        return self.__nota_pratica_1

    def get_nota_p2(self):
        return self.__nota_pratica_2

    def get_nota_p3(self):
        return self.__nota_pratica_3

    def get_nota_p4(self):
        return self.__nota_pratica_4

    #Setters de un atributo específico
    def set_grupo_teoria(self, grupoT):
        self.__grupo_teoria = grupoT

    def set_grupo_practicas(self, grupoP):
        self.__grupo_pratica = grupoP

    def set_nota_p1(self, notaP1):
        self.__nota_pratica_1 = notaP1

    def set_nota_p2(self, notaP2):
        self.__nota_pratica_2 = notaP2

    def set_nota_p3(self, notaP3):
        self.__nota_pratica_3 = notaP3

    def set_nota_p4(self, notaP4):
        self.__nota_pratica_4 = notaP4
    
    ## 4. Leer, actualizar y calcular la media de las notas
    def calcular_nota_practica(self):
        print('\n# ------------ Notas prácticas de IA del alumno ------------ #')
        self.__nota_pratica_1 = float(input('>> Inserta la nota práctica 1 del alumno: '))
        self.__nota_pratica_2 = float(input('>> Inserta la nota práctica 2 del alumno: '))
        self.__nota_pratica_3 = float(input('>> Inserta la nota práctica 3 del alumno: '))
        self.__nota_pratica_4 = float(input('>> Inserta la nota práctica 4 del alumno: '))
        
        print('\n# ------------ Media de las notas del alumno ------------ #')
        media = (self.__nota_pratica_1 + self.__nota_pratica_2 + self.__nota_pratica_3 + self.__nota_pratica_4)/4

        print(media)
        return media

## 5. Lectura de los datos del los alumnos desde un fichero y exporte de aquellos que tienen DNI impares para otro fichero
with open('datos.txt', mode='r') as datos:
    lineas = datos.readlines()
    with open('impares.txt', mode = 'w') as impares:
        for x in lineas:
            division = x.strip().split(", ")
            if int(division[1])%2 != 0:
                impares.write(x)
