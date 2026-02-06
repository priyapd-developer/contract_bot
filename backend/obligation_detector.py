def detect_obligation_type(text):
    text = text.lower()
    if "shall not" in text or "prohibited" in text:
        return "Prohibition"
    if "shall" in text or "must" in text:
        return "Obligation"
    if "may" in text:
        return "Right"
    return "Neutral"
