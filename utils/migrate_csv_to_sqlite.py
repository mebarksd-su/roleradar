import pandas as pd

from utils.database import (
    initialize_database,
    replace_applications_from_dataframe
)

CSV_FILE = "data/applications.csv"


def migrate_csv_to_sqlite():

    df = pd.read_csv(CSV_FILE)

    replace_applications_from_dataframe(df)

    print("CSV successfully migrated to SQLite.")


if __name__ == "__main__":

    initialize_database()

    migrate_csv_to_sqlite()