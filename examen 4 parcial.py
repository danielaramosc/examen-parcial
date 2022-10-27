from random import randint


lista_letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.',',']

pairs_enc = []
pairs_dec = []
for letra in lista_letras:
    codificado = ""
    for i in range(8):
        codificado = codificado + chr(randint(32,125))
    pairs_enc.append((letra,codificado))
    pairs_dec.append((codificado,letra))

hash_enc = dict(pairs_enc)
hash_dec = dict(pairs_dec)

mensaje = "mi mama me mima"

def encript(mensaje,hash):
    msn = ""
    for l in mensaje:
        msn = msn + hash.get(l,'_')
    return msn

def decript(mensaje,hash_d):
    msn = ""
    for i in range(0,len(mensaje),8):
        letras = mensaje[i:i+8]
        msn = msn + hash_d.get(letras,'*')
    return msn

encriptado = encript(mensaje,hash_enc)
print(encriptado)
desencriptado = decript(encriptado,hash_dec)
print(desencriptado)


#opcional
print(hash_enc)
print(hash_dec)