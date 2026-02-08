import re # Importation du module 're' pour les expressions régulières

def recuperer_mots_fichier(nom_fichier): # Définition de la fonction qui récupère tous les mots d'un fichier texte (.txt)
     
    try: # Ouverture du fichier en mode lecture ('r') avec encodage UTF-8 pour lire le contenu du fichier texte
        with open(nom_fichier, 'r', encoding='utf-8') as fichier: # Utilisation d'un bloc 'with' pour assurer la fermeture du fichier après la lecture, même en cas d'erreur
            contenu = fichier.read() # Lecture du contenu du fichier dans une variable 'contenu' pour traitement ultérieur#
      
        mots = re.findall(r'\b\w+\b', contenu)  # Utilisation d'une expression régulière pour extraire tous les mots du contenu du fichier. L'expression '\b\w+\b' correspond à des séquences de caractères alphanumériques entourées de limites de mots, ce qui permet d'extraire les mots individuels tout en ignorant la ponctuation et les espaces.# Affichage d'un message pour indiquer que les mots extraits du contenu du fichier vont être affichés
     
        return mots # Retourne la liste des mots extraits du fichier texte pour une utilisation ultérieure dans l'analyse des logs ou d'autres traitements.#
    
    except FileNotFoundError: # Gestion de l'exception FileNotFoundError qui peut être levée si le fichier texte n'existe pas à l'emplacement spécifié. Le message d'erreur est affiché pour informer l'utilisateur du problème.

        print(f"Erreur : Le fichier '{nom_fichier}' est introuvable.") # Affichage du message d'erreur si le fichier n'est pas trouvé, informant l'utilisateur de la nature du problème (fichier manquant) et de l'emplacement spécifié.

        return [] # Retourne une liste vide pour indiquer qu'aucun mot n'a été extrait en raison de l'absence du fichier, permettant ainsi à l'appelant de gérer cette situation de manière appropriée (par exemple, en affichant un message d'erreur ou en terminant le programme).#
    
    except UnicodeDecodeError: # Gestion de l'exception UnicodeDecodeError qui peut être levée si le fichier texte n'est pas encodé en UTF-8. Le message d'erreur est affiché pour informer l'utilisateur du problème et suggérer une alternative d'encodage.

        print("Erreur : Le fichier n'est pas encodé en UTF-8. Essayez avec 'latin-1'.") # Affichage du message d'erreur si le fichier n'est pas encodé en UTF-8, informant l'utilisateur de la nature du problème (encodage incorrect) et suggérant une alternative d'encodage (latin-1) pour tenter de lire le fichier correctement.#

        return [] # Retourne une liste vide pour indiquer qu'aucun mot n'a été extrait en raison d'un problème d'encodage, permettant ainsi à l'appelant de gérer cette situation de manière appropriée (par exemple, en affichant un message d'erreur ou en terminant le programme).
    
    except Exception as e: # Gestion de toute autre exception inattendue qui peut survenir lors de la lecture du fichier ou de l'extraction des mots. Le message d'erreur est affiché pour informer l'utilisateur de la nature du problème, et une liste vide est retournée pour indiquer qu'aucun mot n'a été extrait en raison de cette erreur.#

        print(f"Erreur inattendue : {e}") # Affichage du message d'erreur pour toute exception inattendue, informant l'utilisateur de la nature du problème qui a empêché l'extraction des mots du fichier texte.#

        return [] # Retourne une liste vide pour indiquer qu'aucun mot n'a été extrait en raison d'une erreur inattendue, permettant ainsi à l'appelant de gérer cette situation de manière appropriée (par exemple, en affichant un message d'erreur ou en terminant le programme).#

