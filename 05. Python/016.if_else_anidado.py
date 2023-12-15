#una estructura dentro de otra estructura if
nivel = 2
puntos = 35

if nivel < 1:
        print ('nivel incorrecto')

if nivel == 1:
    if puntos< 20:
            print('mal comienzo')
    else:
            print('!buen comienzo !')
            
            
elif nivel == 2:
    if puntos< 30:
            print ('podria hacerse mejor para un nivel 2')
    else:
            print('gran avance de nivel')
            
elif nivel == 3:
    if puntos< 40:
            print ('mejorable')
    else:
            print('está perfecto')
    
elif nivel == 4:
    if puntos< 50:
            print ('maquina')
    else:
            print('Más que perfecto')