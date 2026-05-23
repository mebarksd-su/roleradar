

# =========================
# CITY NORMALIZATION
# Future radar map support
# =========================

CITY_ALIASES = {
    "nyc": "New York City",
    "new york": "New York City",
    "new york city": "New York City",
    "manhattan": "New York City",
    "brooklyn": "New York City",
    "queens": "New York City",
    "boston ma": "Boston",
    "boston": "Boston",
    "syracuse ny": "Syracuse",
    "syracuse": "Syracuse",
    "atlanta ga": "Atlanta",
    "atlanta": "Atlanta",
    "philadelphia pa": "Philadelphia",
    "philly": "Philadelphia",
    "philadelphia": "Philadelphia",
    "dallas tx": "Dallas",
    "dallas": "Dallas",
    "texas": "Texas",
    "ca": "California",
    "california": "California",
    "ma": "Massachusetts",
    "massachusetts": "Massachusetts",
    "mn": "Minnesota",
    "minnesota": "Minnesota",
    "va": "Virginia",
    "virginia": "Virginia"
}


# =========================
# NORMALIZE CITY NAME
# =========================
def normalize_city(location):

    if location is None:
        return "Not Specified"

    cleaned_location = str(location).strip()

    if cleaned_location == "":
        return "Not Specified"

    lookup_key = cleaned_location.lower()

    return CITY_ALIASES.get(
        lookup_key,
        cleaned_location
    )