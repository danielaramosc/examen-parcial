def eliminar_termino(polinomio1, termino):
    mayor = polinomio1.termino_mayor
    if mayor.info.termino == termino:
        polinomio1.termino_mayor = polinomio1.termino_mayor.sig
    else:
        aux = Polinomio()
        while mayor is not None:
            if mayor.info.termino != termino:
                agregar_termino(aux,mayor.info.termino,mayor.info.valor)
            mayor = mayor.sig
        polinomio1 = aux

def existe_termino(polinomio,termino):
    mayor = polinomio.termino_mayor
    existe = False
    while mayor is not None and existe == False:
        if mayor.info.termino == termino:
            existe = True
    return existe


    