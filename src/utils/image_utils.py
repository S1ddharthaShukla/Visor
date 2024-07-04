from PIL import Image

def load_image(image_path):
    """
    Load an image from the given file path.
    
    Parameters:
    image_path (str): The path to the image file.
    
    Returns:
    Image: The loaded image object.
    """
    try:
        image = Image.open(image_path)
        print(f"Image loaded successfully from {image_path}")
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        raise

def save_image(image, save_path):
    """
    Save the given image to the specified file path.
    
    Parameters:
    image (Image): The image object to save.
    save_path (str): The path to save the image file.
    """
    try:
        image.save(save_path)
        print(f"Image saved successfully to {save_path}")
    except Exception as e:
        print(f"Error saving image: {e}")
        raise

def resize_image(image, size):
    """
    Resize the given image to the specified size.
    
    Parameters:
    image (Image): The image object to resize.
    size (tuple): The desired size as a tuple (width, height).
    
    Returns:
    Image: The resized image object.
    """
    try:
        resized_image = image.resize(size)
        print(f"Image resized to {size}")
        return resized_image
    except Exception as e:
        print(f"Error resizing image: {e}")
        raise

def convert_image_to_grayscale(image):
    """
    Convert the given image to grayscale.
    
    Parameters:
    image (Image): The image object to convert.
    
    Returns:
    Image: The converted grayscale image object.
    """
    try:
        grayscale_image = image.convert('L')
        print("Image converted to grayscale")
        return grayscale_image
    except Exception as e:
        print(f"Error converting image to grayscale: {e}")
        raise

def show_image(image):
    """
    Display the given image.
    
    Parameters:
    image (Image): The image object to display.
    """
    try:
        image.show()
        print("Image displayed successfully")
    except Exception as e:
        print(f"Error displaying image: {e}")
        raise

def get_image_size(image):
    """
    Get the size of the given image.
    
    Parameters:
    image (Image): The image object to get the size of.
    
    Returns:
    tuple: The size of the image as a tuple (width, height).
    """
    try:
        size = image.size
        print(f"Image size: {size}")
        return size
    except Exception as e:
        print(f"Error getting image size: {e}")
        raise

def convert_image_to_rgb(image):
    """
    Convert the given image to RGB mode.
    
    Parameters:
    image (Image): The image object to convert.
    
    Returns:
    Image: The converted RGB image object.
    """
    try:
        rgb_image = image.convert('RGB')
        print("Image converted to RGB")
        return rgb_image
    except Exception as e:
        print(f"Error converting image to RGB: {e}")
        raise
