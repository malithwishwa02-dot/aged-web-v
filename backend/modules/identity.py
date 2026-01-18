"""
identity.py - SQL injection and identity seeding logic for Chronos Engine (OP-VERITAS)
"""
import sqlite3
import os
from typing import Dict, Any

CHROME_PROFILE_PATH = os.environ.get("CHROME_PROFILE_PATH", "/app/chrome-profile")
AUTOFILL_DB = os.path.join(CHROME_PROFILE_PATH, "Web Data")

# Example identity schema for Chrome autofill_profiles
IDENTITY_SCHEMA = {
    "guid": "string",
    "full_name": "string",
    "company_name": "string",
    "street_address": "string",
    "city": "string",
    "state": "string",
    "zipcode": "string",
    "country_code": "string",
    "phone_number": "string",
    "email": "string"
}

def seed_identity(identity: Dict[str, Any], db_path: str = AUTOFILL_DB):
    """
    Injects identity data into Chrome's autofill_profiles table via SQL.
    """
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Chrome profile DB not found: {db_path}")
    conn = sqlite3.connect(db_path)
    try:
        c = conn.cursor()
        # Insert or replace identity
        c.execute("""
            INSERT OR REPLACE INTO autofill_profiles
            (guid, full_name, company_name, street_address, city, state, zipcode, country_code, phone_number, email)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [identity.get(k, "") for k in IDENTITY_SCHEMA.keys()])
        conn.commit()
    finally:
        conn.close()

def get_identities(db_path: str = AUTOFILL_DB):
    """
    Returns all seeded identities from Chrome's autofill_profiles table.
    """
    if not os.path.exists(db_path):
        return []
    conn = sqlite3.connect(db_path)
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM autofill_profiles")
        rows = c.fetchall()
        return rows
    finally:
        conn.close()
