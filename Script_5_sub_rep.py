import os # Importation du module os pour interagir avec le système d'exploitation, notamment pour parcourir les répertoires et manipuler les chemins de fichiers.

def lister_contenu_repertoire(chemin): # Définition de la fonction qui affiche le contenu d'un répertoire et de ses sous-répertoires de manière récursive. La fonction prend en entrée le chemin du répertoire à explorer et affiche tous les fichiers et sous-répertoires présents dans ce répertoire, en parcourant également les sous-répertoires de manière récursive pour afficher leur contenu.#
    
   # Affiche le contenu d'un répertoire et de ses sous-répertoires de manière récursive.

   # Args:
       # chemin (str): Chemin du répertoire à explorer.
    
  
    if not os.path.exists(chemin):   # Vérifie si le chemin existe

        print(f"Le chemin '{chemin}' n'existe pas.") # Si le chemin spécifié n'existe pas, un message d'erreur est affiché pour informer l'utilisateur du problème, et la fonction retourne sans effectuer de traitement supplémentaire, ce qui permet de gérer cette situation de manière appropriée (par exemple, en affichant un message d'erreur ou en terminant le programme).#
        
        return # Retourne pour indiquer que le chemin n'existe pas, permettant ainsi à l'appelant de gérer cette situation de manière appropriée (par exemple, en affichant un message d'erreur ou en terminant le programme).#

    if not os.path.isdir(chemin):  # Vérifie si le chemin est un répertoire 

        print(f"'{chemin}' n'est pas un répertoire.") # Si le chemin spécifié n'est pas un répertoire, un message d'erreur est affiché pour informer l'utilisateur du problème, et la fonction retourne sans effectuer de traitement supplémentaire, ce qui permet de gérer cette situation de manière appropriée (par exemple, en affichant un message d'erreur ou en terminant le programme).#

        return # Retourne pour indiquer que le chemin n'est pas un répertoire, permettant ainsi à l'appelant de gérer cette situation de manière appropriée (par exemple, en affichant un message d'erreur ou en terminant le programme).#


    for element in os.listdir(chemin):     # Parcourt chaque élément dans le répertoire
     
        chemin_complet = os.path.join(chemin, element)    # Construit le chemin complet de l'élément

        print(chemin_complet) # Affiche l'élément (fichier ou répertoire)

 
        if os.path.isdir(chemin_complet): # Si l'élément est un répertoire, appelle récursivement la fonction
           
            lister_contenu_repertoire(chemin_complet) # Appel récursif pour explorer le contenu du sous-répertoire, ce qui permet d'afficher de manière complète et hiérarchique tous les fichiers et répertoires présents dans le répertoire spécifié, y compris ceux situés dans les sous-répertoires.#

# Exemple d'utilisation
if __name__ == "__main__": # Bloc principal du script qui s'exécute lorsque le script est exécuté directement (et non importé comme module). Ce bloc permet à l'utilisateur d'entrer le chemin du répertoire à explorer, puis appelle la fonction pour lister le contenu de ce répertoire et de ses sous-répertoires.#
   
    repertoire = input("Entrez le chemin du répertoire à explorer : ") # Demande à l'utilisateur d'entrer le chemin du répertoire à explorer, ce qui permet de spécifier le répertoire dont le contenu doit être affiché, et ensuite appelle la fonction pour lister le contenu de ce répertoire et de ses sous-répertoires.#
   
    lister_contenu_repertoire(repertoire) # Appel de la fonction pour lister le contenu du répertoire spécifié par l'utilisateur, ce qui permet d'afficher de manière complète et hiérarchique tous les fichiers et répertoires présents dans le répertoire spécifié, y compris ceux situés dans les sous-répertoires.#