', '.join(['0x0{}'.format(letter) for letter in [['00102030405060708090a0b0c0d0e0f0'[i:i+2] for i in range(0, len('00102030405060708090a0b0c0d0e0f0'), 2)]]])

h = '00112233445566778899aabbccddeeff'
h = '00112233445566778899aabbccddeeff'
print(', '.join(['0x{}'.format(h[i : i + 2]) for i in range(0, len(h), 2)]))
