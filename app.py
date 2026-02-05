import streamlit as st
import pandas as pd

from utils.extractor import extract_text
from utils.clause_splitter import split_clauses
from utils.risk_engine import score_clause
from utils.llm_analyzer import analyze_clause


# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Contract Risk Bot",
    layout="wide"
)

st.title("📄 Contract Analysis & Risk Assessment Bot")
st.markdown(
    "AI assistant to **analyze contracts, detect risks, and explain clauses in simple language**."
)


# ---------------------------
# File upload
# ---------------------------
file = st.file_uploader(
    "Upload contract",
    type=["pdf", "docx", "txt"]
)


# ---------------------------
# Main logic
# ---------------------------
if file:

    with st.spinner("🔍 Reading contract..."):
        text = extract_text(file)

    clauses = split_clauses(text)

    if not clauses:
        st.error("No clauses detected.")
        st.stop()

    results = []

    with st.spinner("🤖 Analyzing clauses..."):
        for clause in clauses:
            risk = score_clause(clause)
            explanation = analyze_clause(clause)

            results.append({
                "Clause": clause[:250] + "...",
                "Risk": risk,
                "Explanation": explanation
            })

    df = pd.DataFrame(results)


    # ---------------------------
    # Tabs layout
    # ---------------------------
    tab1, tab2 = st.tabs(["📊 Summary", "📋 Clause Analysis"])


    # ===========================
    # SUMMARY TAB
    # ===========================
    with tab1:
        st.subheader("Risk Overview")

        counts = df["Risk"].value_counts()

        col1, col2, col3 = st.columns(3)

        col1.metric("🔴 High", counts.get("High", 0))
        col2.metric("🟡 Medium", counts.get("Medium", 0))
        col3.metric("🟢 Low", counts.get("Low", 0))

        st.markdown("---")

        st.write("Total Clauses:", len(df))


    # ===========================
    # CLAUSE TABLE TAB
    # ===========================
    with tab2:

        def color_risk(val):
            if val == "High":
                return "background-color:#ffcccc"
            elif val == "Medium":
                return "background-color:#fff3cd"
            else:
                return "background-color:#d4edda"

        styled = df.style.applymap(color_risk, subset=["Risk"])

        st.dataframe(styled, use_container_width=True)


        # Download report
        csv = df.to_csv(index=False)
        st.download_button(
            "⬇ Download Report (CSV)",
            csv,
            "contract_analysis.csv",
            "text/csv"
        )


else:
    st.info("Upload a contract file to begin analysis.")
