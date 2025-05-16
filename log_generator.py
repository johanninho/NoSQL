from datetime import datetime
import random
import hashlib

def generate_log():
    ip_addresses = ["192.168.1.12", "192.168.1.15", "192.168.1.20"]
    user_names = ["admin", "user1", "guest"]

    log = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ip": random.choice(ip_addresses),
        "user": random.choice(user_names),
        "action": "login_attempt",
        "status": random.choice(["failed", "success"]),
    }

    hash_input = log["timestamp"] + log["ip"] + log["user"] + log["action"] + log["status"]
    log["log_hash"] = hashlib.sha256(hash_input.encode()).hexdigest()
    return log
