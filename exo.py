print("Bienvenue les men's in black")

while True: 
    try: 
        pv = int(input('Saissisez votre nombre de PV : ')) 
        if pv < 0: 
            print("Désolé, le nombre de PV doit être un entier positif. Veuillez réessayer.")  
            continue 
        break 
    except ValueError: 
        print("Erreur : Veuillez entrer un nombre entier pour les PV.")

try:
    degat = int(input('Saissisez le nombre de dégât que vous allez subir : '))
except ValueError:
    print("Erreur : Veuillez entrer un nombre entier pour les PV.")

result = pv - degat

print(f"Le résultat est : ",result)