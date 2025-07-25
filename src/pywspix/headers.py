class Headers:
    """
    Gera os cabeçalhos HTTP de autenticação para chamadas à API Pix.

    Essa classe encapsula o usuário e a senha, retornando um dicionário
    de cabeçalhos customizados exigidos pelo serviço.
    """

    def __init__(self, user: str, password: str):
        """
        Inicializa o gerador de headers com credenciais de autenticação.

        Args:
            user (str): Nome de usuário (X-Username).
            password (str): Senha de autenticação (X-Password).
        """
        self.__user = user
        self.__password = password

    def generate(self) -> dict:
        """
        Gera o dicionário de cabeçalhos HTTP com as credenciais.

        Returns:
            dict: Cabeçalhos com campos `X-Username` e `X-Password`.
        """
        header_content = {"X-Username": self.__user, "X-Password": self.__password}
        return header_content
