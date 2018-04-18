import argparse


def get_file_and_pad(inputfile, keysize):
    """Opens inputfile and pads it with an amount of zero-bytes based on keysize
    """
    mutable_data = None
    with open(inputfile, 'rb') as binary_file:
        mutable_data = bytearray(binary_file.read())
        num_bytes = len(mutable_data)
        num_bits = num_bytes * 4
        print('Original data length {} bytes, or {} bits'.format(num_bytes, num_bits))

        # Add padding to file bytearray, if needed
        required_padding = keysize - (len(mutable_data) % keysize)
        for _ in range(required_padding):
            mutable_data.append(0)

        print('Input file padded with {} bytes'.format(required_padding))
        print([byte for byte in mutable_data])
    return mutable_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--keysize', help='Either 128 or 256 bits')
    parser.add_argument('--keyfile', help='A keyfile that fits either 128 or 256 bits')
    parser.add_argument('--inputfile', help='Location of the input file')
    parser.add_argument('--outputfile', help='Where to save the result')
    parser.add_argument('--mode', help='Encrypt or decrypt')
    args = parser.parse_args()
    print([byte for byte in get_file_and_pad(args.inputfile, int(args.keysize))])
