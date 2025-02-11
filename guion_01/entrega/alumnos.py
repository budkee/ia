## 1. Definir la clase Alumno y sus atributos:
class Alumno():
    
    # Construtor
    def __init__(self, nombre='', p_apellido='', dni='', correo=''):
        self.nombre = nombre
        self.p_apellido = p_apellido
        self.dni = dni
        self.correo = correo

    # Pillar un atributo específico
    def get_atributo(self, atributo):
        return getattr(self, atributo, None)  

    ## 2. Crear un método que permita crear un nuevo alumno inserindo los datos por consola  
    @classmethod 
    def nuevo_alumno(obj):
        print('# ------------ Nuevo Alumno ------------ #')
        nombre = input('>> Insira el nombre del alumno: ')
        p_apellido = input('>> Insira el primer apellido del alumno: ')
        dni = input('>> Insira el DNI del alumno: ')
        correo = input('>> Insira el email del alumno: ')
        return obj(nombre, p_apellido, dni, correo)
    
    def get_alumno(self):
        print('\n# ------------ Datos del Alumno ------------ #')
        for atributo, valor in self.__dict__.items():
            print(f'>> {atributo}: {valor}')

## 3. Crear una clase Alumno_IA que herede de Alumno y añadir atributos específicos
class Alumno_IA(Alumno):
    
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
        self.grupo_teoria = grupo_teoria
        self.grupo_pratica = grupo_pratica
        self.nota_pratica_1 = nota_pratica_1
        self.nota_pratica_2 = nota_pratica_2
        self.nota_pratica_3 = nota_pratica_3
        self.nota_pratica_4 = nota_pratica_4

    # Pillar atributos especificos
    def get_atributo(self, atributo):
        return getattr(self, atributo, None)  

    # Anãdir más detalles del alumno 
    def anadir_detalles(self):
        print('\n# ------------ Más detalles del alumno de IA ------------ #')
        self.grupo_teoria = input('>> Insira el grupo teórico del alumno: ')
        self.grupo_pratica = input('>> Insira el grupo práctico del alumno: ')
    
    ## 4. Leer, actualizar y calcular la media de las notas
    def calcular_nota_practica(self):
        print('\n# ------------ Notas prácticas de IA del alumno ------------ #')
        self.nota_pratica_1 = float(input('>> Insira la nota práctica 1 del alumno: '))
        self.nota_pratica_2 = float(input('>> Insira la nota práctica 2 del alumno: '))
        self.nota_pratica_3 = float(input('>> Insira la nota práctica 3 del alumno: '))
        self.nota_pratica_4 = float(input('>> Insira la nota práctica 4 del alumno: '))
        
        print('\n# ------------ Media de las notas del alumno ------------ #')
        media = (self.nota_pratica_1 + self.nota_pratica_2 + self.nota_pratica_3 + self.nota_pratica_4)/4

        return print(media)

    def get_alumno_ia(self):
        print('\n# ------------ Datos del Alumno de IA ------------ #')
        for atributo, valor in self.__dict__.items():
            print(f'>> {atributo}: {valor}')

## 5. Leitura de los datos del los alumnos desde un fichero y exporte de aquellos que tienen DNI impares para otro fichero
with open('datos.txt', mode='r') as datos:
    
    # Poner las lineas en una lista y sus valores en otra lista con list comprehension
    lineas = [[valor.strip() for valor in linea.strip().split(',')] for linea in datos.readlines()]
    # print(lineas[0])

    ## Pillar solo los DNIs ímpares y grabar en un archivo externo
    # print(lineas[0][1])
    # with open('impares.txt', mode='w') as salida:
    #     for linea in lineas:
    #         dni = linea[1]
    #         if dni[-1].isdigit() and int(dni) % 2 != 0:
    #             print(dni, file=salida)


## ----------------- Tests ----------------- 
if __name__ == '__main__':
    ## 1. Instancia del Alumno pasando valores como parámetros
    eu = Alumno(
        nombre="Kaê", 
        p_apellido="de Oliveira", 
        dni="GJ854298", 
        correo="kob00001@red.ujaen.es"
    )
    # print(eu.get_atributo(atributo="p_apellido"))

    ## 2. Crear un nuevo alumno
    # aluno = Alumno.nuevo_alumno()

    # Leer los datos del alumno
    # aluno.get_alumno()

    ## 3. Instancia de la clase Alumno_IA
    # Crear nuevo alumno de IA
    aluno = Alumno_IA.nuevo_alumno()

    # Añadir detalles del alumno de IA
    aluno.anadir_detalles()

    # Leer los datos del alumno
    aluno.get_alumno_ia()

    ## 4. Añadir las notas y calcular la media
    # Calcular la media
    aluno.calcular_nota_practica()