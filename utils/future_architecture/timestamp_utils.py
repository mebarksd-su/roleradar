

from datetime import datetime, date


# =========================
# TIMESTAMP UTILITIES
# Future analytics and radar freshness support
# =========================

def get_today_string():

    return str(date.today())


# =========================
# PARSE DATE SAFELY
# =========================
def parse_date_safe(date_value):

    if date_value is None:
        return None

    try:
        return datetime.strptime(
            str(date_value),
            "%Y-%m-%d"
        ).date()

    except ValueError:
        return None


# =========================
# DAYS SINCE DATE
# =========================
def days_since(date_value):

    parsed_date = parse_date_safe(date_value)

    if parsed_date is None:
        return None

    return (
        date.today() - parsed_date
    ).days


# =========================
# APPLICATION FRESHNESS LABEL
# =========================
def get_freshness_label(date_value):

    days_old = days_since(date_value)

    if days_old is None:
        return "Unknown"

    if days_old <= 7:
        return "Fresh"

    if days_old <= 14:
        return "Follow Up Soon"

    return "Stale"