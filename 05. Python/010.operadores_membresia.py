#esto esta dentro de otro texto o  un elemento dentro de una lista
#comprueba si un valor es miembro de una secuencia string o estructura de datos



#in
print("java" in "curso avanzado de java com spring") #True
print("java" in "curso avanzado de python com Flask")#False


#in en listas
students = ['jehiel','judith','silvia','lili']
name = input('introduce tu nombre: ')


if name in students:
    print('tienes acceso al curso de Java')
else: 
    print('No eres Vip.')

#not in 