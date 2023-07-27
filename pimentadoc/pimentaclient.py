# Copyright (C) 2023  Lucas Zunho <lucaszunho17@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from colorama import Fore, Style
import socket

class PimentaClient:
    buffer_size = 1024
    
    def __init__(self, server_addr=("127.0.0.1", 8080)):
        """
        Armazena o endereço do servidor e envia um ECHO.
        
        Args:
            server_addr (tupla): Endereço e porta do PimentaServer.
        """
        self.server_addr = server_addr
        self.echo_msg(self.server_addr)

    @staticmethod
    def echo_msg(addr, msg="ECHO Teste de conexão. Retorne 'ACK'."):
        """
        Envia uma mensagem de ECHO para o endereço especificado.

        Args:
            addr (tupla): Tupla com endereço e porta do servidor.
            msg (string): Mensagem a ser enviada.

        Returns:
            Booleano: 'True' para sucesso e 'False' para falha.
        """
        return_code = True

        # Criando o file descriptor e realizando a conexão com o servidor
        try:
            sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockfd.connect(addr)
        except socket.error as e:
            print(f"{Fore.RED}[Erro]{Style.RESET_ALL} O socket retornou uma exceção: {e}")
            return_code = False

        # Enviando a mensagem de ECHO
        try:
            sockfd.sendall(msg.encode())
            res = sockfd.recv(512)
            print("[ECHO] -> Foi retornado {}".format(res))
        except Exception as e:
            print(f"{Fore.RED}[Erro]{Style.RESET_ALL} O envio do 'ECHO' retornou: {e}")
            return_code = False
        finally:
            sockfd.close()
        return return_code
