# steganography

**Group Info**

Team Rocket:
Rainier Ababao,
Kieran Vanderslice

**Requirements** (with Python 2 and `pip`: `Pillow`, `numpy`)

**Introduction/Original proposal**

We are going to write a Python program that implements least significant bit steganography. It will be a command line program that takes in three additional command line arguments as inputs. These inputs will be a cover image filename, a secret image filename, a flag for the number of least significant bits to use from the cover image, and the output will be an image file that ideally should look visually similar to the original cover image, but encodes the secret image. The input requirements shall be that the cover image be larger than the secret image.

Our program will use a Python image library called Pillow to transform the cover image byte data into an easily-manipulated pixel-wise rgb/intensity bits representation and replace the specified number of least significant bits from the cover image with that of the secret image's, similarly loaded into an easily-manipulated data structure. It will then write the transformed cover image bits representation to the specified output file.

**Algorithm**

Our LSB algorithm that we implemented takes in the given images and places the pixel values of these images into arrays that we can manipulate. Then for each pixel that we are manipulating to hide the secret image we use a mask to clear out the x least significant bits of the cover image, where x is the third command line argument provided and get only the x most significant bits of the secret image. We then replace the x bits we just cleared out from the cover image with the x most significant bits from the secret image. 

**Example** (using 5 LSBs for _demonstration_ (easy visual attack), used to create out.png in repo)

```
python lsb.py teapot.png secret.png 5 out.png
```

**Major Points**

- Accepts any image type that can be opened by PIL
- Error checking to ensure cover image and secret image are compatible
- User can specifiy with a commnad line argument how many least significant bits they wish to use
- User can specify their output destination
