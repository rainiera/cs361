from PIL import Image
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI for least-significant-bit steganography.')
    im = Image.open('teapot.png')
    print(im.format, im.size, im.mode)
