import requests
from pywspix.headers import Headers
from urllib.parse import urljoin


class WSPixFile:
    def __init__(self, baseurl: str, headers: Headers, idfpix: str):
        self.__baseurl = baseurl
        self.__headers = headers
        self.__idfpix = idfpix

    def get_baseurl(self):
        return self.__baseurl
    
    def get_headers(self):
        return self.__headers.generate()
    
    def get_idfpix(self):
        return self.__idfpix

    def generate_file_url(self, media_type: str):
        baseurl = self.get_baseurl()
        idfpix = self.get_idfpix()
        uri = f"/pix/{idfpix}/{media_type}"
        url = urljoin(baseurl, uri)
        return url
    
    def get_pdf_url(self):
        return self.generate_file_url(media_type="pdf")
    
    def get_qrcode_url(self):
        return self.generate_file_url(media_type="qrcode")

    def get_media(self, url: str):
        try:
            headers = self.get_headers()
            resp = requests.get(url=url, headers=headers)
            return resp.content
        except Exception as error:
            return error

    def get_pdf(self):
        pdf_api_url = self.get_pdf_url()
        return self.get_media(pdf_api_url)

    def get_qrcode(self):
        qrcode_api_url = self.get_qrcode_url()
        return self.get_media(qrcode_api_url)
    