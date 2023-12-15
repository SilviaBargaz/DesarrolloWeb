vehiculos = ['Mercedes', 'Lambo', 'Tractor John Deere', 'Bici Orbea', 'Patinete'] 
#iterar con bucle for y si el vehiculo contiene "tractor" entonces imprimir y salir

#BREAK : while y for ( rompe la ejecución y sale del bucle)
#vehiculo # vehiculos = es lo que quiero iterar
for vehiculo in vehiculos:
    if 'tractor' in vehiculo.lower():  # Utilizando lower() para hacer la comparación sin distinguir mayúsculas y minúsculas
        print(f'tractor encontrado : {vehiculo}')
        break
    

