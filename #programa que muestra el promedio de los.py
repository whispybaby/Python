#programa que muestra el promedio de los pedos generados a la semana
#lista pedos
pedos = [100,1,2,3,4,5,6]

total = 0
n = 0
for promedio in  pedos:
    total+=promedio
    n+=1

    print ("Pedos promedio por semana:", str (total/n))