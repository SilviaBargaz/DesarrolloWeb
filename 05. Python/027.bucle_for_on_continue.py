vehiculos = ['mercedes rojo','bmw gris','tractor azul','tractor rosa','patinete azul']

#hacer un bucle for que itere imprimiendo cada vehiculo y si es de 
#color azul salta a la siguiente iteracion
#usar continue


for vehiculo in vehiculos:
    if 'azul' in vehiculo.lower():  # Utilizando lower() para hacer la comparación sin distinguir mayúsculas y minúsculas
        
        continue #se utiliza en Python para pasar a la siguiente iteración de un bucle (while o for)
    
    print(vehiculo) #solo imprime el vehiculo que NO es azul
    #a diferencia de break que rompe el bucle,
    #continue se mantiene dentro para salta a la siguiente iteracion
    