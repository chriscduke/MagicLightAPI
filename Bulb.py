# No confidence
import socket
import sys
import inspect
import types

Colors = dict(
             blue = "310000ff00f00f2f",
             red = "31ff000000f00f2f",
             green = "3100ff0000f00f2f",
             white = "31000000ff0f0f4e"
             )

Controls = dict(
                on = "71230fa3",
                off = "71240fa4"
               )

AllOptions = dict(Colors)
AllOptions.update(Controls)

class Bulb(object):

    def __init__(self, ip):
        self.port = 5577
        self.ip = ip
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))

    def shutdown(self):
        """
        :param: str : string data input
        """
        self.sock.close()

    def _decode(self, data):
        """
        :param: str : string data input
        """
        return data.decode('hex')

    def _send_data(self, hex_string):
        """
        :param: str : hex 
        """
        self.sock.sendall(self._decode(hex_string))

    def green(self):
        self.genericMethod()

    def blue(self):
        self.genericMethod()

    def red(self):
        self.genericMethod()

    def white(self):
        self.genericMethod()

    def off(self):
        self.genericMethod()

    def on(self):
        self.genericMethod()

    def genericMethod(self):
        frame = inspect.currentframe()
        generatedName = inspect.getframeinfo(inspect.currentframe().f_back)[2]
        self._send_data(AllOptions[generatedName])
