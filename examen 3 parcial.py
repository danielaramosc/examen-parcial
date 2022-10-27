class Producto():
    def __init__(self,codigo,nombre,precio,tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print("Se ha creado el producto {} con exito".format(self.nombre))
    def __str__(self):
        return "Codigo: {}, Nombre: {}, Precio: {}, Tipo: {}".format(self.codigo,self.nombre,self.precio,self.tipo)

producto1 = Producto("33","Coche de juguete",10.2,"Juguetes")
producto2 = Producto("56","Manzana",1,"Frutas")
producto3 = Producto("1","Pizza",3.5,"Comida Congelada")

print(producto1)
print(producto2)
print(producto3)

producto1.precio = 30
print(producto1)