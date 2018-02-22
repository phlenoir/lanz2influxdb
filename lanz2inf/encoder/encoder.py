import lanz_pb2
import logging
from util_functions import influxdb_tag_escaper

class Encoder(object):
    """
    An encoder for the LANZ protobuf format
    """
    def __init__(self):
        self.escape_tag = influxdb_tag_escaper()

    def encode(self, msg):
        measurements = []

        try:
            cgr = lanz_pb2.CongestionRecord
            cgr.ParseFromString(msg)
            logging.debug("Parsed protobuf: %s", msg)

        except ValueError as e:
            cgr = None
            logging.debug("Error in encoder: %s", e)

        """ TODO format influxdb message """

        return measurements


    @staticmethod
    def compose_data(measurement, tags, fields, time):
        data = "{0!s},{1!s} {2!s} {3!s}".format(measurement, tags, fields, time)
        return data

    @staticmethod
    def format_keys(entry, args):
        key = []
        for arg in args:
            if arg in entry:
                # to avoid add None as tag value
                if entry[arg] != '':
                    key.append("{0!s}={1!s}".format(arg, entry[arg]))
        return ','.join(key)
