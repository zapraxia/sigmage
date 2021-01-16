from abc import ABC


class SigmageException(Exception, ABC):
    """SigmageException is the base class for all exceptions in sigmage."""

    def __init__(self):
        super().__init__(self.__doc__)


class ImageFormatException(SigmageException):
    """The output image format is not png."""
    pass
