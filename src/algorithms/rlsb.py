from PIL import Image
import random

def encode_rlsb(image: Image.Image, message: str, seed: int) -> Image.Image:
    """
    Encodes a message into an image using the Randomized LSB technique with a consistent seed.
    
    Parameters:
        image (Image.Image): The input image in which the message will be encoded.
        message (str): The message to encode in the image.
        seed (int): The seed for the random number generator to ensure consistency.
    
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

    # Generate random pixel positions with the given seed
    random.seed(seed)
    pixel_positions = [(x, y) for y in range(height) for x in range(width)]
    random.shuffle(pixel_positions)

    for x, y in pixel_positions:
        if idx >= len(binary_message):
            break  # Exit loop if all message bits are encoded

        r, g, b = pixels[x, y]

        # Modify LSB of each color component
        r = (r & 0xFE) | int(binary_message[idx]) if idx < len(binary_message) else r
        idx += 1
        g = (g & 0xFE) | int(binary_message[idx]) if idx < len(binary_message) else g
        idx += 1
        b = (b & 0xFE) | int(binary_message[idx]) if idx < len(binary_message) else b
        idx += 1

        pixels[x, y] = (r, g, b)

    return encoded_image

def decode_rlsb(image: Image.Image, seed: int) -> str:
    """
    Decodes a message from an image using the Randomized LSB technique with a consistent seed.
    
    Parameters:
        image (Image.Image): The input image from which the message will be decoded.
        seed (int): The seed for the random number generator to ensure consistency.
    
    Returns:
        str: The decoded message.
    """
    pixels = image.load()
    width, height = image.size

    binary_message = []
    # Generate random pixel positions with the given seed
    random.seed(seed)
    pixel_positions = [(x, y) for y in range(height) for x in range(width)]
    random.shuffle(pixel_positions)

    for x, y in pixel_positions:
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
    input_image_path = "input_image.png"
    output_image_path = "encoded_image_rlsb.png"
    message_to_encode = "Hello, Randomized LSB!"
    seed = 12345  # Use a consistent seed for both encoding and decoding

    # Load the image
    input_image = Image.open(input_image_path)

    # Encode the message
    encoded_image = encode_rlsb(input_image, message_to_encode, seed)

    # Save the encoded image
    encoded_image.save(output_image_path)

    # Decode the message
    decoded_image = Image.open(output_image_path)  # Reload the image from file to ensure consistency
    decoded_message = decode_rlsb(decoded_image, seed)
    print(f"Decoded message: {decoded_message}")
