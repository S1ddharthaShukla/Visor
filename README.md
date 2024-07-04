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
    git clone https://github.com/yourusername/steganography.git
    cd steganography
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
