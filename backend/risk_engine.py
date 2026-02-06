# Enhanced Risk Detection Logic
def analyze_risk(clause_text):
    text = clause_text.lower()
    
    if "terminate" in text and "without notice" in text:
        return "High", "The other party can terminate the contract without notice"

    if "penalty" in text or "liquidated damages" in text:
        return "High", "Financial penalty may apply if obligations not met"

    if "automatically renew" in text or "auto-renew" in text:
        return "Medium", "Contract auto-renews; may lock you in"

    if "intellectual property" in text and "company" in text:
        return "Medium", "IP may belong to the company"

    if "non-compete" in text:
        return "High", "Non-compete may restrict your future work"

    if "arbitration" in text or "jurisdiction" in text:
        return "Medium", "Arbitration/jurisdiction may favor other party"

    if "indemnity" in text:
        return "High", "Indemnity clauses may create liability"

    return "Low", "No major risk detected"
