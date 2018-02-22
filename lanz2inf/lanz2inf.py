"""
Created on 31 jan 2018

@author: Philippe Lenoir
"""

from __future__ import print_function

import logging
import os
import sys

from config import loader
from encoder import load_encoder
from reader import load_reader
from worker import Worker
from writer import influxdb_writer

__title__ = 'lanz2inf'
__version__ = '0.0.1'


def start_consumer(config):
    """
    Start metrics consumer
    :param config:
    """
    logging.debug("Initializing Lanz Consumer")
    reader = load_reader(
        config.lanz_reader,
        config.lanz_host,
        config.lanz_port
    )
    logging.debug("Initializing connection to InfluxDB at %s:%s",
                  config.influxdb_host, config.influxdb_port)
    writer = create_writer(config)
    logging.debug("Initializing message encoder: %s", config.encoder)
    encoder = load_encoder(config.encoder)
    client = Worker(reader, encoder, writer, config)
    client.consume()


def create_writer(config):
    """
    Create InfluxDB writer
    """
    return influxdb_writer.InfluxDBWriter(config.influxdb_host,
                                          config.influxdb_port,
                                          config.influxdb_user,
                                          config.influxdb_password,
                                          config.influxdb_dbname,
                                          config.influxdb_use_ssl,
                                          config.influxdb_verify_ssl,
                                          config.influxdb_timeout,
                                          config.influxdb_use_udp,
                                          config.influxdb_retention_policy,
                                          config.influxdb_time_precision)


def show_version():
    """
    Output current version and exit
    """
    print("{} {}".format(__title__, __version__))
    sys.exit(0)


if __name__ == '__main__':
    FORMAT = '%(asctime)-15s %(name)s:%(levelname)s:%(message)s'
    logging.basicConfig(format=FORMAT)
    config = loader.load_config()
    if config.version:
        show_version()

    # Check for a pidfile to see if the program already runs
    try:
        pf = file(config.pidfile, 'r')
        pid = int(pf.read().strip())
        pf.close()
    except IOError:
        pid = None
    if pid:
        message = "pidfile %s already exist. Daemon already running?\n"
        sys.stderr.write(message % config.pidfile)
        sys.exit(1)
    pid = str(os.getpid())
    file(config.pidfile, 'w+').write("%s\n" % pid)
    start_consumer(config)
