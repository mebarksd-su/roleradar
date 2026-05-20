import os
import pandas as pd
from utils.database import (
    initialize_database,
    fetch_applications,
    replace_applications_from_dataframe
)


DATA_FILE = "data/applications.csv"
APPLICATION_COLUMNS = [
    "Date Added",
    "Company",
    "Role",
    "Location",
    "Work Arrangement",
    "Status",
    "Job Link",
    "Notes"
]

def normalize_location(location):

    if pd.isna(location) or str(location).strip() == "":
        return "Not Specified"

    location = str(location).strip().lower()

    location_map = {
        "ny": "NYC",
        "nyc": "NYC",
        "new york": "NYC",
        "new york city": "NYC",
        "new york, ny": "NYC",
        "ca": "CA",
        "california": "CA",
        "fl": "FL",
        "florida": "FL",
        "ma": "MA",
        "massachusetts": "MA"
    }

    return location_map.get(location, location.title())

def normalize_status(status):

    if pd.isna(status) or str(status).strip() == "":
        return "Applied"

    status = str(status).strip().lower()

    status_map = {
        "interested": "Applied",
        "applied": "Applied",
        "interview": "Interviewing",
        "interviewing": "Interviewing",
        "rejected": "Rejected",
        "rejection": "Rejected",
        "offer": "Offer",
        "offered": "Offer"
    }

    return status_map.get(status, "Applied")

def normalize_work_arrangement(work_arrangement):

    if pd.isna(work_arrangement) or str(work_arrangement).strip() == "":
        return "Not Specified"

    work_arrangement = str(work_arrangement).strip().lower()

    work_map = {
        "remote": "Remote",
        "hybrid": "Hybrid",
        "on-site": "On-site",
        "onsite": "On-site",
        "on site": "On-site",
        "in person": "On-site",
        "in-person": "On-site"
    }

    return work_map.get(work_arrangement, "Not Specified")

def load_applications():

    initialize_database()

    df = fetch_applications()

    if df.empty:
        return pd.DataFrame(columns=APPLICATION_COLUMNS)

    if "Work Arrangement" not in df.columns:
        df["Work Arrangement"] = "Not Specified"

    if "Notes" not in df.columns:
        df["Notes"] = ""

    df["Notes"] = df["Notes"].fillna("").astype(str)
    df["Location"] = df["Location"].apply(normalize_location)
    df["Status"] = df["Status"].apply(normalize_status)
    df["Work Arrangement"] = df["Work Arrangement"].apply(normalize_work_arrangement)

    return df

def save_applications(df):

    initialize_database()

    replace_applications_from_dataframe(df)

    