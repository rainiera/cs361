# steganography

**Requirements** (with Python 2 and `pip`: `Pillow`, `numpy`)

**Example** (using 5 LSBs for _demonstration_ (easy visual attack), used to create out.png in repo)

```
python lsb.py teapot.png secret.png 5 out.png
```

**Original proposal**

We are going to write a Python program that implements least significant bit steganography. It will be a command line program that takes in three additional command line arguments as inputs. These inputs will be a cover image filename, a secret image filename, a flag for the number of least significant bits to use from the cover image, and the output will be an image file that ideally should look visually similar to the original cover image, but encodes the secret image. The input requirements shall be that the cover image be larger than the secret image.

Our program will most likely use a Python image library called Pillow to transform the cover image byte data into an easily-manipulated pixel-wise rgb/intensity bits representation and replace the specified number of least significant bits from the cover image with that of the secret image's, similarly loaded into an easily-manipulated data structure. It will then write the transformed cover image bits representation to the specified output file.



