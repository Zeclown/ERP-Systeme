README
ERP-SYSTEM PROJET 1.0.0.0 2015/11/11

Les fichiers .py sont dans le dossier src.Nous avons deux "mains", le fichier serveur, qui doit rouler sur la machine serveur, et le fichier controleur, 
qui doit rouler sur la machine client.Le serveur utilise le dbaManager pour accéder à la base de donnée.Il est le seul qui a accès à dbManager directement.
La base de données est crée à partir du code si elle n'est pas présente dans le dossier direct de dbaManager.
Serveur communication est le messager du client pour parler au serveur. C'est le "bottleneck" des différents échanges qu'effectue le client avec le serveur.
Chaque frames du logiciel est hérite d'une frame parent (GFrame).
Le logiciel est actuellement configuré pour rouler les deux parties sur la même machine (serveur local) . 
On peut se log-in avec une vérification (usager de base: username:jmd , motdepasse:mdp). Ensuite en utilisant option
dans le menu en haut, on peut utiliser deux fenêtre. La fenêtre création d'usagers, 
qui n'est pas totalement fini (pas relié à la base de données encore) et la création de table(fonctionne en majeure partie).
Coté serveur, des fonctions de backup de la base de donnée à tout les x de temps, et l'envoit de email ont été programmée et sont prête à être utiliser
Nos plans pour le design logiciel et l'interface sont inclus dans le dossier "Documents"
La base de donnée système est presque complète(il nous manque le storage des différentes options d'affichage pour un champ de formulaire,il
faut s'entendre sur une méthode)

Pierre-Olivier Chartrand
Dragomir Dobrev
Alexandre Boulay
Antoine Paul-Vaillant