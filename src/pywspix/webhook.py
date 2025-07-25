import requests
from urllib.parse import urljoin
from pywspix.headers import Headers
from pywspix.schemas import WebhookConfig


class WSPixWebhook:
    """
    Cliente para configurar e remover webhooks Pix via API institucional.

    Esta classe permite definir e enviar configurações de webhook,
    além de excluir a configuração existente junto à API Pix.
    """

    def __init__(self, baseurl: str, headers: Headers):
        """
        Inicializa o cliente com a URL base da API e os cabeçalhos de autenticação.

        Args:
            baseurl (str): URL base da API Pix.
            headers (Headers): Objeto que gera os cabeçalhos HTTP.
        """
        self.__baseurl = baseurl
        self.__headers = headers
        self.__webhook_url = "/wspix/pix/webhookConfig"
        self.__config = None

    def get_baseurl(self) -> str:
        """Retorna a URL base configurada."""
        return self.__baseurl

    def get_webhook_url(self) -> str:
        """Retorna o path da rota de configuração do webhook."""
        return self.__webhook_url

    def get_url(self) -> str:
        """
        Retorna a URL completa da rota de configuração do webhook.

        Returns:
            str: URL final usada para POST e DELETE.
        """
        baseurl = self.get_baseurl()
        webhook_url = self.get_webhook_url()
        url = urljoin(baseurl, webhook_url)
        return url

    def get_headers(self) -> dict:
        """Gera e retorna os cabeçalhos HTTP necessários para a requisição."""
        headers = self.__headers.generate()
        return headers

    def validate_config(self, **config) -> dict:
        """
        Valida os parâmetros de configuração do webhook.

        Args:
            **config: Parâmetros esperados pela API Pix.

        Returns:
            dict: Dados validados no formato JSON.
        """
        validated_config = WebhookConfig(**config)
        return validated_config.model_dump(mode="json")

    def set_config(self, **config):
        """
        Define e armazena a configuração a ser enviada ao webhook.

        Args:
            **config: Dados de configuração a serem validados.
        """
        validated_config = self.validate_config(**config)
        self.__config = validated_config

    def get_config(self) -> dict:
        """
        Retorna a configuração armazenada internamente.

        Returns:
            dict: Configuração atual validada.

        Raises:
            ValueError: Se a configuração ainda não tiver sido definida.
        """
        if not self.__config:
            raise ValueError("Config has not been set yet.")
        return self.__config

    def config(self) -> dict | Exception:
        """
        Envia a configuração atual do webhook para a API Pix.

        Returns:
            dict | Exception: Resposta da API ou erro capturado.
        """
        try:
            url = self.get_url()
            config = self.get_config()
            headers = self.get_headers()
            resp = requests.post(url=url, json=config, headers=headers)
            return resp.json()
        except Exception as error:
            return error

    def delete(self) -> dict | Exception:
        """
        Remove a configuração atual do webhook da API Pix.

        Returns:
            dict | Exception: Resposta da API ou erro capturado.
        """
        try:
            url = self.get_url()
            headers = self.get_headers()
            resp = requests.delete(url=url, headers=headers)
            return resp.json()
        except Exception as error:
            return error
