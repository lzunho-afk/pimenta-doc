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

import os
import sys
import threading
import socket
import socketserver
import glob

class ThreadedServerHandler(socketserver.BaseRequestHandler):
    """ Manipulador de requisições TCP """
    def handle(self, buffer_size):
        data = self.request.recv(buffer_size)
        current_thread = threading.current_thread()
        res = "{}: {}".format(current_thread, data)
        self.request.sendall(res.encode())

class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class PimentaServer:
    serv_threads = []
    handlers_list = []
    
    def __init__(self, address=("localhost", 0)):
        """ Construtor da classe PimentaServer.
        Inicializa o thread do serviço mestre e inicializa o handler dele.
        
        :param address: Tupla com os valores de endereço do servidor.
        """
        self.server = ThreadedServer(address, ThreadedServerHandler)
        self.host, self.port = self.server.server_address
        serv_thread = threading.Thread(target=self.server.serve_forever)
        serv_thread.daemon = True
        self.serv_threads.append(serv_thread)
        serv_thread.start()
        #print("[*] Rodando serviço 'master' ~> PimentaServer (Thread: {})".format(serv_thread.name))
        #print("\t~> Inicializando 'slaves' \{\n{}\n\}".format(self.start_side_services()))

    def load_service_handlers(directory):
        """ Carrega todos os phandlers de determinado diretório para o contexto de serviços do Servidor.
        :param directory: Caminho para o diretório com os arquivos '.phandler' (String).
        """
        print("[Handlers] Loading from '{}'".format(directory))
        for handler_path in glob.glob(directory + '/**/*.phandler', recursive=True):
            with open(handler_path, 'r', encoding="utf-8") as f:
                handler_create_service(f.read())
                print("\t~> {}... Done.".format(handler_path))

    def handler_create_service(handler_text):
        """ Cria um serviço a partir do texto de phandler.
        :param handler: Texto integral do arquivo '.phandler' (String List).
        :returns: 'False' caso não seja possível a criação e 'True' caso contrário.
        """
        pass
