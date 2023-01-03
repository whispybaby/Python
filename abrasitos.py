def abrasitos():
    ##Con input pedimos el valor al usuario 
    cantidad_abrasitos = input("Cuantos abrasitos quieres?")
    try:
        cantidad_abrasitos = int(cantidad_abrasitos)
        print(f"Quiero {cantidad_abrasitos} ")
        cantidad_abrasitos_dados = cantidad_abrasitos-1
        while cantidad_abrasitos_dados>=0:
            print("Te doy un abraso")
            cantidad_abrasitos_dados -=1
            print("satisfecho")        
    except:
        print("Eso no es  un numero")
abrasitos()