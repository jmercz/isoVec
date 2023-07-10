
class FractionError(Exception):
    def __init__(self, message="Unexpected behaviour.", errors={}):
        super().__init__(message)
        self.errors = errors
