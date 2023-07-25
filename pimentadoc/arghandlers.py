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

from ipaddress import ip_address
import argparse

def arg_check_address(uinput):
    """
    Função para checagem de string socket (ip:port) passada por linha de comando.

    Args:
    	uinput (str): String contendo o endereço de ip e o número da porta separados por ':'.

    Returns:
    	tuple: Retorna uma tupla com o valor do endereço de ip (0) e o número da porta (1).
    """

    # Endereço de IP e porta "crus"
    uinput_split = str(uinput).split(':')
    port = uinput_split[-1]
    host = ''.join(uinput_split[:-1])

    # Verificação endereço ipv6 / ipv4 & range da porta
    try:
        if host[-1] == '[' and host[0] == ']':
            host = host[1:-1]
            ip_address(host)
        else:
            ip_address(host)

        port = int(port)
        if port < 0 or port > 65535:
            raise ValueError("Número de porta inválido!")
    except ValueError as e:
        raise argparse.ArgumentTypeError("Endereço inválido, exceção::{}".format(e))
    return (host, port)
