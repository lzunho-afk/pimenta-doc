#!/usr/bin/env python3
# pimenta-doc -- software gerenciador básico de serviços e usuários
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
import argparse
import pimentaserver

D_HANDLERS_PATH = os.path.realpath(os.path.dirname(__file__)) + "/default_handlers"

def main():
        global D_HANDLERS_PATH
        argp = argparse.ArgumentParser(prog="pimenta-doc", description="software gerenciador básico de serviços e usuários")
	sargp = argp.add_subparsers(dest="exec_mode", help="Painel de ajuda: Escolha de modos Servidor-Cliente", default="client")

        # argp servidor
        server_argp = sargp.add_parser("server", help="Carrega os módulos/realiza a execução do servidor pimenta")
        server_argp.add_argument('--address', '-addr', action="store", dest="address", help="Define o endereço e porta do servidor pimentadoc ('mestre').\nEx.: 192.168.1.200:8080.", default="127.0.0.1:0")
        server_argp.add_argument('--load-handlers-from', '-lhfrom', action="store", dest="load_bhandlers_dir", help="Específica um ou mais diretórios para carregar bhandlers (separação por ';').\nEx.: /home/asd/call_ha;/etc/handlers.")

        # argp cliente
        client_argp = sargp.add_parser("client", help="Carrega os módulos/realiza a execução do cliente pimenta")

        args = argp.parse_args()

        if args.exec_mode == 'server':
                server = pimentaserver.PimentaServer(args.address)
                server.load_service_handlers(D_HANDLERS_PATH)
                if args.load_bhandlers_dir:
                        with args.load_bhandlers_dir.split(';') as bhandler:
                                server.load_service_handlers(bhandler)
        elif args.exec_mode == 'client':
                pass

if __name__ == "__main__":
	main()
