from abc import ABC


class SigmageException(Exception, ABC):
    """SigmageException is the abstract base class for all Sigmage exceptions."""

    def __init__(self) -> None:
        super().__init__(self.__doc__)


class ImageFormatException(SigmageException):
    """ImageFormatException is the exception class raised when the output image format is not png."""
    pass
