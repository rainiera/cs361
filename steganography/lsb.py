import argparse
import sys

from PIL import Image


def encode(cover_fn, secret_fn, output_fn):
    cover_im = Image.open(cover_fn)
    secret_im = Image.open(secret_fn)

    # invalid input checking
    if cover_im.format != secret_im.format or cover_im.mode != secret_im.mode:
        print('Error: Format or mode mismatch.')
        sys.exit(1)
    if cover_im.size[0] < secret_im.size[0] or cover_im.size[1] < secret_im.size[1]:
        print('Error: Length or width of secret image cannot exceed length or width of image to hide it in.')
        sys.exit(1)

    # do encoding here



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI for least-significant-bit steganography.')
    parser.add_argument('cover_fn', action="store")
    parser.add_argument('secret_fn', action="store")
    parser.add_argument('num_bits', action="store", type=int)
    parser.add_argument('output_fn', action="store", default='output.png')

    args = parser.parse_args()
    cover_fn = args.cover_fn
    secret_fn = args.secret_fn
    output_fn = args.output_fn
    num_bits = args.num_bits
    print('Using {} as cover image filename'.format(cover_fn))
    print('Using {} as secret image filename'.format(secret_fn))
    print('Using {} as number of least significant bits to use'.format(num_bits))
    print('Using {} as output image filename'.format(output_fn))

    encode(cover_fn, secret_fn, output_fn)

