#Importer les modules d'ont on a besoin
import random
import string


# Créer une fonction qui va générer le mot de passe

# On défini la fonction avec les paramètres
def generate_password(lenght=16, use_uppercase=True, use_digits=True, use_symbols=True):
    # On défini ici les paramêtres requis du mot de passe
    characters = string.ascii_lowercase
    
    # Si maj demandé
    if use_uppercase:
        characters += string.ascii_uppercase
        
    # Si int demandé
    if use_digits:
        characters += string.digits
        
    # Si symbole demandé
    if use_symbols:
        characters += string.punctuation
    
    # On génére le mot de passe
    password = ''.join(random.choice(characters) for i in range(lenght))
    
    # On retourne le password final 
            # Vérifier si le mot de passe satisfait tous les critères
    if (not use_uppercase or any(c.isupper() for c in password)) and \
        (not use_digits or any(c.isdigit() for c in password)) and \
        (not use_symbols or any(c in string.punctuation for c in password)):
            print('abc')
            password = generate_password(16, use_uppercase=True, use_digits=True, use_symbols=True)
            
    return password 

password = generate_password(16, use_uppercase=True, use_digits=True, use_symbols=True)
print(password)

# La fonction doit retourner un mot de passe qui respecte les critères donnés 
# (par exemple, un mot de passe de 16 caractères avec au moins une majuscule, un chiffre et un symbole).


# Bonus : Crée une fonction save_password qui sauvegarde ce mot de passe dans un fichier texte sécurisé en utilisant une bibliothèque comme cryptography pour le chiffrement.
# Ajoute des tests pour t'assurer que ton générateur fonctionne comme prévu, par exemple en vérifiant que les critères de complexité sont respectés.