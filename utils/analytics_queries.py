import pandas as pd

from utils.database import get_connection


# ============================================
# BASIC SQL METRICS
# ============================================

def get_total_applications():

    connection = get_connection()

    query = """
        SELECT COUNT(*) AS total
        FROM applications
    """

    result = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    return int(result.iloc[0]["total"])



def get_status_count(status):

    connection = get_connection()

    query = """
        SELECT COUNT(*) AS total
        FROM applications
        WHERE status = ?
    """

    result = pd.read_sql_query(
        query,
        connection,
        params=(status,)
    )

    connection.close()

    return int(result.iloc[0]["total"])



def get_interview_count():

    return get_status_count("Interviewing")



def get_offer_count():

    return get_status_count("Offer")



def get_rejected_count():

    return get_status_count("Rejected")


# ============================================
# SQL RATIOS
# ============================================

def get_interview_rate():

    total = get_total_applications()

    if total == 0:
        return 0

    interviews = get_interview_count()

    return round(
        (interviews / total) * 100,
        1
    )



def get_offer_rate():

    total = get_total_applications()

    if total == 0:
        return 0

    offers = get_offer_count()

    return round(
        (offers / total) * 100,
        1
    )


# ============================================
# APPLICATION VELOCITY
# ============================================

def get_applications_per_week():

    connection = get_connection()

    query = """
        SELECT
            strftime('%Y-%W', date_added) AS week,
            COUNT(*) AS applications
        FROM applications
        WHERE date_added IS NOT NULL
        AND date_added != ''
        GROUP BY week
        ORDER BY week DESC
    """

    result = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    return result


# ============================================
# TOP LOCATIONS
# ============================================

def get_top_locations(limit=5):

    connection = get_connection()

    query = """
        SELECT
            location,
            COUNT(*) AS applications
        FROM applications
        WHERE location IS NOT NULL
        AND location != ''
        GROUP BY location
        ORDER BY applications DESC
        LIMIT ?
    """

    result = pd.read_sql_query(
        query,
        connection,
        params=(limit,)
    )

    connection.close()

    return result


# ============================================
# TOP COMPANIES
# ============================================

def get_top_companies(limit=5):

    connection = get_connection()

    query = """
        SELECT
            company,
            COUNT(*) AS applications
        FROM applications
        WHERE company IS NOT NULL
        AND company != ''
        GROUP BY company
        ORDER BY applications DESC
        LIMIT ?
    """

    result = pd.read_sql_query(
        query,
        connection,
        params=(limit,)
    )

    connection.close()

    return result