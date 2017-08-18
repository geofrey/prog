import jefferson
import frequency

jefferson.get_wheels(open('jefferson.wheel', 'r'))
cipher = 'VAPJKHLUPQ'
print(jefferson.decode(cipher))
print(jefferson.encode('MINECRAFT'))

print()

def cleartextsearch(ciphertext):
    rotations = [jefferson.align_rotate(ciphertext, i) for i in range(26)]
    rotations.sort(key=lambda text: -frequency.deviation(frequency.frequencies(text)))
    return rotations[-3:] # top three matches
#

print('\n'.join(cleartextsearch('BOLRGLTIJ')))

