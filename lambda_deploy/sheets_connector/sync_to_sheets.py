import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from hubspot_connector.client import (
    get_all_contacts,
    get_contacts_created_today,
)

def sync_contacts_to_google_sheets(sheet_name="HubSpot Contacts"):

    scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scopes)
    client = gspread.authorize(creds)
    try:
        sheet = client.open(sheet_name).sheet1
    except gspread.SpreadsheetNotFound:
        logging.error("Google Sheet introuvable.")
        return

    sheet.clear()

    header = ["firstname", "lastname", "email", "created_at"]

    sheet.append_row(["TOUS LES CONTACTS"])
    sheet.append_row(header)
    all_contacts = get_all_contacts(limit=100)
    for c in all_contacts:
        props = c.properties
        sheet.append_row([
            props.get("firstname", ""),
            props.get("lastname", ""),
            props.get("email", ""),
            props.get("createdate", "")
        ])
    print(f"{len(all_contacts)} contacts ajoutés à la section TOUS LES CONTACTS.")

    sheet.append_row([""])

    sheet.append_row(["CONTACTS CRÉÉS AUJOURD’HUI"])
    sheet.append_row(header)
    today_contacts = get_contacts_created_today(limit=100)
    for c in today_contacts:
        props = c.properties
        sheet.append_row([
            props.get("firstname", ""),
            props.get("lastname", ""),
            props.get("email", ""),
            props.get("createdate", "")
        ])
    print(f"{len(today_contacts)} contacts ajoutés à la section CONTACTS CRÉÉS AUJOURD’HUI.")
    print("Synchronisation vers Google Sheets terminée.")