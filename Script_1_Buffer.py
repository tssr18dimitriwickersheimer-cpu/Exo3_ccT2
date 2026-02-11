import os # Importation du module os pour vérifier l'existence du fichier et manipuler les chemins de fichiers

def lire_et_stocker_buffer(chemin_fichier): # Définition de la fonction qui lit un fichier et le stocke dans un buffer (en mémoire)

    if not os.path.exists(chemin_fichier): # Vérifie si le fichier existe à l'emplacement spécifié
        raise FileNotFoundError(f"Le fichier '{chemin_fichier}' n'existe pas.") # Si le fichier n'existe pas, une exception FileNotFoundError est levée avec un message d'erreur approprié

    with open(chemin_fichier, 'rb') as fichier: # Ouverture du fichier en mode binaire ('rb') pour lire les données brutes
        
        buffer = fichier.read() # Lecture du contenu du fichier dans un buffer (objet bytes)

    return buffer  # Retourne le buffer contenant les données du fichier

if __name__ == "__main__": # Bloc principal du script qui s'exécute lorsque le script est exécuté directement (et non importé comme module)

    chemin_vers_fichier = r"C:\Users\DIMI\Desktop\esgi\cours\python mme Oulmi\CC T2 Python - Exo3\Exo3_ccT2\Copie_2.txt" # ici j'utilise un chemin absolu pour éviter les problèmes de localisation de mon fichier.

    try: # Appel de la fonction pour lire le PDF dans un buffer
       
        contenu_buffer = lire_et_stocker_buffer(chemin_vers_fichier) # Stockage du contenu du PDF dans un buffer (variable contenu_buffer)

        # Affichage des 50 premiers octets pour éviter de surcharger la console
        print(f"--- Lecture réussie ---")# Affichage d'un message pour indiquer que les 50 premiers octets du buffer vont être affichés
        print(f"Taille du buffer : {len(contenu_buffer)} octets") # Affichage de la taille totale du buffer en octets pour donner une idée de la quantité de données lues à partir du fichier

    except FileNotFoundError as e: # Gestion de l'exception FileNotFoundError qui peut être levée si le fichier n'existe pas à l'emplacement spécifié. Le message d'erreur est affiché pour informer l'utilisateur du problème.
        print(f"Erreur : {e}") # Affichage du message d'erreur si le fichier n'est pas trouvé, informant l'utilisateur de la nature du problème (fichier manquant) et de l'emplacement spécifié.
    except PermissionError: # Gestion de l'exception PermissionError qui peut être levée si l'utilisateur n'a pas les droits nécessaires pour lire le fichier. Un message d'erreur est affiché pour informer l'utilisateur du problème de permissions.
        print("Erreur : Vous n'avez pas les droits pour lire ce fichier.") # Affichage d'un message d'erreur si l'utilisateur n'a pas les permissions nécessaires pour lire le fichier, informant l'utilisateur du problème de permissions et de la nécessité d'obtenir les droits appropriés pour accéder au fichier.