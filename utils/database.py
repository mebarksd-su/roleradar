import sqlite3
import pandas as pd
import os
from config.constants import APPLICATION_COLUMNS


# =========================
# DATABASE CONFIG
# =========================

DATABASE_FILE = "data/roleradar.db"


# =========================
# DATABASE CONNECTION
# =========================

def get_connection():
    os.makedirs(
        os.path.dirname(DATABASE_FILE),
        exist_ok=True
    )
    connection = sqlite3.connect(
        DATABASE_FILE,
        check_same_thread=False
    )
    return connection


# =========================
# DATABASE INITIALIZATION
# =========================

def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_added TEXT,
            company TEXT,
            role TEXT,
            location TEXT,
            work_arrangement TEXT,
            status TEXT,
            job_link TEXT,
            notes TEXT
        )
        """
    )

    connection.commit()
    connection.close()


# =========================
# FETCH APPLICATIONS
# =========================

def fetch_applications():

    connection = get_connection()

    query = "SELECT * FROM applications"

    df = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    if "id" in df.columns:
        df = df.rename(
            columns={
                "id": "Application ID",
                "date_added": "Date Added",
                "company": "Company",
                "role": "Role",
                "location": "Location",
                "work_arrangement": "Work Arrangement",
                "status": "Status",
                "job_link": "Job Link",
                "notes": "Notes"
            }
        )

    if len(df.columns) == 0:
        df = pd.DataFrame(columns=APPLICATION_COLUMNS)

    return df


# =========================
# INSERT APPLICATION
# =========================

def insert_application(application):

    initialize_database()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO applications (
            date_added,
            company,
            role,
            location,
            work_arrangement,
            status,
            job_link,
            notes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            application.get("Date Added", ""),
            application.get("Company", ""),
            application.get("Role", ""),
            application.get("Location", ""),
            application.get("Work Arrangement", ""),
            application.get("Status", ""),
            application.get("Job Link", ""),
            application.get("Notes", "")
        )
    )

    connection.commit()
    connection.close()


# =========================
# REPLACE APPLICATIONS FROM DATAFRAME
# Useful during migration because current app still works with DataFrames.
# =========================

def replace_applications_from_dataframe(df):

    initialize_database()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM applications")

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO applications (
                date_added,
                company,
                role,
                location,
                work_arrangement,
                status,
                job_link,
                notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                row.get("Date Added", ""),
                row.get("Company", ""),
                row.get("Role", ""),
                row.get("Location", ""),
                row.get("Work Arrangement", ""),
                row.get("Status", ""),
                row.get("Job Link", ""),
                row.get("Notes", "")
            )
        )

    connection.commit()
    connection.close()


# =========================
# UPDATE APPLICATION
# Updates one row by database id.
# Future UI migration can preserve ids for cleaner updates.
# =========================

def update_application(application_id, updated_application):

    initialize_database()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE applications
        SET
            date_added = ?,
            company = ?,
            role = ?,
            location = ?,
            work_arrangement = ?,
            status = ?,
            job_link = ?,
            notes = ?
        WHERE id = ?
        """,
        (
            updated_application.get("Date Added", ""),
            updated_application.get("Company", ""),
            updated_application.get("Role", ""),
            updated_application.get("Location", ""),
            updated_application.get("Work Arrangement", ""),
            updated_application.get("Status", ""),
            updated_application.get("Job Link", ""),
            updated_application.get("Notes", ""),
            application_id
        )
    )

    connection.commit()
    connection.close()


# =========================
# DELETE APPLICATION
# =========================

def delete_application(application_id):

    initialize_database()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM applications WHERE id = ?",
        (application_id,)
    )

    connection.commit()
    connection.close()
