from random import randint



class Alumno():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno {} se ha creado con existo".format(nombre))

    def calificacion(self):
        if self.nota >= 5:
            print("El alumno {} ha aprobado".format(self.nombre))
        else:
            print("El alumno {} ha suspendido".format(self.nombre))            

    def __str__(self):
        return "Nombre: {}, Nota: {}".format(self.nombre,self.nota)



numero_random = randint(5,10)
lista = []
for i in range(numero_random):
    alum = Alumno("Alumno{}".format(i), randint(0,10))
    lista.append(alum)

for alumno in lista:
    print(alumno)


