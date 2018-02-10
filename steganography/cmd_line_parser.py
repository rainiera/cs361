import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI for least-significant-bit steganography.')
    parser.add_argument('cover_file', action="store")
    parser.add_argument('secret_file', action="store")
    parser.add_argument('flag', action="store", type=int)

    list = parser.parse_args()
    print list.cover_file
    print list.secret_file
    print list.flag