
print("Ingrese los valores:")
print("|M01 M02 M03|")
print("|M04 M05 M06|")
print("|M07 M08 M09|")

M01 = float(input('Ingrese el valor M01: '))
M02 = float(input('Ingrese el valor M02: '))
M03 = float(input('Ingrese el valor M03: '))
M04 = float(input('Ingrese el valor M04: '))
M05 = float(input('Ingrese el valor M05: '))
M06 = float(input('Ingrese el valor M06: '))
M07= float(input('Ingrese el valor M07: '))
M08 = float(input('Ingrese el valor M08: '))
M09 = float(input('Ingrese el valor M09: '))


determinante_M= (M01*M05*M09) + (M04*M08*M03) + (M07*M02*M06) - (M03*M05*M07) - (M06*M08*M01) - (M09*M02*M04)

if determinante_M!=0:
   print ("El determinante de esta matriz es: ",determinante_M)

else:
    print ("El detrrminante de esta matriz es 0")