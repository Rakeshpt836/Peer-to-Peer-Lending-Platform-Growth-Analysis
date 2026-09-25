import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.engine import URL


# ==========================================
# Database connection
# ==========================================

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "mummy@41",  # Replace with your actual MySQL password
    "database": "p2p_lending_analysis"
}


# ==========================================
# Raw dataset file
# ==========================================

CSV_FILE_NAME = r"data/Processed/P2P_Lending_Cleaned.csv"


# ==========================================
# MySQL table
# ==========================================

TABLE_NAME = " p2p_loans"


# ==========================================
# Create MySQL connection
# ==========================================

def get_engine():
    """Create and return a SQLAlchemy engine connected to MySQL."""

    connection_url = URL.create(
        drivername="mysql+mysqlconnector",
        username=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"]
    )

    engine = create_engine(connection_url)

    return engine


# ==========================================
# Load CSV into MySQL
# ==========================================

def load_csv_to_database():
    """
    Read the CSV file and insert its rows
    into the MySQL table.
    """

    engine = get_engine()

    # Read CSV
    df = pd.read_csv(CSV_FILE_NAME)

    print(f"CSV loaded successfully: {len(df)} rows")

    # Insert into MySQL
    df.to_sql(
        name=TABLE_NAME,
        con=engine,
        if_exists="append",
        index=False
    )

    print(
        f"Loaded {len(df)} rows into "
        f"'{TABLE_NAME}' successfully."
    )


# ==========================================
# Fetch data from MySQL
# ==========================================

def fetch_data_from_database():
    """
    Fetch the Green Bond data from MySQL
    into a Pandas DataFrame.
    """

    engine = get_engine()

    query = f"SELECT * FROM {TABLE_NAME}"

    df = pd.read_sql(query, con=engine)

    return df


# ==========================================
# Test connection
# ==========================================

if __name__ == "__main__":

    engine = get_engine()

    with engine.connect() as connection:
        print("MySQL connection successful!")

    # Keep this commented for the first test
    load_csv_to_database()