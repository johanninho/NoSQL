import hashlib

def verify_logs(collection):
    for log in collection.find():
        original_hash = log.get("log_hash")
        if not original_hash:
            print("Aucun hash trouvé pour le log :", log)
            continue

        fields = [log.get(k, "") for k in ["timestamp", "ip", "user", "action", "status"]]
        hash_input = "".join(fields)
        computed_hash = hashlib.sha256(hash_input.encode()).hexdigest()

        if computed_hash != original_hash:
            print("❌ ALERTE : Log modifié ou corrompu !", log)
        else:
            print("✅ Log intègre :", log["_id"])
