', '.join(['0x0{}'.format(letter) for letter in [['00102030405060708090a0b0c0d0e0f0'[i:i+2] for i in range(0, len('00102030405060708090a0b0c0d0e0f0'), 2)]]])

h = '00102030405060708090a0b0c0d0e0f0'
h = 'a7be1a6997ad739bd8c9ca451f618b61'
print(', '.join(['0x{}'.format(h[i : i + 2]) for i in range(0, len(h), 2)]))
