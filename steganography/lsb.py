import argparse
import sys

import numpy as np
from PIL import Image


def encode(cover_fn, secret_fn, output_fn, num_bits):
    cover_im = Image.open(cover_fn)
    secret_im = Image.open(secret_fn)

    # Check for invalid inputs
    if cover_im.format != secret_im.format or cover_im.mode != secret_im.mode:
        print('Error: Format or mode mismatch.')
        sys.exit(1)
    if cover_im.size[0] < secret_im.size[0] or cover_im.size[1] < secret_im.size[1]:
        print('Error: Length or width of secret image cannot exceed length or width of image to hide it in.')
        sys.exit(1)

    cover_im_array = np.array(cover_im)

    # mask the n least significant bits of the cover image
    cover_im_array_n_lsb_masked = cover_im_array & (256 - 2**num_bits)

    # pad secret image array with 0's to match cover image array dims
    secret_im_padded = Image.new('RGB', cover_im.size)
    secret_im_padded.paste(secret_im,
        (
            (cover_im.size[0] - secret_im.size[0]) / 2,
            (cover_im.size[1] - secret_im.size[1]) / 2
        )
    )
    secret_im_padded.save('padded_{}'.format(secret_fn)) # sanity

    # right-shift secret image pixel bytes by 8 - n bits
    secret_im_n_msb_shifted_array = np.array(secret_im_padded) >> (8 - num_bits)

    output_im_array = cover_im_array_n_lsb_masked + secret_im_n_msb_shifted_array

    output_im = Image.fromarray(output_im_array)
    output_im.save(output_fn)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='CLI for least-significant-bit steganography.')
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

    encode(cover_fn, secret_fn, output_fn, num_bits)
