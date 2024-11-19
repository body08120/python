print("Bienvenue les men's in black")

while True: 
    try: 
        pv = int(input('Saissisez votre nombre de PV : ')) 
        if pv < 0: 
            print("Désolé, il faut une valeur positive")  
            continue 
        break 
    except ValueError: 
        print("Erreur : Veuillez entrer un nombre entier pour les PV.")

while True:
    try:
        degat = int(input('Saissisez le nombre de dégât que vous allez subir : '))
        if degat < 0:
            print('Désolé, il faut une valeur positive')
            continue
        break
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier pour les PV.")

result = pv - degat

print(f"Le résultat est : ",result)