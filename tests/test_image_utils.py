import pytest
import unittest
from src.utils.image_utils import load_image, save_image
from PIL import Image
import os

class TestImageUtils(unittest.TestCase):

    def setUp(self):
        self.test_image = Image.new('RGB', (10, 10), color = 'white')
        self.test_image_path = 'test_image.png'
        self.test_image.save(self.test_image_path)

    def tearDown(self):
        os.remove(self.test_image_path)

    def test_load_image(self):
        image = load_image(self.test_image_path)
        self.assertIsInstance(image, Image.Image)

    def test_save_image(self):
        image = load_image(self.test_image_path)
        output_path = 'output_image.png'
        save_image(image, output_path)
        self.assertTrue(os.path.exists(output_path))
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()
