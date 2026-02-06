import re

def split_clauses(text):
    clauses = re.split(r'\n(?=\d+[\.\)])', text)
    result = []
    for i, clause in enumerate(clauses):
        if clause.strip():
            result.append({
                "id": f"Clause {i + 1}",
                "text": clause.strip()
            })
    return result

