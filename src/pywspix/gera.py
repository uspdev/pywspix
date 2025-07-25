import requests
from urllib.parse import urljoin
from pywspix.headers import Headers
from pywspix.schemas import GerarPix


from urllib.parse import urljoin
import requests


class WSPixGera:
    """
    Cliente responsável por gerar cobranças Pix via WebService da instituição.

    Essa classe prepara e envia uma requisição para geração de um Pix,
    validando o payload de entrada e armazenando o `idfpix` da cobrança criada.
    """

    def __init__(self, headers: Headers, url: str):
        """
        Inicializa o cliente com cabeçalhos e URL base da API Pix.

        Args:
            headers (Headers): Objeto que gera os cabeçalhos HTTP.
            url (str): URL base da API Pix.
        """
        self.__payload = {}
        self.__headers = headers
        self.__url = url
        self.__idfpix = None
        self.__gerar_uri = "/wspix/api/pix/gerar"

    def __validate_payload(self, **kwargs):
        """
        Valida o payload usando o schema GerarPix.

        Args:
            **kwargs: Campos do payload a serem validados.

        Returns:
            GerarPix: Instância validada do modelo de payload.
        """
        validated = GerarPix(**kwargs)
        return validated

    def __get_headers(self) -> dict:
        """Gera e retorna os cabeçalhos HTTP."""
        return self.__headers.generate()

    def __get_url(self) -> str:
        """Gera a URL completa para a requisição de geração do Pix."""
        url = urljoin(self.__url, self.__gerar_uri)
        return url

    def __set_idfpix(self, pix_data: dict):
        """
        Extrai e armazena o ID da cobrança Pix (idfpix) da resposta.

        Args:
            pix_data (dict): Dicionário de resposta contendo o campo `idfpix`.
        """
        idfpix = pix_data.get("idfpix")
        self.__idfpix = idfpix

    def __get_idfpix(self) -> str | None:
        """Retorna o ID da cobrança Pix gerada, se houver."""
        return self.__idfpix

    def __str__(self) -> str:
        """Retorna o idfpix como representação textual do objeto."""
        return str(self.__get_idfpix())

    def set_payload(self, **kwargs):
        """
        Define o payload para a requisição de geração do Pix.

        Args:
            **kwargs: Dados a serem enviados no corpo da requisição.

        Raises:
            ValidationError: Caso o payload não atenda ao schema `GerarPix`.
        """
        self.__validate_payload(**kwargs)
        self.__payload = kwargs

    def get_payload(self) -> dict:
        """Retorna o payload atual configurado para envio."""
        return self.__payload

    def request_gerar_pix(self):
        """
        Realiza a requisição POST para a API de geração de cobrança Pix.

        Returns:
            Response: Objeto de resposta da requisição HTTP.
        """
        payload = self.get_payload()
        headers = self.__get_headers()
        url = self.__get_url()
        resp = requests.post(headers=headers, url=url, json=payload)
        return resp

    def gerar_pix(self):
        """
        Envia a requisição para gerar um Pix e armazena o idfpix da resposta.

        Returns:
            Response | Exception: Resposta da API ou erro capturado.
        """
        try:
            resp = self.request_gerar_pix()
            self.__set_idfpix(resp.json())
            return resp
        except Exception as error:
            return error
