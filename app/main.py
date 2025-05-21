from NoSQL.app.db import get_db
from NoSQL.app.log_generator import generate_log
from NoSQL.app.integrity import verify_logs
from NoSQL.app.analyzer import detect_anomalies

db = get_db()
old_collection = db["utilisateurs"]
log_collection = db["logs"]

# Copier documents anciens
for doc in old_collection.find():
    log_collection.insert_one(doc)

# Insertion de nouveaux logs
for _ in range(5):
    log_collection.insert_one(generate_log())

# Supprimer ancienne collection
db.drop_collection("utilisateurs")

# Analyser les logs
detect_anomalies(log_collection)

# Vérifier l'intégrité
verify_logs(log_collection)

# Affichage des logs
for log in log_collection.find():
    print(log)
