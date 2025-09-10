import requests
from urllib.parse import urljoin
from pywspix.headers import Headers


class WSPixConsulta:
    """
    Consulta as informações para um dado pix (idfpix)

    Args:
        headers (Headers): Objeto Header com Usuário e Senha
        url (str): Url da api do serviço 
    """
    def __init__(self, headers: Headers, url: str):
        self.__headers = headers
        self.__url = url
        self.__uri = "/wspix/api/pix/"

    def get_headers(self):
        """
        Retorna o header para autenticação no serviço.
        """
        return self.__headers.generate()
    
    def get_consulta_url(self, idfpix: str):
        """
        Retorna a url da api para a consulta do pix.

        Args:
            idfpix (str): Identificação do pix.
        """
        uri = f"{self.__uri}{idfpix}"
        url = urljoin(self.__url, uri)
        return url
    
    def get_verificar_parameters(self):
        """
        Define o parâmetro varificar = true
        para verificar status de pagamento 
        para um determinado Pix
        """
        return {"verificar": "true"}
    
    def consultar(self, idfpix: str):
        """
        Consulta as informações para um dado Pix

        Args:
            idfpix (str): Identificação do Pix.
        """
        try:
            headers = self.get_headers()
            url = self.get_consulta_url(idfpix)
            resp = requests.get(url=url, headers=headers)
            return resp.json()
        except Exception as error:
            return error
    
    def verificar(self, idfpix: str):
        """
        Consulta o status de pagamento 
        para um determinado Pix

        Args:
            idfpix (str): Identificação do Pix.
        """
        try:
            url = self.get_consulta_url(idfpix)
            headers = self.get_headers()
            parameters = self.get_verifica_parameters()
            resp = requests.get(url=url, headers=headers, params=parameters)
            return resp
        except Exception as error:
            return error
