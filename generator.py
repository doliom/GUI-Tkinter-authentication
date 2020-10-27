from random import sample

PASS_PHRASE = (
        'abcdefghijklmnopqrstuvwxyz' +
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
        '+=-*'
)

def generate(count=1, length=6, chars=PASS_PHRASE):
    if count == 1:
        return ''.join(sample(chars, length))
    passwords = []
    while count > 0:
        passwords.append(''.join(sample(chars, length)))
        count -= 1
    return passwords
