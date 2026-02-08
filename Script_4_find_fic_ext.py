import os # Importation du module os pour interagir avec le système d'exploitation, notamment pour parcourir les répertoires et manipuler les chemins de fichiers.

def rechercher_fichiers_par_extension(repertoire, extension): # Définition de la fonction qui recherche tous les fichiers avec une extension donnée dans un répertoire et ses sous-répertoires. La fonction prend en entrée le chemin du répertoire à explorer et l'extension des fichiers à rechercher, et retourne une liste des chemins complets des fichiers trouvés correspondant à cette extension.#
    
    # Recherche tous les fichiers avec une extension donnée dans un répertoire et ses sous-répertoires.

    # Args:
        # repertoire (str): Chemin du répertoire où effectuer la recherche.
       # extension (str): Extension des fichiers à rechercher (ex: '.txt', '.pdf').

    # Returns:
        # list: Liste des chemins complets des fichiers trouvés.
    
    # Liste pour stocker les chemins des fichiers trouvés

    fichiers_trouves = [] # Initialisation d'une liste vide pour stocker les chemins complets des fichiers trouvés qui correspondent à l'extension spécifiée. Cette liste sera remplie au fur et à mesure que les fichiers sont parcourus et vérifiés, permettant ainsi de collecter tous les fichiers pertinents pour une utilisation ultérieure (par exemple, pour les analyser, les renommer, etc.).#

    # Parcourir le répertoire et ses sous-répertoires

    for racine, dossiers, fichiers in os.walk(repertoire): # Utilisation de os.walk pour parcourir le répertoire spécifié et tous ses sous-répertoires. La fonction os.walk génère un tuple pour chaque répertoire rencontré, contenant le chemin du répertoire (racine), une liste des sous-répertoires (dossiers), et une liste des fichiers présents dans ce répertoire (fichiers). Cette approche permet d'explorer de manière récursive tous les fichiers dans la hiérarchie du répertoire, facilitant ainsi la recherche de fichiers avec l'extension spécifiée.#
        for fichier in fichiers: # Parcours de chaque fichier dans la liste des fichiers du répertoire actuel. Cette boucle permet d'examiner chaque fichier individuellement pour vérifier s'il correspond à l'extension recherchée, ce qui est essentiel pour filtrer les fichiers pertinents et les ajouter à la liste des fichiers trouvés.#
           
            if fichier.endswith(extension): # Vérifier si le fichier a l'extension recherchée
               
                chemin_complet = os.path.join(racine, fichier) # Construction du chemin complet du fichier en combinant le chemin du répertoire (racine) et le nom du fichier. Cette étape est nécessaire pour obtenir le chemin absolu du fichier, ce qui permet de l'identifier de manière unique dans le système de fichiers et de l'utiliser pour des opérations ultérieures (par exemple, pour l'ouvrir, le renommer, etc.).#
               
                fichiers_trouves.append(chemin_complet) # Ajouter le chemin à la liste des fichiers trouvés si l'extension correspond. Cette étape permet de collecter tous les fichiers qui répondent au critère de recherche (extension), ce qui peut être utile pour une analyse ultérieure, un traitement en masse, ou simplement pour afficher les résultats à l'utilisateur.#

    return fichiers_trouves # Retourne la liste des chemins complets des fichiers trouvés qui correspondent à l'extension spécifiée, permettant ainsi à l'appelant de gérer ces fichiers de manière appropriée (par exemple, en les affichant, en les analysant, en les renommant, etc.).#  

# Exemple d'utilisation
if __name__ == "__main__": # Bloc principal du script qui s'exécute lorsque le script est exécuté directement (et non importé comme module). Ce bloc permet à l'utilisateur d'entrer le chemin du répertoire à explorer et l'extension des fichiers à rechercher, puis appelle la fonction de recherche pour trouver les fichiers correspondants et affiche les résultats.#
  
    repertoire = input("Entrez le chemin du répertoire à explorer : ")   # Demander à l'utilisateur le répertoire et l'extension à rechercher, ce qui permet de spécifier les critères de recherche pour trouver les fichiers pertinents dans le système de fichiers.#
    extension = input("Entrez l'extension des fichiers à rechercher : ") # Demander à l'utilisateur l'extension des fichiers à rechercher, ce qui permet de filtrer les fichiers en fonction de leur type (par exemple, '.txt' pour les fichiers texte, '.pdf' pour les fichiers PDF, etc.) et d'obtenir des résultats plus ciblés lors de la recherche dans le répertoire spécifié.#

   
    resultats = rechercher_fichiers_par_extension(repertoire, extension)  # Appeler la fonction pour rechercher les fichiers avec l'extension spécifiée dans le répertoire donné, ce qui permet d'obtenir une liste des fichiers correspondants pour une utilisation ultérieure (par exemple, pour les afficher, les analyser, etc.).#


    if resultats:    # Afficher les résultats de la recherche, en vérifiant d'abord si des fichiers ont été trouvés. Si la liste des résultats n'est pas vide, cela signifie que des fichiers correspondant à l'extension spécifiée ont été trouvés, et ils seront affichés à l'utilisateur. Si la liste est vide, un message indiquant qu'aucun fichier n'a été trouvé avec l'extension spécifiée sera affiché pour informer l'utilisateur de la situation.#

        print(f"\nFichiers trouvés avec l'extension '{extension}' :") # Affichage d'un message pour indiquer que les fichiers trouvés avec l'extension spécifiée vont être affichés, ce qui permet de présenter les résultats de manière claire et organisée à l'utilisateur.#

        for fichier in resultats: # Parcours de chaque fichier trouvé dans la liste des résultats pour les afficher individuellement. Cette boucle permet de présenter chaque fichier correspondant à l'extension spécifiée de manière lisible, en affichant le chemin complet de chaque fichier pour que l'utilisateur puisse facilement les identifier et les localiser dans le système de fichiers.#

            print(fichier) # Affichage du chemin complet de chaque fichier trouvé, ce qui permet à l'utilisateur de voir exactement où se trouvent les fichiers correspondants à l'extension spécifiée dans le système de fichiers, facilitant ainsi leur identification et leur utilisation ultérieure (par exemple, pour les ouvrir, les analyser, etc.).#

    else: # Si aucun fichier n'a été trouvé avec l'extension spécifiée, un message d'information est affiché pour informer l'utilisateur de la situation, ce qui permet de clarifier que la recherche a été effectuée mais qu'aucun résultat correspondant n'a été trouvé, suggérant ainsi à l'utilisateur de vérifier les critères de recherche (répertoire et extension) ou d'essayer avec d'autres paramètres.#

        print(f"Aucun fichier trouvé avec l'extension '{extension}'.") # Affichage d'un message pour indiquer qu'aucun fichier n'a été trouvé avec l'extension spécifiée, informant ainsi l'utilisateur de la nature du résultat de la recherche et suggérant de vérifier les critères de recherche ou d'essayer avec d'autres paramètres pour obtenir des résultats différents.#
