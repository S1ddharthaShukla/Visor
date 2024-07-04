import pytest
import unittest
from src.algorithms.lsbm import encode_lsbm, decode_lsbm
from src.utils.image_utils import load_image, save_image
from PIL import Image
import os

class TestLSBM(unittest.TestCase):

    def setUp(self):
        # Create a simple test image
        self.test_image = Image.new('RGB', (10, 10), color = 'white')
        self.test_image_path = 'test_image_lsbm.png'
        self.test_output_path = 'output_image_lsbm.png'
        self.test_message = 'Hello, LSBM!'

        self.test_image.save(self.test_image_path)

    def tearDown(self):
        # Remove the test images
        os.remove(self.test_image_path)
        if os.path.exists(self.test_output_path):
            os.remove(self.test_output_path)

    def test_encode_decode_lsbm(self):
        image = load_image(self.test_image_path)
        encoded_image = encode_lsbm(image, self.test_message)
        save_image(encoded_image, self.test_output_path)

        encoded_image_loaded = load_image(self.test_output_path)
        decoded_message = decode_lsbm(encoded_image_loaded)

        self.assertEqual(self.test_message, decoded_message)

if __name__ == '__main__':
    unittest.main()
