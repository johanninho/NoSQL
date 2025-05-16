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
├── main.py                # Script principal
├── db.py                  # Connexion à MongoDB
├── log_generator.py       # Génération des logs + hachage SHA256
├── integrity.py           # Vérification de l'intégrité des logs
├── analyzer.py            # Détection d’anomalies (logs suspects)
└── README.md              # Ce fichier
