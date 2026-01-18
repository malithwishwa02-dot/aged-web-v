"""
app.py - Streamlit GUI for Chronos Identity Synthesis Engine (OP-VERITAS)
"""
import streamlit as st
from backend.modules.identity import seed_identity, get_identities
from backend.modules.chronos import ChronosTimeShifter
import os

st.set_page_config(page_title="Chronos Identity Synthesis Engine", layout="wide")
st.title("Chronos Identity Synthesis Engine")

st.sidebar.header("Identity Seeding")
with st.sidebar.form("identity_form"):
    guid = st.text_input("GUID", "test-guid-001")
    full_name = st.text_input("Full Name", "John Doe")
    company_name = st.text_input("Company Name", "ACME Corp")
    street_address = st.text_input("Street Address", "123 Main St")
    city = st.text_input("City", "Metropolis")
    state = st.text_input("State", "CA")
    zipcode = st.text_input("Zipcode", "90001")
    country_code = st.text_input("Country Code", "US")
    phone_number = st.text_input("Phone Number", "+1-555-1234")
    email = st.text_input("Email", "john.doe@example.com")
    submitted = st.form_submit_button("Seed Identity")
    if submitted:
        identity = {
            "guid": guid,
            "full_name": full_name,
            "company_name": company_name,
            "street_address": street_address,
            "city": city,
            "state": state,
            "zipcode": zipcode,
            "country_code": country_code,
            "phone_number": phone_number,
            "email": email
        }
        try:
            seed_identity(identity)
            st.success("Identity seeded into Chrome profile DB.")
        except Exception as e:
            st.error(f"Error: {e}")

st.header("Seeded Identities (Chrome Autofill)")
identities = get_identities()
if identities:
    st.dataframe(identities)
else:
    st.info("No identities found in Chrome profile DB.")

st.sidebar.header("Time Manipulation")
faketime_env = st.sidebar.text_input("FAKETIME (libfaketime)", os.environ.get("FAKETIME", "@2020-01-01 00:00:00"))
if st.sidebar.button("Start Time-Shifted Run"):
    chronos = ChronosTimeShifter(faketime_env)
    # Example: run main.py with faketime (non-blocking demo)
    import threading
    def run_main():
        chronos.run_with_faketime(["python", "main.py"])
    threading.Thread(target=run_main, daemon=True).start()
    st.sidebar.success(f"Started main.py with FAKETIME={faketime_env}")