def analyser_logs(mots, mots_suspects): # Définition de la fonction qui analyse les mots extraits du fichier texte pour identifier les mots suspects en les comparant à une liste de mots suspects prédéfinie. La fonction retourne une liste des mots suspects trouvés dans les logs, en supprimant les doublons pour éviter les répétitions.#
  
    mots_suspects_en_minuscules = [mot.lower() for mot in mots_suspects] # Convertit tous les mots suspects en minuscules pour permettre une comparaison insensible à la casse lors de l'analyse des logs, assurant ainsi que les mots suspects seront détectés même s'ils apparaissent dans différentes capitalisations (par exemple, "Root", "root", "ROOT" seront tous reconnus comme le même mot suspect).#

    mots_trouves = [] # Initialisation d'une liste vide pour stocker les mots suspects trouvés dans les logs. Cette liste sera remplie au fur et à mesure que les mots extraits du fichier texte seront comparés à la liste des mots suspects, permettant ainsi de collecter tous les mots suspects détectés dans les logs pour une analyse ultérieure ou un rapport.#

    for mot in mots: # Parcours de chaque mot extrait du fichier texte pour le comparer à la liste des mots suspects. Cette boucle permet d'itérer sur tous les mots extraits et de vérifier s'ils correspondent à l'un des mots suspects, en tenant compte de la casse grâce à la conversion en minuscules effectuée précédemment.#

        if mot.lower() in mots_suspects_en_minuscules: # Vérifie si le mot actuel (converti en minuscules) est présent dans la liste des mots suspects également convertis en minuscules. Si une correspondance est trouvée, cela signifie que le mot extrait du fichier texte est considéré comme suspect et doit être ajouté à la liste des mots trouvés pour un suivi ultérieur ou une analyse plus approfondie.#

            mots_trouves.append(mot) # Si le mot extrait du fichier texte correspond à un mot suspect, il est ajouté à la liste des mots trouvés. Cette étape permet de collecter tous les mots suspects détectés dans les logs, ce qui peut être utile pour identifier des tendances, des menaces potentielles ou des activités suspectes dans les données analysées.#

    return list(set(mots_trouves))  # Supprime les doublons

if __name__ == "__main__": # Bloc principal du script qui s'exécute lorsque le script est exécuté directement (et non importé comme module). Ce bloc permet à l'utilisateur d'entrer le chemin du fichier texte à analyser, de récupérer les mots du fichier, d'analyser les logs pour trouver les mots suspects, et d'afficher les résultats de l'analyse.#

    fichier_logs = input("Entrez le chemin complet du fichier texte (.txt) : ") # Demande à l'utilisateur d'entrer le chemin complet du fichier texte à analyser, ce qui permet de spécifier l'emplacement du fichier contenant les logs ou les données à analyser pour détecter les mots suspects.#

    fichier_logs = fichier_logs.replace('\\', '/')  # Remplace les antislashs pour éviter les erreurs sous Windows 

    mots_suspects = [ # Liste prédéfinie de mots suspects à rechercher dans les logs. Ces mots sont souvent associés à des activités malveillantes, des tentatives d'intrusion, ou des vulnérabilités de sécurité. En analysant les logs pour détecter la présence de ces mots, il est possible d'identifier des comportements suspects ou des menaces potentielles dans les données analysées.#
        "root", "exploit", "failed", "login",
        "192.168", "attack", "malware",
        "credential", "safe", "vulnerabilities", "protect"
    ]

    mots = recuperer_mots_fichier(fichier_logs) # Appel de la fonction pour récupérer les mots du fichier texte spécifié par l'utilisateur. Les mots extraits seront ensuite analysés pour identifier les mots suspects présents dans les logs, permettant ainsi de détecter des activités potentiellement malveillantes ou des vulnérabilités de sécurité dans les données analysées.#

    if mots: # Vérifie si des mots ont été extraits du fichier texte. Si la liste de mots n'est pas vide, cela signifie que des mots ont été récupérés avec succès et peuvent être analysés pour détecter les mots suspects. Si la liste est vide, cela indique qu'aucun mot n'a été extrait, ce qui peut être dû à un problème de lecture du fichier ou à un fichier vide, et un message d'erreur approprié sera affiché pour informer l'utilisateur de la situation.#

        mots_trouves = analyser_logs(mots, mots_suspects) # Appel de la fonction pour analyser les mots extraits du fichier texte en les comparant à la liste des mots suspects. La fonction retourne une liste des mots suspects trouvés dans les logs, ce qui permet d'identifier des activités potentiellement malveillantes ou des vulnérabilités de sécurité dans les données analysées.#

        print(f"Mots suspects trouvés : {mots_trouves}") # Affichage des mots suspects trouvés dans les logs. Cette étape permet à l'utilisateur de voir les résultats de l'analyse et d'identifier les mots suspects qui ont été détectés dans les données analysées, ce qui peut être utile pour prendre des mesures de sécurité appropriées ou pour approfondir l'analyse des logs.#

    else: # Si aucun mot n'a été extrait du fichier texte, un message d'erreur est affiché pour informer l'utilisateur de la situation, suggérant de vérifier le fichier et son encodage pour s'assurer que les données peuvent être lues correctement et que les mots peuvent être extraits pour l'analyse.#

        print("Aucun mot extrait. Vérifiez le fichier et son encodage.") # Affichage du message d'erreur si aucun mot n'a été extrait du fichier texte, informant l'utilisateur de la nature du problème (absence de mots extraits) et suggérant de vérifier le fichier et son encodage pour s'assurer que les données peuvent être lues correctement et que les mots peuvent être extraits pour l'analyse.#