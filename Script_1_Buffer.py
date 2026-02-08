import os # Importation du module os pour vérifier l'existence du fichier et manipuler les chemins de fichiers

def lire_pdf_dans_buffer(chemin_fichier): # Définition de la fonction qui lit un fichier PDF et le stocke dans un buffer (en mémoire)

    # Lit le contenu d'un fichier PDF et le stocke dans un buffer (en mémoire). 

    # Args:
        #chemin_fichier (str): Le chemin complet vers le fichier PDF à lire.

    # Returns:
        #bytes: Le contenu du fichier PDF sous forme de buffer (bytes).

 
    if not os.path.exists(chemin_fichier): # Vérifie si le fichier existe à l'emplacement spécifié
        raise FileNotFoundError(f"Le fichier '{chemin_fichier}' n'existe pas.") # Si le fichier n'existe pas, une exception FileNotFoundError est levée avec un message d'erreur approprié

    with open(chemin_fichier, 'rb') as fichier: # Ouverture du fichier en mode binaire ('rb') pour lire les données brutes
        
        buffer = fichier.read() # Lecture du contenu du fichier dans un buffer (objet bytes)

  
    return buffer  # Retourne le buffer contenant les données du fichier PDF


if __name__ == "__main__": # Bloc principal du script qui s'exécute lorsque le script est exécuté directement (et non importé comme module)

    # Exemple d'utilisation
        # Exemple 1 : Chemin relatif (fichier dans le même dossier)
              # chemin_vers_pdf = "cybersec-cisco.pdf"

        # Exemple 2 : Chemin relatif (fichier dans un sous-dossier)
              # chemin_vers_pdf = "documents/cybersec-cisco.pdf"

        # Exemple 3 : Chemin absolu (Windows)

    chemin_vers_pdf = r"\Users\DIMI\Desktop\revision_CCNA\cybersec-cisco.pdf" # ici j'utilise un chemin absolu pour éviter les problèmes de localisation de mon fichier mais il est possible d'utiliser exemple 1 ou 2 en fonction de l'emplacement du fichier PDF sur le système

    try: # Appel de la fonction pour lire le PDF dans un buffer
       
        contenu_buffer = lire_pdf_dans_buffer(chemin_vers_pdf) # Stockage du contenu du PDF dans un buffer (variable contenu_buffer)

        # Affichage des 50 premiers octets pour éviter de surcharger la console
        print("Contenu du buffer (50 premiers octets) :") # Affichage d'un message pour indiquer que les 50 premiers octets du buffer vont être affichés
        print(contenu_buffer[:50]) # Affichage des 50 premiers octets du buffer pour donner un aperçu du contenu sans surcharger la console avec l'intégralité du contenu du PDF, qui peut être très volumineux
        print(f"\nTaille du buffer : {len(contenu_buffer)} octets") # Affichage de la taille totale du buffer en octets pour donner une idée de la quantité de données lues à partir du fichier PDF


    except FileNotFoundError as e: # Gestion de l'exception FileNotFoundError qui peut être levée si le fichier PDF n'existe pas à l'emplacement spécifié. Le message d'erreur est affiché pour informer l'utilisateur du problème.
        print(f"Erreur : {e}") # Affichage du message d'erreur si le fichier n'est pas trouvé, informant l'utilisateur de la nature du problème (fichier manquant) et de l'emplacement spécifié.
