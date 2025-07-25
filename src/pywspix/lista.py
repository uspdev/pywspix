import requests
from urllib.parse import urljoin
from datetime import datetime
from pywspix.headers import Headers
from pywspix.schemas import SearchParams


class Lista:
    """
    Cliente para listar cobranças Pix concluídas via WebService institucional.

    Essa classe constrói URLs, valida parâmetros de busca, formata datas
    e realiza requisições HTTP para obter os registros Pix concluídos.
    """

    def __init__(self, baseurl: str, headers: Headers):
        """
        Inicializa o cliente com a URL base da API e cabeçalhos de autenticação.

        Args:
            baseurl (str): URL base da API Pix.
            headers (Headers): Objeto responsável por gerar os cabeçalhos HTTP.
        """
        self.__search_params = None
        self.__baseurl = baseurl
        self.__listar_url = "/wspix/pix/listarConcluidos"
        self.__headers = headers

    def get_listar_url(self) -> str:
        """Retorna o path da rota para listar cobranças concluídas."""
        return self.__listar_url

    def get_base_url(self) -> str:
        """Retorna a URL base da API Pix."""
        return self.__baseurl

    def get_url(self) -> str:
        """
        Retorna a URL completa para a requisição de listagem.

        Returns:
            str: URL completa da rota de listagem.
        """
        baseurl = self.get_base_url()
        listar_url = self.get_listar_url()
        return urljoin(baseurl, listar_url)

    def validate_params(self, **params) -> dict:
        """
        Valida os parâmetros de busca usando o schema SearchParams.

        Args:
            **params: Parâmetros de entrada para busca de cobranças.

        Returns:
            dict: Parâmetros validados e convertidos.
        """
        search_params = SearchParams(**params)
        return search_params.model_dump()

    def get_headers(self) -> dict:
        """Gera e retorna os cabeçalhos HTTP."""
        return self.__headers.generate()

    def format_date(self, date: datetime) -> str:
        """
        Formata objeto datetime para o formato aceito pela API Pix.

        Args:
            date (datetime): Data a ser formatada.

        Returns:
            str: Data formatada como 'dd/mm/yyyy HH:MM:SS'.
        """
        return date.strftime("%d/%m/%Y %H:%M:%S")

    def get_search_params(self) -> dict:
        """
        Retorna os parâmetros de busca formatando as datas corretamente.

        Returns:
            dict: Parâmetros prontos para envio na query string.
        """
        search_params = self.__search_params
        search_params["dtaini"] = self.format_date(search_params["dtaini"])
        search_params["dtafim"] = self.format_date(search_params["dtafim"])
        return search_params

    def set_search_params(self, **params):
        """
        Valida e define os parâmetros de busca a serem utilizados na requisição.

        Args:
            **params: Argumentos para filtragem de cobranças Pix.
        """
        validated_params = self.validate_params(**params)
        self.__search_params = validated_params

    def request_listar(self) -> dict:
        """
        Executa a requisição HTTP GET para listar as cobranças Pix.

        Returns:
            dict: Resposta JSON da API com os registros encontrados.
        """
        params = self.get_search_params()
        headers = self.get_headers()
        url = self.get_url()
        resp = requests.get(url=url, headers=headers, params=params)
        return resp.json()

    def listar(self):
        """
        Lista as cobranças Pix concluídas de acordo com os parâmetros definidos.

        Returns:
            dict | Exception: Dados retornados pela API ou erro capturado.
        """
        try:
            resp = self.request_listar()
            return resp
        except Exception as error:
            return error
