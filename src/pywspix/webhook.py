import requests
from urllib.parse import urljoin
from pydantic import BaseModel, HttpUrl
from pywspix.headers import Headers


class WebhookConfig(BaseModel):
    url: HttpUrl
    token: str


class Webhook():
    def __init__(self, baseurl: str, headers: Headers):
        self.__baseurl = baseurl
        self.__headers = headers 
        self.__webhook_url = "/pix/webhookConfig"
        self.__config = None

    def get_baseurl(self):
        return self.__baseurl

    def get_webhook_url(self):
        return self.__webhook_url

    def get_url(self):
        baseurl = self.get_baseurl()
        webhook_url = self.get_webhook_url()
        url = urljoin(baseurl, webhook_url)
        return url

    def get_headers(self):
        headers = self.__headers.generate()
        return headers

    def validate_config(self, **config):
        validated_config = WebhookConfig(**config)
        return validated_config.model_dump(mode="json")

    def set_config(self, **config):
        validated_config = self.validate_config(**config)
        self.__config = validated_config
    
    def get_config(self):
        if not self.__config:
            raise ValueError("Config has not been set yet.")
        return self.__config
    
    def config(self):
        url = self.get_url()
        config = self.get_config()
        headers = self.get_headers()
        resp = requests.post(url=url, json=config, headers=headers)
        return resp

    def delete(self):
        url = self.get_url()
        headers = self.get_headers()
        resp = requests.delete(url=url, headers=headers)