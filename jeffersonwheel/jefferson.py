
wheels = []
def get_wheels(istream):
    line = istream.readline().strip()
    while len(line) > 0:
        wheels.append(list(line))
        line = istream.readline().strip()
#

def translate(wheelindex, letter, offset):
    wheel = wheels[wheelindex]
    index = wheel.index(letter)
    return wheel[(len(wheel)+index+offset)%len(wheel)]
#

def align_rotate(text, offset):
    return ''.join([translate(i%len(wheels), text[i], offset) for i in range(len(text))])
def encode(clear):
    return align_rotate(clear, 2)
def decode(cipher):
    return align_rotate(cipher, -2)
#

