import pytest
import unittest
from src.algorithms.rlsb import encode_rlsb, decode_rlsb
from PIL import Image
import os

class TestRLSB(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment"""
        self.input_image_path = "test_input_image.png"
        self.output_image_path = "test_encoded_image_rlsb.png"
        self.message = "Hello, RLSB!"
        self.seed = 12345

        # Create a sample image for testing
        self.create_test_image(self.input_image_path)

    def create_test_image(self, path):
        """Create a simple test image"""
        width, height = 100, 100
        image = Image.new('RGB', (width, height), color = 'white')
        image.save(path)

    def test_encode_decode_rlsb(self):
        """Test the encoding and decoding of the message using RLSB"""
        # Load the image
        input_image = Image.open(self.input_image_path)
        
        # Encode the message
        encoded_image = encode_rlsb(input_image, self.message, self.seed)
        encoded_image.save(self.output_image_path)

        # Decode the message
        decoded_image = Image.open(self.output_image_path)
        decoded_message = decode_rlsb(decoded_image, self.seed)

        # Assert that the decoded message is the same as the original message
        self.assertEqual(self.message, decoded_message)

    def tearDown(self):
        """Clean up the test environment"""
        if os.path.exists(self.input_image_path):
            os.remove(self.input_image_path)
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

if __name__ == "__main__":
    unittest.main()
