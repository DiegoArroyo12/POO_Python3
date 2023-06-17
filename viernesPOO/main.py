from cosas import *

def main():
    per1 = Persona("Diego", 19)
    print(per1)
    print(Persona.descripcion)

    print("----- Herencia Alumno -----")
    al1 = Alumno("Diego", 19, "319169812", "ICO")
    print(al1)
    print(Alumno.descripcion)

    print("----- Constructor Defecto Alumno -----")
    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("----- Herencia Profesor -----")
    profe1 = Profesor("Jesús", 30 + 16, 363565, "Ingeniería de Software")
    print(profe1)
    profe1.dormir()

    print("----- Herencia Ayudante Profesor -----")
    ayudante = AyudanteProfesor("Adrián", 20, "25252", "ICO", 23223, "Ingeniería de Software", 4)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.area = "Ingeniería en Computación"
    ayudante.dar_clase("POO")

main()