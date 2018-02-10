import argparse
import sys

from PIL import Image


def encode(input_fn, secret_fn, output_fn):
    input_im = Image.open(input_fn)
    secret_im = Image.open(secret_fn)

    # invalid input checking
    if input_im.format != secret_im.format or input_im.mode != secret_im.mode:
        print('Error: Format or mode mismatch.')
        sys.exit(1)
    if input_im.size[0] < secret_im.size[0] or input_im.size[1] < secret_im.size[1]:
        print('Error: Length or width of secret image cannot exceed length or width of image to hide it in.')
        sys.exit(1)

    # do encoding here



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI for least-significant-bit steganography.')
    input_fn = 'teapot.png'
    secret_fn = 'secret.png'
    output_fn = 'output.png'
    encode(input_fn, secret_fn, output_fn)
