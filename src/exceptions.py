class FileFormatError(Exception):
    def __init__(self, file_type: str = "image"):
        message = f"Incompatible {file_type} format selected."
        super().__init__(message)
