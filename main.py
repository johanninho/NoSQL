from pymongo import MongoClient
from datetime import datetime
import random
import hashlib
from flask import Flask, jsonify, request

# Connexion au serveur MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Accès à la base de données et collections
db = client["ma_db"]
old_collection = db["utilisateurs"]
new_collection = db["logs"]

# Fonction pour générer un log
def generate_log():
    # Exemple d'IP (tu peux générer des IP aléatoires ou les définir)
    ip_addresses = ["192.168.1.12", "192.168.1.15", "192.168.1.20"]
    user_names = ["admin", "user1", "guest"]

    # Données aléatoires pour un log
    log = {
        "timestamp": datetime.utcnow().isoformat() + "Z",  # Utilisation de l'heure UTC
        "ip": random.choice(ip_addresses),  # IP choisie au hasard
        "user": random.choice(user_names),  # Nom d'utilisateur choisi au hasard
        "action": "login_attempt",  # Action de tentative de connexion
        "status": random.choice(["failed", "success"]),  # Statut du login, aléatoire
    }

    hash_input = log["timestamp"] + log["ip"] + log["user"] + log["action"] + log["status"]
    log_hash = hashlib.sha256(hash_input.encode()).hexdigest()
    log["log_hash"] = log_hash

    return log

def verify_logs():
    for log in new_collection.find():
        original_hash = log.get("log_hash")
        if not original_hash:
            print("Aucun hash trouvé pour le log :", log)
            continue

        # Reconstituer le hash
        fields = [log.get(k, "") for k in ["timestamp", "ip", "user", "action", "status"]]
        hash_input = "".join(fields)
        computed_hash = hashlib.sha256(hash_input.encode()).hexdigest()

        if computed_hash != original_hash:
            print("ALERTE : Log modifié ou corrompu !", log)
        else:
            print("Log intègre :", log["_id"])

pipeline = [
    { "$match": { "status": "failed" } },
    { "$group": {
        "_id": {
            "ip": "$ip",
            "minute": { "$substr": ["$timestamp", 0, 16] }
        },
        "count": { "$sum": 1 }
    }},
    { "$match": { "count": { "$gt": 5 } } }
]

results = new_collection.aggregate(pipeline)

for result in results:
    print(f"IP suspecte : {result['_id']['ip']} avec {result['count']} échecs à {result['_id']['minute']}")

# Copier tous les documents de l'ancienne collection "utilisateurs" vers la nouvelle collection "logs"
for document in old_collection.find():
    new_collection.insert_one(document)

# Insertion de nouveaux logs générés
for _ in range(5):  # Par exemple, insérer 5 nouveaux logs
    new_log = generate_log()
    new_collection.insert_one(new_log)

# Supprimer l'ancienne collection "utilisateurs"
db.drop_collection("utilisateurs")

# Vérification : Affichage des collections dans la base de données
print(db.list_collection_names())

# Vérification : Affichage des logs pour s'assurer que tout est bien inséré
for log in new_collection.find():
    print(log)
