import os # Importation du module os pour interagir avec le système d'exploitation

def renommer_fichier(ancien_nom: str, nouveau_nom: str) -> bool: # Définition de la fonction qui renomme un fichier sur le système de fichiers. La fonction prend en entrée le nom actuel du fichier (ancien_nom) et le nouveau nom souhaité (nouveau_nom), et retourne un booléen indiquant si le renommage a réussi ou non.#

    # Renomme un fichier sur le système de fichiers.

     # Args:
        # ancien_nom (str): Le chemin complet ou relatif du fichier à renommer.
        # nouveau_nom (str): Le nouveau nom (ou chemin) du fichier.

        #Returns:
        # bool: True si le renommage a réussi, False sinon.

    if not os.path.exists(ancien_nom):    # Vérifie si le fichier source existe

        print(f"Erreur : Le fichier '{ancien_nom}' n'existe pas.") # Si le fichier à renommer n'existe pas, un message d'erreur est affiché pour informer l'utilisateur du problème, et la fonction retourne False pour indiquer que le renommage a échoué en raison de l'absence du fichier source.#

        return False # Retourne False pour indiquer que le renommage a échoué en raison de l'absence du fichier source, permettant ainsi à l'appelant de gérer cette situation de manière appropriée (par exemple, en affichant un message d'erreur ou en terminant le programme).#

    if os.path.exists(nouveau_nom): 

        print(f"Erreur : Le nom '{nouveau_nom}' est déjà utilisé.") # Si le nouveau nom de fichier existe déjà, un message d'erreur est affiché pour informer l'utilisateur du problème, et la fonction retourne False pour indiquer que le renommage a échoué en raison d'un conflit de noms.#

        return False # Retourne False pour indiquer que le renommage a échoué en raison d'un conflit de noms, permettant ainsi à l'appelant de gérer cette situation de manière appropriée (par exemple, en affichant un message d'erreur ou en demandant à l'utilisateur de choisir un autre nom).#

    try: # Utilise un bloc try-except pour tenter de renommer le fichier et gérer les exceptions potentielles qui peuvent survenir lors du processus de renommage, telles que des problèmes de permissions, des chemins invalides, ou d'autres erreurs liées au système de fichiers.#
      
        os.rename(ancien_nom, nouveau_nom)   # Utilise la fonction os.rename pour renommer le fichier

        print(f"Fichier '{ancien_nom}' renommé en '{nouveau_nom}' avec succès !") # Si le renommage réussit, un message de succès est affiché pour informer l'utilisateur que le fichier a été renommé avec succès, indiquant à la fois le nom original et le nouveau nom du fichier.#

        return True # Retourne True pour indiquer que le renommage a réussi, permettant ainsi à l'appelant de poursuivre avec d'autres opérations ou de confirmer que le processus s'est déroulé correctement.#
    
    except Exception as e: # Gestion de toute exception qui peut survenir lors du processus de renommage, en affichant un message d'erreur détaillé pour informer l'utilisateur de la nature du problème (par exemple, permissions insuffisantes, chemin invalide, etc.) et en retournant False pour indiquer que le renommage a échoué en raison de cette erreur.#

   
        print(f"Erreur lors du renommage : {e}") # Gestion des erreurs (permissions, chemin invalide, etc.)

        return False # Retourne False pour indiquer que le renommage a échoué en raison d'une exception, permettant ainsi à l'appelant de gérer cette situation de manière appropriée (par exemple, en affichant un message d'erreur ou en terminant le programme).#

# Exemple d'utilisation

if __name__ == "__main__": # Bloc principal du script qui s'exécute lorsque le script est exécuté directement (et non importé comme module). Ce bloc permet à l'utilisateur de choisir un fichier à renommer et d'entrer le nouveau nom souhaité, puis appelle la fonction de renommage pour effectuer l'opération.#

    ancien = input("Choisissez le fichier à renommer : ") # Demande à l'utilisateur de choisir le fichier à renommer en entrant son nom ou son chemin, ce qui permet de spécifier le fichier source pour le processus de renommage.

    nouveau = input("Entrez la modification de nommage du fichier : ") # Demande à l'utilisateur d'entrer le nouveau nom souhaité pour le fichier, ce qui permet de spécifier le nom de destination pour le processus de renommage.

    renommer_fichier(ancien, nouveau) # Appel de la fonction de renommage avec les noms de fichiers fournis par l'utilisateur, ce qui permet d'exécuter le processus de renommage et d'afficher les résultats (succès ou échec) en fonction des conditions définies dans la fonction.#