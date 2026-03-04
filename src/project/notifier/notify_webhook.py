import requests
from project.utils.functions import get_secret

def notify_webhook(data={}, webhook_url=get_secret("WEBHOOK_URL"), headers={'Content-Type': 'applications/json'}):
    
    return requests.post(url=webhook_url, params=data, headers=headers)

data = {
    'name': 'Perturbations sur la ligne A',
    'priority': 'URGENT',
    'message': 'Un retard de 15 minutes est à prévoir sur tous les trains de la ligne A en matinée.'
}