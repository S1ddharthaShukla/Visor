import argparse
from PIL import Image
from utils.image_utils import load_image, save_image
from algorithms.lsb import encode_lsb, decode_lsb
from algorithms.lsbm import encode_lsbm, decode_lsbm
from algorithms.rlsb import encode_rlsb, decode_rlsb

def parse_args():
    parser = argparse.ArgumentParser(description="Steganography Tool")
    subparsers = parser.add_subparsers(dest='command', required=True)

    encode_parser = subparsers.add_parser('encode', help='Encode a message into an image')
    encode_parser.add_argument('algorithm', choices=['lsb', 'lsbm', 'rlsb'], help='Encoding algorithm')
    encode_parser.add_argument('input_image', type=str, help='Path to the input image')
    encode_parser.add_argument('output_image', type=str, help='Path to the output image')
    encode_parser.add_argument('message', type=str, help='Message to encode')
    encode_parser.add_argument('--seed', type=int, default=12345, help='Seed for RLSB encoding (only used with RLSB)')

    decode_parser = subparsers.add_parser('decode', help='Decode a message from an image')
    decode_parser.add_argument('algorithm', choices=['lsb', 'lsbm', 'rlsb'], help='Decoding algorithm')
    decode_parser.add_argument('input_image', type=str, help='Path to the input image')
    decode_parser.add_argument('--seed', type=int, default=12345, help='Seed for RLSB decoding (only used with RLSB)')

    return parser.parse_args()

def main():
    args = parse_args()

    if args.command == 'encode':
        if args.algorithm == 'lsb':
            encode_lsb_mode(args.input_image, args.output_image, args.message)
        elif args.algorithm == 'lsbm':
            encode_lsbm_mode(args.input_image, args.output_image, args.message)
        elif args.algorithm == 'rlsb':
            encode_rlsb_mode(args.input_image, args.output_image, args.message, args.seed)
    elif args.command == 'decode':
        if args.algorithm == 'lsb':
            decode_lsb_mode(args.input_image)
        elif args.algorithm == 'lsbm':
            decode_lsbm_mode(args.input_image)
        elif args.algorithm == 'rlsb':
            decode_rlsb_mode(args.input_image, args.seed)

def encode_lsb_mode(input_image_path, output_image_path, message):
    input_image = load_image(input_image_path)
    encoded_image = encode_lsb(input_image, message)
    save_image(encoded_image, output_image_path)
    print(f"Message encoded using LSB and saved to {output_image_path}")

def decode_lsb_mode(input_image_path):
    input_image = load_image(input_image_path)
    message = decode_lsb(input_image)
    print(f"Decoded message using LSB: {message}")

def encode_lsbm_mode(input_image_path, output_image_path, message):
    input_image = load_image(input_image_path)
    encoded_image = encode_lsbm(input_image, message)
    save_image(encoded_image, output_image_path)
    print(f"Message encoded using LSBM and saved to {output_image_path}")

def decode_lsbm_mode(input_image_path):
    input_image = load_image(input_image_path)
    message = decode_lsbm(input_image)
    print(f"Decoded message using LSBM: {message}")

def encode_rlsb_mode(input_image_path, output_image_path, message, seed):
    input_image = load_image(input_image_path)
    encoded_image = encode_rlsb(input_image, message, seed)
    save_image(encoded_image, output_image_path)
    print(f"Message encoded using RLSB with seed {seed} and saved to {output_image_path}")

def decode_rlsb_mode(input_image_path, seed):
    input_image = load_image(input_image_path)
    message = decode_rlsb(input_image, seed)
    print(f"Decoded message using RLSB with seed {seed}: {message}")

if __name__ == "__main__":
    main()
