import pytest
import unittest
from src.algorithms.lsb import encode_lsb, decode_lsb
from src.utils.image_utils import load_image, save_image
from PIL import Image
import os

class TestLSB(unittest.TestCase):

    def setUp(self):
        # Create a simple test image
        self.test_image = Image.new('RGB', (10, 10), color = 'white')
        self.test_image_path = 'test_image.png'
        self.test_output_path = 'output_image.png'
        self.test_message = 'Hello'

        self.test_image.save(self.test_image_path)

    def tearDown(self):
        # Remove the test images
        os.remove(self.test_image_path)
        if os.path.exists(self.test_output_path):
            os.remove(self.test_output_path)

    def test_encode_decode_lsb(self):
        image = load_image(self.test_image_path)
        encoded_image = encode_lsb(image, self.test_message)
        save_image(encoded_image, self.test_output_path)

        # Load the encoded image and decode the message
        encoded_image_loaded = load_image(self.test_output_path)
        decoded_message = decode_lsb(encoded_image_loaded)

        self.assertEqual(self.test_message, decoded_message)

if __name__ == '__main__':
    unittest.main()
