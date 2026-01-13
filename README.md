# Carnet d'Adresses
Application de gestion de contacts avec PyQt6 et SQLite.
En développement...
Carnet d'Adresses - Application PyQt6 + SQLite
Application de gestion de contacts avec interface graphique moderne utilisant PyQt6 et base de données SQLite.

Fonctionnalités
Gestion complète CRUD

Create : Ajouter de nouveaux contacts
Read : Afficher tous les contacts dans un tableau
Update : Modifier les informations d'un contact existant
Delete : Supprimer un contact (avec confirmation)

Base de données
Connexion SQLite locale
Initialisation automatique de la base de données
Stockage persistant des données
Table contacts avec les champs :

id (clé primaire auto-incrémentée)
nom (obligatoire)
prenom (obligatoire)
telephone (optionnel)
courriel (optionnel)

Interface utilisateur
Interface graphique moderne et intuitive
Affichage en tableau avec tri par nom/prénom
Boutons avec icônes pour toutes les opérations
Messages de confirmation et d'erreur
Validation des données obligatoires

Prérequis : 

Logiciels requis
Python 3.8 ou supérieur
pip (gestionnaire de paquets Python)

Dépendances Python
bashPyQt6

Exécution
Lancer l'application : py main.py

Première utilisation
Au démarrage, cliquez sur "Initialiser BD" pour créer la base de données
La table des contacts sera créée automatiquement
Vous pouvez maintenant ajouter vos premiers contacts!

📁 Structure du projet

carnet-adresses/
│
├── 📄 main.py                    
│
├── 📁 src/
│   ├── 📁 database/              
│   │   ├── __init__.py
│   │   └── manager.py           [DatabaseManager]
│   │
│   └── 📁 ui/                    
│       ├── __init__.py
│       ├── main_window.py       [MainWindow]
│       └── dialogs.py           [ContactDialog]
│
├── 📁 tests/                    
│   ├── __init__.py
│   └── test_database.py
│
├── 📁 docs/                     
│   ├── screenshots/
│   └── ARCHITECTURE.md
│
├── 📄 README.md                 
├── 📄 requirements.txt           
├── 📄 .gitignore                 
└── 📄 LICENSE                    

Utilisation
Ajouter un contact

Cliquez sur "Ajouter"
Remplissez le formulaire (nom et prénom obligatoires)
Cliquez sur "Enregistrer"

Modifier un contact

Sélectionnez un contact dans le tableau
Cliquez sur "Modifier"
Modifiez les informations
Cliquez sur "Enregistrer"

Supprimer un contact

Sélectionnez un contact dans le tableau
Cliquez sur "Supprimer"
Confirmez la suppression

Rafraîchir l'affichage

Cliquez sur "Rafraîchir" pour recharger les données

Configuration
Modifier le nom de la base de données
Dans le fichier main.py, ligne de la classe DatabaseManager :
pythondef __init__(self, db_name="carnet_adresses.db"):
Personnaliser l'interface
Les styles et couleurs peuvent être modifiés dans la méthode setup_ui() de la classe MainWindow.

Dépannage
Problème : "Module PyQt6 not found"
Solution : Installez PyQt6
bashpip install PyQt6
Problème : La base de données ne se crée pas
Solution : Vérifiez les permissions d'écriture dans le dossier de l'application
Problème : L'application ne démarre pas
Solution : Vérifiez votre version de Python
bashpython --version  # Doit être 3.8+

Technologies utilisées

PyQt6 : Framework d'interface graphique
SQLite3 : Base de données relationnelle légère
Python 3 : Langage de programmation

Fonctionnalités futures (idées)

 Recherche et filtrage des contacts
 Export/Import CSV
 Groupes de contacts
 Photos de profil
 Champs personnalisés
 Historique des modifications
 Sauvegarde automatique

Contribution
Les contributions sont les bienvenues! Pour contribuer :

Forkez le projet
Créez une branche (git checkout -b feature/amelioration)
Committez vos changements (git commit -m 'Ajout fonctionnalité')
Poussez vers la branche (git push origin feature/amelioration)
Ouvrez une Pull Request

Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

Note : Cette application a été développée à des fins éducatives et de démonstration des capacités de PyQt6 et SQLite.