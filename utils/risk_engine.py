HIGH = [
    "penalty",
    "indemnify",
    "terminate anytime",
    "liable for all damages",
    "unlimited liability",
    "non-compete",
]

MEDIUM = [
    "auto-renew",
    "lock-in",
    "exclusive",
    "arbitration",
    "jurisdiction",
]


def score_clause(clause):
    c = clause.lower()

    for word in HIGH:
        if word in c:
            return "High"

    for word in MEDIUM:
        if word in c:
            return "Medium"

    return "Low"
