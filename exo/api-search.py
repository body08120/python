import requests  # Importation du module requests pour effectuer des requêtes HTTP.

url = 'https://images.ctfassets.net/hrltx12pl8hq/28ECAQiPJZ78hxatLTa7Ts/2f695d869736ae3b0de3e56ceaca3958/free-nature-images.jpg?fit=fill&w=1200&h=630'
# Définition de l'URL de l'image à télécharger.
# On place l'URL dans une variable pour simplifier la maintenance du code

# try:  # Début d'un bloc try-except pour capturer et gérer les execptions.
#     response = requests.get(url, timeout=10)  
#     # Effectue une requête GET à l'URL spécifiée avec un délai maximum de 10 secondes.
#     # Le timeout est crucial pour éviter que le programme reste bloqué si le serveur ne répond pas.
    
#     response.raise_for_status()  
#     # Vérifie si le serveur a retourné un code HTTP d'erreur (comme 404 ou 500).
#     # Cela permet de détecter rapidement les problèmes et d'arrêter l'exécution en cas d'échec.

#     with open('image.jpg', 'wb') as f:  
#         # Ouvre un fichier en mode écriture binaire (`wb`) pour sauvegarder l'image.
#         # Le mode binaire est utilisé car les images ne sont pas des fichiers texte.
#         f.write(response.content)  
#         # Écrit le contenu brut de la réponse HTTP (l'image) dans le fichier.
#         # `response.content` retourne les données sous forme binaire.

#     print("Image téléchargée avec succès !")  
#     # Message pour confirmer que le téléchargement et l'enregistrement ont été effectués.

# except requests.exceptions.RequestException as e:  
#     # Capture toutes les exceptions liées à requests (ex. : timeout, problème réseau).
#     print(f"Erreur lors du téléchargement : {e}")  
#     # Affiche un message d'erreur détaillé pour aider au débogage.

url = "https://www.nataelwebdesigner.fr/index.php"

try:
    response = requests.get(url, timeout=10)
    
    response.raise_for_status()
    
    with open ('test.txt', 'wb') as f:
        
        f.write(response.content)
        
    print("Écriture du fichier est passer")
    
except requests.exceptions.RequestException as o:
    
    print('erreur lors du lancement du script')