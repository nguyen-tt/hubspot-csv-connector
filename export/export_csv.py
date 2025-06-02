import csv
import logging
from hubspot_connector.client import get_all_contacts, get_contacts_created_today

def export_contacts_to_csv(filename="contacts_export.csv"):
    contacts = get_all_contacts(limit=100)
    today_contacts = get_contacts_created_today(limit=100)

    if not contacts:
        logging.error("Aucun contact à exporter.")
        return

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["firstname", "lastname", "email", "created_date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Tous les contacts
        writer.writerow({"firstname": "TOUS LES CONTACTS"})
        writer.writeheader()
        for contact in contacts:
            props = contact.properties
            writer.writerow({
                "firstname": props.get("firstname", ""),
                "lastname": props.get("lastname", ""),
                "email": props.get("email", ""),
                "created_date": props.get("createdate", "")
            })

        writer.writerow({})

        # Contacts créés aujourd’hui
        writer.writerow({"firstname": "CONTACTS CRÉÉS AUJOURD’HUI"})
        writer.writeheader()
        for contact in today_contacts:
            props = contact.properties
            writer.writerow({
                "firstname": props.get("firstname", ""),
                "lastname": props.get("lastname", ""),
                "email": props.get("email", ""),
                "created_date": props.get("createdate", "")
            })

    print(f"Export CSV terminé : {filename}")