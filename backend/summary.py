def contract_summary(clauses, risk_map):
    summary = []
    for c in clauses:
        risk, reason = risk_map[c["id"]]
        if risk in ["High", "Medium"]:
            summary.append(f"{c['id']}: {reason}")
    return "\n".join(summary)
