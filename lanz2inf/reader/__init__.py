import importlib


def load_reader(name, host, port):
    """
    Creates an instance of the given reader.
    An reader reads messages from Lanz.
    """
    reader_module = importlib.import_module(name)
    reader_class = getattr(reader_module, "Reader")
    # Return an instance of the class
    return reader_class(host, port)