#Operadores  de identidad
email = None  
email_user = input('Introduce tu email: ')

#endswith es un metodo para comprobar si termina en gmail
if email_user.endswith('@gmail.com'): 
    email = email_user



#is

if email is None:  # es habitual para saber si existe un valor
    print('no se ha podido completar el registro.')
    
print (1 == True) #True
print (0== True) #false
print (1 is True )# false, compara la identidad
# el IS /es un operador de indetidad (== es un boolean)


#is not
if email is not None: # comprueba que el email no sea nuelo o vacio
    print('El email es correcto, registro completado.')

#if else
if email is None:
    print('no se ha podido completar el registro.')
else:
    print('el email correcto, registro completado.')
    
if email is not None: # comprueba que el email no sea nuelo o vacio
    print('El email es correcto, registro completado.')


