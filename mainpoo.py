from cosas import Alumno, Perro

def main():
    al1 = Alumno("Jose", 19, "ICO")
    print(vars(al1))
    al1.__nombre = "Diego"
    print(vars(al1))
    al1.set_nombre("María")
    print(vars(al1))
    print("----- To String -----")
    print(al1)
    al1.set_edad(999)
    print(al1)
    al1.estudiar(4)
    print("----- PERRO -----")
    perro1 = Perro("Poddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "De la calle" # set en notación Python
    print(vars(perro1))
    perro1.__raza = "Otra"
    print(vars(perro1))
    perro1.edad = 12
    perro1.estatura = 0.43
    print(perro1)

    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()

    danes = Perro.perro_grande(0.8)
    print(danes)

    obj1 = Perro("Pug", 1, 0.4)
    obj2 = Perro.perro_grande(0.9)
    obj3 = Perro.constructor_dos("French", 2)

    print(obj1)
    print(obj2)
    print(obj3)

main()