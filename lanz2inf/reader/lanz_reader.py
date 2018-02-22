import logging
import socket
import sys

from encoder.errors import EncoderError
from reader import ReaderAbstract
from SocketStreamHandler import SocketStreamHandler

class Reader(ReaderAbstract):

    def _connect(self):
        connection = "{0}:{1}".format(self.host, self.port)
        logging.info("Connecting to Lanz at %s...", connection)
        try:
            # Create a TCP/IP socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect the socket to the port where the server is listening
            server_address = (self.host, int(self.port))
            self.sock.connect(server_address)
        except socket.error:
            raise EncoderError(socket.error)


    def _handle_read(self):
        '''Read messages from Lanz.'''
        try:
            handler = SocketStreamHandler(self.sock)
            byte_stream = handler.getData()
        except socket.error:
            raise error.IOError("Error reading data from LANZ")
        finally:
            self.sock.closeSocket(self.sock)
        return byte_stream