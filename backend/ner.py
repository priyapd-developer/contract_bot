import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    parties = []
    dates = []
    amounts = []
    
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PERSON"]:
            parties.append(ent.text)
        elif ent.label_ in ["DATE"]:
            dates.append(ent.text)
        elif ent.label_ in ["MONEY"]:
            amounts.append(ent.text)
    
    return {
        "parties": list(set(parties)),
        "dates": list(set(dates)),
        "amounts": list(set(amounts))
    }
