from PIL import Image
import random

def encode_lsbm(image: Image.Image, message: str) -> Image.Image:
    """
    Encodes a message into an image using the LSB Matching technique.
    
    Parameters:
        image (Image.Image): The input image in which the message will be encoded.
        message (str): The message to encode in the image.
    
    Returns:
        Image.Image: The output image with the encoded message.
    """
    # Convert message to binary
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    binary_message += '00000000'  # Delimiter to indicate end of message

    encoded_image = image.copy()
    pixels = encoded_image.load()

    width, height = image.size
    idx = 0  # Index to track position in binary message

    for y in range(height):
        for x in range(width):
            if idx >= len(binary_message):
                return encoded_image  # Return encoded image once all message bits are encoded

            r, g, b = pixels[x, y]

            # Modify LSB of each color component using LSB Matching
            if (r & 0x01) != int(binary_message[idx]):
                r = (r + random.choice([-1, 1])) & 0xFF
            if idx + 1 < len(binary_message):
                if (g & 0x01) != int(binary_message[idx + 1]):
                    g = (g + random.choice([-1, 1])) & 0xFF
            if idx + 2 < len(binary_message):
                if (b & 0x01) != int(binary_message[idx + 2]):
                    b = (b + random.choice([-1, 1])) & 0xFF

            pixels[x, y] = (r, g, b)

            idx += 3  # Move to the next set of bits

    return encoded_image

def decode_lsbm(image: Image.Image) -> str:
    """
    Decodes a message from an image using the LSB Matching technique.
    
    Parameters:
        image (Image.Image): The input image from which the message will be decoded.
    
    Returns:
        str: The decoded message.
    """
    pixels = image.load()
    width, height = image.size

    binary_message = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Extract LSB of each color component
            binary_message.append(r & 0x01)
            binary_message.append(g & 0x01)
            binary_message.append(b & 0x01)

    # Group bits into bytes and convert to characters
    message = ''.join(chr(int(''.join(map(str, binary_message[i:i+8])), 2)) for i in range(0, len(binary_message), 8))
    
    # Find the delimiter and trim the message
    delimiter_index = message.find('\x00')
    if delimiter_index != -1:
        message = message[:delimiter_index]

    return message

if __name__ == "__main__":
    # Example usage
    input_image_path = "data/input images/input_image.png"
    output_image_path = "encoded_image_lsbm.png"
    message_to_encode = "Hello, LSB Matching!"

    # Load the image
    input_image = Image.open(input_image_path)

    # Encode the message
    encoded_image = encode_lsbm(input_image, message_to_encode)

    # Save the encoded image
    encoded_image.save(output_image_path)

    # Decode the message
    decoded_message = decode_lsbm(encoded_image)
    print(f"Decoded message: {decoded_message}")

