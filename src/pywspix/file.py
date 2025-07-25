import requests
from pywspix.headers import Headers
from urllib.parse import urljoin


from urllib.parse import urljoin
import requests

class WSPixFile:
    """
    Cliente utilitário para obter arquivos (PDF ou QR Code) associados a uma cobrança Pix.

    Essa classe gera URLs para acesso a arquivos relacionados ao Pix
    e realiza requisições HTTP para obter seu conteúdo.
    """

    def __init__(self, baseurl: str, headers: Headers, idfpix: str):
        """
        Inicializa o cliente com a URL base da API, cabeçalhos e ID da cobrança Pix.

        Args:
            baseurl (str): URL base da API Pix.
            headers (Headers): Objeto que gera os cabeçalhos HTTP.
            idfpix (str): Identificador da cobrança Pix.
        """
        self.__baseurl = baseurl
        self.__headers = headers
        self.__idfpix = idfpix

    def get_baseurl(self) -> str:
        """Retorna a URL base da API Pix."""
        return self.__baseurl
    
    def get_headers(self) -> dict:
        """Gera e retorna os cabeçalhos HTTP."""
        return self.__headers.generate()
    
    def get_idfpix(self) -> str:
        """Retorna o identificador da cobrança Pix."""
        return self.__idfpix

    def generate_file_url(self, media_type: str) -> str:
        """
        Gera a URL para acesso a um recurso do tipo informado (ex: pdf, qrcode).

        Args:
            media_type (str): Tipo do arquivo a ser acessado ('pdf' ou 'qrcode').

        Returns:
            str: URL completa para o recurso.
        """
        baseurl = self.get_baseurl()
        idfpix = self.get_idfpix()
        uri = f"/pix/{idfpix}/{media_type}"
        url = urljoin(baseurl, uri)
        return url
    
    def get_pdf_url(self) -> str:
        """Retorna a URL do arquivo PDF da cobrança."""
        return self.generate_file_url(media_type="pdf")
    
    def get_qrcode_url(self) -> str:
        """Retorna a URL da imagem QR Code da cobrança."""
        return self.generate_file_url(media_type="qrcode")

    def get_media(self, url: str) -> bytes | Exception:
        """
        Realiza uma requisição HTTP para obter o conteúdo binário de um recurso.

        Args:
            url (str): URL do recurso a ser acessado.

        Returns:
            bytes | Exception: Conteúdo do recurso ou exceção capturada.
        """
        try:
            headers = self.get_headers()
            resp = requests.get(url=url, headers=headers)
            return resp.content
        except Exception as error:
            return error

    def get_pdf(self) -> bytes | Exception:
        """
        Obtém o conteúdo binário do PDF da cobrança Pix.

        Returns:
            bytes | Exception: Arquivo PDF ou exceção.
        """
        pdf_api_url = self.get_pdf_url()
        return self.get_media(pdf_api_url)

    def get_qrcode(self) -> bytes | Exception:
        """
        Obtém o conteúdo binário da imagem QR Code da cobrança Pix.

        Returns:
            bytes | Exception: Imagem QR Code ou exceção.
        """
        qrcode_api_url = self.get_qrcode_url()
        return self.get_media(qrcode_api_url)
