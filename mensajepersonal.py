mensaje = "Hola mi cristobal ¿Te gustaria aprender python hoy?"
print(mensaje)

mensaje2 = "cristobal"
##Prueba de impresion de mensaje mayuscula inicial
print(mensaje2.title())
##Prueba de impresion de mensaje todas mayusculas 
print(mensaje2.upper())
##Prueba de impresion de mensaje todo en minusculas
print(mensaje2.lower())

##Prueba de impresion de cia celebre

persona_famosa = "Albert Einstein"

mensaje = f'{persona_famosa} dijo una vez "Una persona que nunca cometio un error, nunca intento nada nuevo"'
print(mensaje)

x = "\tte amo mucho"
#el \t sirve para dar un tabulador
x2 = "\nte amo mucho kitobal"
#el \n sirve para dar un salto de linea
print(x) 
print(x.lstrip())
#Esto sirve para imprimir dando un salto de linea :3
print(x2.rstrip())
#esto sirve para imprimir sin espacios
print(x2.strip())