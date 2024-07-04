# Steganography Project

This project implements steganography techniques to encode and decode messages within images using various algorithms such as LSB, LSBM, and RLSB. The project includes both a command-line interface and a graphical user interface (GUI) using PyQt5.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface](#command-line-interface)
  - [Graphical User Interface](#graphical-user-interface)
- [Algorithms](#algorithms)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **LSB (Least Significant Bit) Encoding/Decoding**
- **LSBM (Least Significant Bit Matching) Encoding/Decoding**
- **RLSB (Random Least Significant Bit) Encoding/Decoding with Seed**
- **PyQt5 GUI for easy interaction**
- **Command-line interface for advanced users**
- **Unit tests for core functionalities**

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/S1ddharthaShukla/Steganography-Project.git
    cd Steganography-Project
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Command-Line Interface

1. Encode a message into an image:
    ```sh
    python main.py encode -a lsb -i input_image.png -o output_image.png -m "Your secret message"
    ```

2. Decode a message from an image:
    ```sh
    python main.py decode -a lsb -i input_image.png
    ```

3. For help and more options:
    ```sh
    python main.py --help
    ```

### Graphical User Interface

1. Run the GUI:
    ```sh
    python gui.py
    ```

2. Follow the instructions on the GUI to encode or decode messages using the chosen algorithm.

## Algorithms

### LSB (Least Significant Bit)
- Encodes the message by altering the least significant bit of each pixel in the image.

### LSBM (Least Significant Bit Matching)
- Encodes the message by matching the least significant bit of each pixel to the message bit.

### RLSB (Random Least Significant Bit)
- Encodes the message by altering random bits in the image pixels based on a seed for randomness.

## Testing

Run the unit tests using `pytest`:
```sh
pytest
```

## Project Structure

```sh
Steganography-Project/
│
├── data/
|   ├── input_images/
|   |   ├── input_image.png
|   |   ├── input_image_1.png
|   |   └── input_image_2.png
|   └── output_images/
|       ├── lsb_encoded_output_image.png
|       ├── lsbm_encoded_output_image.png
|       └── rlsb_encoded_output_image.png
|
├── src/
│   ├── __init__.py
|   ├── algorithms/
|   |   ├── lsb.py
|   |   ├── lsbm.py
|   |   └── rlsb.py
│   ├── main.py
│   ├── gui.py
│   └── utils/
│       └── image_utils.py
|
├── tests/
│   ├── __init__.py
│   ├── test_image_utils.py
│   ├── test_lsb.py
│   ├── test_lsbm.py
|   └── test_rlsb.py
|
├── requirements.txt
└── README.md
```
