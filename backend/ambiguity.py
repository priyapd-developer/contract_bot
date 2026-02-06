AMBIGUOUS_TERMS = ["reasonable", "as applicable", "from time to time"]

def detect_ambiguity(text):
    return [word for word in AMBIGUOUS_TERMS if word in text.lower()]
