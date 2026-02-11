import os
import hashlib

def lire_et_stocker_buffer(chemin_fichier):

    if not os.path.exists(chemin_fichier):
        raise FileNotFoundError(f"Le fichier '{chemin_fichier}' n'existe pas.") 

    with open(chemin_fichier, 'rb') as fichier: 
        
        buffer = fichier.read()

    return buffer

if __name__ == "__main__": 

    chemin_vers_fichier = r"C:\Users\DIMI\Desktop\esgi\cours\python mme Oulmi\CC T2 Python - Exo3\Exo3_ccT2\Copie_2.txt" 

    try:
       
        contenu_buffer = lire_et_stocker_buffer(chemin_vers_fichier)
        
        print(f"Empreinte SHA-256 : {hashlib.sha256(contenu_buffer).hexdigest()}")
        print(f"--- Lecture réussie ---")
        print(f"Taille du buffer : {len(contenu_buffer)} octets") 

    except FileNotFoundError as e: 
        print(f"Erreur : {e}") 
    except PermissionError: 
        print("Erreur : Vous n'avez pas les droits pour lire ce fichier.") 
