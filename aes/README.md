Group:
Kieran Vanderslice
Rainier Ababao

Language: Python 3

Notes: 
- We implimented assuming that the ascii chars provided in the input file are hex values of the bytes (i.e. "1cf403b782" correspond to "0x1c 0xf4 0x03 0xb7 0x82")
- Our program concatenates all of the 16 byte state blocks together for the output file
- On the case where the input is a multiple of 16 bytes exactly, we still add 16 bytes of padding to the end
- We print the result of each intermediate step for each round for both encryption and decryption to the console to help with debugging and seeing what going on

Example Command to Run:
python aes.py --keysize $KEYSIZE --keyfile $KEYFILE --inputfile $INPUTFILE --outputfile $OUTFILENAME --mode $MODE

● keysize: Either 128 or 256 bits
● keyfile: Should take in a keyfile that fits one of the specified sizes. To generate a key, use: head -c 16 < /dev/urandom > key (this generates 16 random bytes ~ 128 bits)
● inputfile: This should be able to handle any file and any size (padding might be required). All we care is the bytes of the file. To get the byte representation of a file use xxd.
	❍ For example, a file that says "Hello World" will actually have a byte representation of 4865 6c6c 6f20 576f 726c 640a
● outpfile: what to save the result
● mode: encrypt or decrypt