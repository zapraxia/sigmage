from pathlib import Path
from unittest import TestCase, main

from sigmage import ImageFormatException, get_signature, set_signature


class SignatureTestCase(TestCase):
    BASE_DIR = Path(__file__).resolve().parent

    png_input_path = str(BASE_DIR / 'images/dies.png')
    png_output_path = str(BASE_DIR / 'images/dies-signed.png')

    jpg_input_path = str(BASE_DIR / 'images/jones.jpg')
    jpg_output_path = str(BASE_DIR / 'images/jones-signed.jpg')
    jpg_png_output_path = str(BASE_DIR / 'images/jones-signed.png')

    signature = 'AussieSeaweed'

    def test_png(self) -> None:
        self.assertIsNone(get_signature(self.png_input_path))

        set_signature(self.png_input_path, self.png_output_path, self.signature)
        self.assertEqual(get_signature(self.png_output_path), self.signature)

    def test_jpg(self) -> None:
        self.assertIsNone(get_signature(self.jpg_input_path))

        self.assertRaises(ImageFormatException,
                          lambda: set_signature(self.jpg_input_path, self.jpg_output_path, self.signature))

        set_signature(self.jpg_input_path, self.jpg_png_output_path, self.signature)
        self.assertEqual(get_signature(self.jpg_png_output_path), self.signature)


if __name__ == '__main__':
    main()
