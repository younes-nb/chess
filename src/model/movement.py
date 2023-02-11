class Movement:
    def __init__(self, source: tuple, destination: tuple):
        self.source = source
        self.destination = destination
        self.captured = None
        self.promoted = None
