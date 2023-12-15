
# print(students[4]) # IndexError: list index out of range#Borrar elementos de una lista existente

phones= ['6291029302','604882727','60493829302','6039202910']
#remove () borrar un elemento que pasemos por parámetro

phones.remove('6291029302')
print (phones)

# pop() elimina o devuelve el ultimo elemento de la lista o por su índice
#pop sacan el ultimo de la lista

pendientes_calificacion = [' angel', ' aitor', ' carlos', ' sigueros']
alumno_a_calificar = pendientes_calificacion.pop()
print(f"alumno_a_calificar{alumno_a_calificar} ")

alumno_a_calificar = pendientes_calificacion.pop()
print(f"alumno_a_calificar{alumno_a_calificar} ")

alumno_a_calificar = pendientes_calificacion.pop()
print(f"alumno_a_calificar{alumno_a_calificar} ")

alumno_a_calificar = pendientes_calificacion.pop()
print(f"alumno_a_calificar{alumno_a_calificar} ")

#pop  (0) con el 0 lo especifica
fila_pescaderia =['persona1','persona2','persona3','persona4','persona5','silvia']
persona_a_atender = fila_pescaderia.pop (0)
print(f"persona_a_atender {persona_a_atender}") #persona1

persona_a_atender = fila_pescaderia.pop (0)
print(f"persona_a_atender {persona_a_atender}") #persona2

persona_a_atender = fila_pescaderia.pop (0)
print(f"persona_a_atender {persona_a_atender}") #persona3

persona_a_atender = fila_pescaderia.pop (0)
print(f"persona_a_atender {persona_a_atender}") #persona4


#del permite borrar un elemento concreto sin devolverlo
#ejemplo: productor de un ecommerce, en el checkout antes de finalizar la compra
precios = [5.99, 12.32, 10.00, 48.57]
del precios [2]
print(precios)


#Calcular longitud listas con el método len()


print(len(precios))

# En Java
# arrays .length
# ArrayList .size() 



