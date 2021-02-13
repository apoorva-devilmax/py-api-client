#import core modules
import requests
import json
#import custom modules
from ..api_interface import APIInterface

class APIClient(APIInterface):
    """Sophisticated API Client"""
    def __init__(self, **kwargs):
        """Constructor"""
        self._base_url = kwargs['base_url'] if 'base_url' in kwargs else None
        self._endpoint = kwargs['endpoint'] if 'endpoint' in kwargs else None
        self._header = kwargs['header'] if 'header' in kwargs else None
        self._is_valid_request = False
        self._payload = kwargs['payload'] if 'payload' in kwargs else None
        self._method = kwargs['method'] if 'method' in kwargs else 'GET'
        self._request_type = kwargs['request_type'] if 'request_type' in kwargs else None
        self._api_response = {
            'status': 'failure',
            'error': '',
            'response': None,
        }

    @property
    def base_url(self) -> str:
        """Base URL"""
        return self._base_url

    @property
    def endpoint(self) -> str:
        """API Endpoint"""
        return self._endpoint

    @property
    def header(self) -> dict:
        """Request Headers"""
        return self._header

    @property
    def method(self) -> str:
        """Request Method"""
        return self._method

    @property
    def payload(self) -> dict:
        """Request Payload"""
        return json.dumps(self._payload) if self._request_type == 'json' else self._payload

    @property
    def is_valid_request(self) -> bool:
        """Is Valid Request"""
        return self._is_valid_request

    def prepare_request(self, param: dict) -> None:
        """Prepare Request"""
        self._payload = param

    def validate_request(self) -> None:
        """Validate Request"""
        self._is_valid_request = True

    def send_request(self) -> dict:
        """Send Request"""
        if self._is_valid_request:
            try: 
                client_resp = requests.request(self.method, self.base_url + self.endpoint, 
                data = self.payload,
                headers = self.header,
                )
                self._api_response['status'] = 'success'
                self._api_response['response'] = client_resp
            except requests.ConnectTimeout as e:
                self._api_response['error'] = 'Connection_Timeout'
                self._api_response['error_msg'] = str(e)
            except requests.TooManyRedirects as e:
                self._api_response['error'] = 'Too_Many_Redirects'
                self._api_response['error_msg'] = str(e)
            except requests.HTTPError as e:
                self._api_response['error'] = 'HTTP_Error'
                self._api_response['error_msg'] = str(e)
            except ConnectionError as e:
                self._api_response['error'] = 'Connection_Error'
                self._api_response['error_msg'] = str(e)
            except Exception as e:
                self._api_response['error'] = 'Unknown_Error'
                self._api_response['error_msg'] = str(e)
            #try/except ends
        else:
            self._api_response['error'] = 'Invalid_Request'
        #end if/else
        return self._api_response

    def make_log(self, param: dict) -> None:
        """Make Log"""
        pass