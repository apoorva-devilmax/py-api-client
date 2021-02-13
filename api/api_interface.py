import abc

class APIInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'prepare_request') and 
                callable(subclass.prepare_request) and 
                hasattr(subclass, 'validate_request') and 
                callable(subclass.validate_request) and 
                hasattr(subclass, 'is_valid_request') and 
                callable(subclass.is_valid_request) and 
                hasattr(subclass, 'send_request') and 
                callable(subclass.send_request) and 
                hasattr(subclass, 'make_log') and 
                callable(subclass.make_log) or 
                NotImplemented)

    @abc.abstractmethod
    def prepare_request(self, param: dict) -> None:
        """Prepare Request"""
        raise NotImplementedError

    @abc.abstractmethod
    def validate_request(self) -> None:
        """Validate Request"""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def is_valid_request(self) -> bool:
        """Is Valid Request"""
        raise NotImplementedError

    @abc.abstractmethod
    def send_request(self) -> dict:
        """Send Request"""
        raise NotImplementedError

    @abc.abstractmethod
    def make_log(self, param: dict) -> None:
        """Make Log"""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def base_url(self) -> str:
        """Base URL"""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def endpoint(self) -> str:
        """API Endpoint"""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def header(self) -> dict:
        """Request Headers"""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def payload(self) -> dict:
        """Request Payload"""
        raise NotImplementedError