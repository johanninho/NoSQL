# NoSQL

# 📓 Système de Journalisation Sécurisée

Ce projet est une démonstration d’un système de journalisation sécurisé permettant :
- La génération de logs avec hachage pour garantir l'intégrité,
- La détection de comportements suspects (tentatives de connexions échouées),
- La vérification de l'intégrité des logs,
- Le stockage sécurisé dans une base MongoDB.

## 🔧 Technologies utilisées

- Python 3.x
- MongoDB (via MongoDB Compass ou serveur local)
- Pymongo


## 🗂️ Organisation du projet

```bash
journalisation-securisee/
├── app/
│   ├── main.py                 # Point d'entrée principal (exécution complète du projet)
│   ├── db.py                   # Connexion à MongoDB
│   ├── log_generator.py        # Génération des logs avec hachage SHA256
│   ├── integrity.py            # Vérification de l'intégrité des logs
│   ├── analyzer.py             # Analyse d'anomalies dans les logs
│   ├── requirements.txt        # Dépendances Python (Flask, pymongo, etc.)
│   └── Dockerfile              # Fichier Docker pour construire l’image de l’application
├── docker-compose.yml          # Démarrage automatique de MongoDB + app Python avec Docker
├── README.md                   # Fichier de présentation du projet
├── .gitignore     
