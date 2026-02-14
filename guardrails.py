def is_out_of_domain(query):
    restricted_keywords = [
        "politics",
        "hacking",
        "crypto trading tips",
        "illegal",
        "adult"
    ]

    for word in restricted_keywords:
        if word in query.lower():
            return True

    return False

def contains_sensitive_data(query):
    sensitive_keywords = ["account number", "aadhaar", "pan number", "credit card number"]

    for word in sensitive_keywords:
        if word in query.lower():
            return True

    return False
