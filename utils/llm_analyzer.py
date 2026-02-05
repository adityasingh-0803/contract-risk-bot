import os

# Optional OpenAI support
try:
    from openai import OpenAI
    HAS_OPENAI = True
except:
    HAS_OPENAI = False


def analyze_clause(clause):
    """
    Returns plain-language explanation of clause.
    Uses OpenAI if API key exists.
    Otherwise falls back to simple rule-based explanation.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    # -----------------------------
    # 🟢 Fallback (NO API)
    # -----------------------------
    if not HAS_OPENAI or not api_key:
        return simple_explanation(clause)

    # -----------------------------
    # 🟢 GPT explanation (optional)
    # -----------------------------
    try:
        client = OpenAI(api_key=api_key)

        prompt = f"""
        Explain this contract clause in simple business English.
        Mention risks if any.
        Suggest safer alternative.

        Clause:
        {clause}
        """

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        return res.choices[0].message.content

    except:
        return simple_explanation(clause)


# -----------------------------
# 🟢 Local fallback logic
# -----------------------------
def simple_explanation(clause):

    text = clause.lower()

    if "penalty" in text or "indemnify" in text:
        return "⚠️ This clause may impose financial penalties or liabilities on your business."

    elif "terminate" in text:
        return "⚠️ This clause allows termination which may end the agreement early."

    elif "auto-renew" in text:
        return "⚠️ This clause automatically renews the contract unless cancelled."

    elif "non-compete" in text:
        return "⚠️ This clause restricts you from working with competitors."

    else:
        return "This clause appears standard with low legal risk."
