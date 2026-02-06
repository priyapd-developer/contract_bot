STANDARD_TEMPLATES = {
    "termination": "Either party may terminate with 30 days notice.",
    "payment": "Payment shall be made within 15 days of invoice."
}

def match_template(clause):
    for k, v in STANDARD_TEMPLATES.items():
        if k in clause.lower():
            return v
    return None
