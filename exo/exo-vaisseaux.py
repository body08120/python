print('Vous devez créer 3 vaisseaux, nous vous dirons lequel est le plus rentable')

vaisseaux = []

for vaisseau_num in range(3):
    print(f'Création du vaisseau {vaisseau_num+1} :')
    # Récupérer les valeurs de l'utilisateur
    name = input('NOM :')
    color = input('COULEUR :')
    nb_passager = int(input('NB PASSAGER :'))
    nb_max_passager = int(input('NB PASSAGER MAX :'))
    
    # Stocker les valeurs
    vaisseau = {
        'name': name,
        'color': color,
        'nb_passager': nb_passager,
        'nb_max_passager': nb_max_passager,
    }
    vaisseaux.append(vaisseau)

# Afficher les informations des vaisseaux
print(vaisseaux)

# Calculer le taux de remplissage, c'est-à-dire le plus grand rapport nombre_de_passagers / nombre_de_places_disponibles.
top_vaisseau = None
top_taux = 0

for vaisseau in vaisseaux:
    taux = vaisseau['nb_passager'] / vaisseau['nb_max_passager']
    if taux > top_taux:
        top_taux = taux
        top_vaisseau = vaisseau

# Afficher le vaisseau avec le meilleur taux de remplissage
if top_vaisseau:
    print(f'Le vaisseau avec le meilleur taux de remplissage est {top_vaisseau["name"]} avec un taux de {top_taux:.2f}.')

# class Vaisseau:
#     def __init__(self, name, color, nb_passager, nb_max_passager):
#         self.name = name
#         self.color = color
#         self.nb_passager = nb_passager
#         self.nb_max_passager = nb_max_passager
    
#     def taux_remplissage(self):
#         return self.nb_passager / self.nb_max_passager

# # Créer les vaisseaux
# vaisseaux = []
# for i in range(3):
#     print(f"Création du vaisseau {i+1} :")
#     name = input('NOM :')
#     color = input('COULEUR :')
#     nb_passager = int(input('NB PASSAGER :'))
#     nb_max_passager = int(input('NB PASSAGER MAX :'))
#     vaisseaux.append(Vaisseau(name, color, nb_passager, nb_max_passager))

# # Trouver le vaisseau avec le meilleur taux de remplissage
# top_vaisseau = max(vaisseaux, key=lambda v: v.taux_remplissage())
# print(f'Le vaisseau avec le meilleur taux de remplissage est {top_vaisseau.name} avec un taux de {top_vaisseau.taux_remplissage():.2f}.')
