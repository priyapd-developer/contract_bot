# Offline mock suggestions
mock_suggestions = {
    "terminate": "Consider allowing termination only after 30 days notice to protect both parties.",
    "penalty": "Reduce penalty amounts or add grace period before penalty is applied.",
    "auto-renew": "Add an option to cancel contract 30 days before renewal.",
    "intellectual property": "Clarify that IP created by contractor remains theirs unless explicitly assigned.",
    "non-compete": "Limit non-compete to 6 months and only within the same city or sector.",
    "arbitration": "Specify neutral arbitration location and shared costs.",
    "indemnity": "Limit indemnity liability to actual damages and cap amount."
}

def get_suggestion(clause_text):
    text = clause_text.lower()
    for keyword, suggestion in mock_suggestions.items():
        if keyword in text:
            return suggestion
    return "This clause is acceptable, no changes suggested."
