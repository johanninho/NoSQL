def detect_anomalies(collection):
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

    results = collection.aggregate(pipeline)
    for result in results:
        print(f"⚠️ IP suspecte : {result['_id']['ip']} avec {result['count']} échecs à {result['_id']['minute']}")
