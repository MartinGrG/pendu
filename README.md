# Jeu du pendu
### Présentation
Ce projet permet de jouer au jeu du pendu. Le joueur a 6 vies afin de trouver le mot à deviner. Pour ce faire il propose 
une lettre: si elle fait partie du mot, bien joué il faut trouver les autres; si elle n'en fait pas partie le joueur perd une vie.
Le jeu s'arrête lorsque le joueur a trouvé toutes les lettres du mot caché ou lorsqu'il n'a plus de vie.  
Dans le cas où il ne lui reste plus qu'une vie, le joueur obtient un indice: une lettre qui n'est pas dans le mot.  
Un mot caché est représentépar les lettres déjà trouvées et avec des '_', exemple: abeille -> a_e___e. Ici la lettre a et e ont été trouvées.

### Utilisation:
Afin de jouer il suffit de télécharger le dossier, ourvrir "main.py" et run le programme.
Le joueur n'a plus qu'à suivre les instructions dans le terminal.  
Le joueur peut décider de fournir un fichier texte ave sa propre liste de mot, pour ce faire il lui suffit de le glisser dans
même dossier où est enregistré le main en l'appelant "mots.pendu.txt". Dans le cas où le joueur n'a pas de liste de mot, 
une liste pas défaut est fournit.

### Fonctionnalitées
Le jeu prend en compte le cas où l'utilisateur entre: du vide, un chiffre, plusieurs lettre, une lettre déjà proposée  
De plus les '-' et les " ' " sont affichés, le joueur n'a pas à les devener.
