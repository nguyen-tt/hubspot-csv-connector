from main import get_all_contacts, sync_contacts_to_google_sheets
from utils.display import display_contacts
import logging

def lambda_handler(event, context):
    logging.info("▶️ Lancement de la synchronisation via AWS Lambda...")

    contacts = get_all_contacts()
    if not contacts:
        logging.error("❌ Aucun contact trouvé.")
        return {
            "statusCode": 404,
            "body": "Aucun contact trouvé."
        }

    display_contacts(contacts)
    sync_contacts_to_google_sheets()

    logging.info("✅ Synchronisation terminée.")
    return {
        "statusCode": 200,
        "body": "Synchronisation terminée avec succès."
    }