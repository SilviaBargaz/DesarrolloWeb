coches = ['mercedes', 'bmw', 'skoda', 'alfa romeo' , 'kia']
          #short() ordena de forma Ascendente, de menos a más A-Z
          
coches.sort()
print(coches) 
#short ( reverse = true) ordena de forma DESCENDENTE, de más a menos Z - A
coches.sort(reverse=True)
print(coches) 

#reverse ( ) equivalente a .sort (reverse=true)
# (method) def reverse() -> None no devuelve nada 
coches2 = ['mercedes', 'bmw', 'skoda', 'alfa romeo' , 'kia']
coches2.reverse()
print(coches2)  # invierte el orden de los elementos en torno al centro
#['skoda', 'mercedes', 'kia', 'bmw', 'alfa romeo']

#sorted () la diferencia es que este no modifica la original
#devuelve una nueva lista con los elementos ordenados
precios = [1.11,2.22,3.33,7.77,4.44,6.66]
precios_asc = sorted(precios)
print(precios)
print(precios_asc)

#sorted(reverse=True)
#ordena de forma descendente 
calificaciones = [1.11,2.22,3.33,7.77,4.44,6.66]
calificaciones_desc = sorted(calificaciones, reverse=True)
print(calificaciones_desc)


calificacion_maxima = calificaciones_desc[0] #el primero
calificacion_maxima = calificaciones_desc [-1] #el ultimo

#otra opción para obtener el último:
calificacion_maxima = calificaciones_desc[0] # El primero
calificacion_minima = calificaciones_desc[-1] # El último
# otra opción para obtener el último:
last_index = len(calificaciones_desc) - 1 
calificacion_minima = calificaciones_desc[last_index]



        