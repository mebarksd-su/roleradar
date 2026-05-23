

# =========================
# INDUSTRY TAGGING
# Future analytics and radar clustering
# =========================

COMPANY_INDUSTRIES = {
    "Google": "Technology",
    "Microsoft": "Technology",
    "Apple": "Technology",
    "Spotify": "Media",
    "Meta": "Technology",
    "Amazon": "Technology",
    "Netflix": "Media",
    "JP Morgan": "Finance",
    "Goldman Sachs": "Finance",
    "Deloitte": "Consulting",
    "PwC": "Consulting",
    "KPMG": "Consulting",
    "EY": "Consulting",
    "NBC": "Media",
    "Disney": "Entertainment",
    "Lockheed Martin": "Defense",
    "Raytheon": "Defense",
    "Boeing": "Aerospace",
    "SRC": "Defense"
}


# =========================
# GET INDUSTRY TAG
# =========================
def get_industry(company_name):

    if company_name is None:
        return "Unknown"

    cleaned_company = str(company_name).strip()

    if cleaned_company == "":
        return "Unknown"

    return COMPANY_INDUSTRIES.get(
        cleaned_company,
        "Other"
    )