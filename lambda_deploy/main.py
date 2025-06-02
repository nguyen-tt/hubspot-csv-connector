import logging
from hubspot_connector.client import get_all_contacts
from sheets_connector.sync_to_sheets import sync_contacts_to_google_sheets
from utils.display import display_contacts

if __name__ == "__main__":
    contacts = get_all_contacts()

    if not contacts:
        logging.error("❌ Aucun contact trouvé après la date spécifiée.")
    else:
        print("\n👥 Contacts récupérés :")
        display_contacts(contacts)

        print("\n🔄 Export vers Google Sheets...")
        sync_contacts_to_google_sheets()