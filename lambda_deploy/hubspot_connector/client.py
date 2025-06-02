from datetime import datetime, timezone
import logging
import os
from dotenv import load_dotenv
from hubspot import HubSpot
from hubspot.crm.contacts import ApiException
from hubspot.crm.contacts import Filter, FilterGroup, PublicObjectSearchRequest

load_dotenv()
token = os.getenv("HUBSPOT_API_KEY")

client = HubSpot(access_token=token)

def get_all_contacts(limit=100):
    try:
        response = client.crm.contacts.basic_api.get_page(limit=limit, archived=False)
        return response.results
    except ApiException as e:
        logging.error(f"[HubSpot] Erreur récupération des contacts : {e}")
        return []


def get_contacts_created_today(limit=100):
    # Récupère la date actuelle à minuit UTC
    today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    iso_today = today.isoformat()

    filter_by_date = Filter(property_name="createdate", operator="GTE", value=iso_today)
    filter_group = FilterGroup(filters=[filter_by_date])
    search_request = PublicObjectSearchRequest(filter_groups=[filter_group], limit=limit)

    try:
        api_response = client.crm.contacts.search_api.do_search(search_request)
        return api_response.results
    except ApiException as e:
        logging.error(f"[HubSpot] Erreur récupération des contacts créés aujourd’hui : {e}")
        return []