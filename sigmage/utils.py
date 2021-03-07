from typing import Optional, cast

from stegano import lsb

from sigmage.exceptions import ImageFormatException


def get_signature(input_image: str) -> Optional[str]:
    """Obtains the signature of the image at the supplied path.

    :param input_image: The input image path.
    :return: The signature if the image is signed, else None.
    """
    return cast(str, lsb.reveal(input_image))


def set_signature(input_image: str, output_image: str, signature: str) -> None:
    """Signs the image at the input path with the supplied signature and saves it at the output image path.

       The output image must be of png format because lossless compression is required to sign an image.

    :param input_image: The input image path.
    :param output_image: The output image path.
    :param signature: The signature.
    :return: None.
    :raise ImageFormatException: If the output image format is not png.
    """
    if not output_image or output_image.split('.')[-1] != 'png':
        raise ImageFormatException()

    lsb.hide(input_image, signature).save(output_image, 'png')
