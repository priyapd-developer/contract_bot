def classify_contract(text):
    text = text.lower()
    if "employee" in text or "salary" in text:
        return "Employment Contract"
    if "lease" in text or "rent" in text:
        return "Lease Agreement"
    if "partner" in text:
        return "Partnership Deed"
    if "vendor" in text:
        return "Vendor Contract"
    return "Service Agreement"
