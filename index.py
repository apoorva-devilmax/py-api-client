#import core modules
#import custom modules
from api.rest.api_client import APIClient

#start programming
client = APIClient(
    base_url = 'http://localhost:3000',
    endpoint = '/health'
)
client.validate_request()
api_resp = client.send_request()
print(api_resp['response'])
#test