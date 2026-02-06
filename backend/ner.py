import spacy

# Safe spaCy model loading for Streamlit Cloud
try:
    nlp = spacy.load("en_core_web_sm")
except OSError as e:
    raise RuntimeError(
        "spaCy model 'en_core_web_sm' is not installed. "
        "Add 'en-core-web-sm' to requirements.txt"
    ) from e


def extract_entities(text: str):
    if not text or not text.strip():
        return {
            "parties": [],
            "dates": [],
            "amounts": []
        }

    doc = nlp(text)

    parties = set()
    dates = set()
    amounts = set()

    for ent in doc.ents:
        if ent.label_ in ("ORG", "PERSON"):
            parties.add(ent.text)
        elif ent.label_ == "DATE":
            dates.add(ent.text)
        elif ent.label_ == "MONEY":
            amounts.add(ent.text)

    return {
        "parties": sorted(parties),
        "dates": sorted(dates),
        "amounts": sorted(amounts)
    }