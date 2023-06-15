from cosas import Autor, Libro, Persona, Alumno

def main():
    l1 = Libro.libro_planeta("El perfume", Autor("Patrick", "PS"),1980)
    print(l1)
    # El código para cambiar el pseudónimo
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)
    print("----- Herencia -----")
    al2 = Alumno("José", 19, 319169813, "ICO", 9)
    al2.nombre = "Diego"
    print(vars(al2))

main()