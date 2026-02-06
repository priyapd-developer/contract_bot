import streamlit as st

from backend.loader import extract_text
from backend.clause_splitter import split_clauses
from backend.risk_engine import analyze_risk
from backend.ner import extract_entities
from backend.summary import contract_summary
from backend.suggestions import get_suggestion
from backend.classifier import classify_contract
from backend.obligation_detector import detect_obligation_type
from backend.ambiguity import detect_ambiguity
from backend.hindi_convert import normalize
from backend.exporter import export_pdf
from backend.audit import log_action

st.set_page_config(page_title="Contract Analysis Bot", layout="wide")
st.title("📄 Contract Analysis & Risk Assessment ")

uploaded_file = st.file_uploader(
    "Upload contract (PDF, DOCX, TXT)", 
    type=["pdf", "docx", "txt"]
)

if uploaded_file:
    # Audit log
    log_action(uploaded_file.name)

    # Hindi → English normalization (offline)
    raw_text = extract_text(uploaded_file)
    text = normalize(raw_text)

    # 📌 Contract classification
    st.subheader("📑 Contract Type")
    st.info(classify_contract(text))

    #  contract text
    st.subheader("📜 Contract Text")
    st.text_area("", text, height=250)

    clauses = split_clauses(text)

    st.subheader("🔍 Clause-wise Analysis")

    risk_map = {}
    score_map = {"High": 3, "Medium": 2, "Low": 1}
    total_score = 0

    for c in clauses:
        risk, reason = analyze_risk(c["text"])
        risk_map[c["id"]] = (risk, reason)
        total_score += score_map[risk]

        #  Risk display
        if risk == "High":
            st.error(f"{c['id']} – HIGH RISK 🚨")
        elif risk == "Medium":
            st.warning(f"{c['id']} – MEDIUM RISK ⚠️")
        else:
            st.success(f"{c['id']} – LOW RISK ✅")

        # Clause text
        st.write(c["text"])

        # Obligation / Right / Prohibition
        st.markdown("**→ Clause Nature:**")
        st.write(detect_obligation_type(c["text"]))

        # Plain English explanation
        st.markdown("**→ Simple Explanation:**")
        st.write(reason)

        # Ambiguity detection
        ambiguous_terms = detect_ambiguity(c["text"])
        if ambiguous_terms:
            st.markdown("**⚠️ Ambiguity Detected:**")
            st.write(", ".join(ambiguous_terms))

        #  mock renegotiation suggestion
        st.markdown("**→ Suggested Alternative Clause:**")
        st.write(get_suggestion(c["text"]))

        st.markdown("---")

    # Overall risk score
    final_score = round((total_score / (len(clauses) * 3)) * 100, 2)
    st.subheader("📊 Overall Contract Risk")

    if final_score > 60:
        st.error(f"🔴 High Risk Contract – {final_score}%")
    elif final_score > 30:
        st.warning(f"🟠 Medium Risk Contract – {final_score}%")
    else:
        st.success(f"🟢 Low Risk Contract – {final_score}%")

    #  Entity Recognition
    st.subheader("🏷 Extracted Parties, Dates, Amounts")
    st.write(extract_entities(text))

    #  Contract summary
    st.subheader("📝 Contract Summary (Key Risks)")
    summary_text = contract_summary(clauses, risk_map)
    st.text(summary_text)

    #  PDF Export
    if st.button("📄 Export Summary as PDF"):
        export_pdf(summary_text)
        st.success("PDF exported successfully!")
