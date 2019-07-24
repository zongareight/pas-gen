import random as rnd
import string as s

excluded = '/\\"<>_|'
punctuation = ''

for ch in s.punctuation:
    if ch not in excluded:
        punctuation += ch

symbol_bank = s.ascii_letters + s.digits + punctuation


def pas_gen(length=11):

    while True:
        pas = ''
        pas_valid = [0, 0, 0, 0]

        for i in range(length):
            pas += rnd.choice(symbol_bank)

        for item in pas:
            if item in s.ascii_lowercase:
                pas_valid[0] += 1
            elif item in s.ascii_uppercase:
                pas_valid[1] += 1
            elif item in s.digits:
                pas_valid[2] += 1
            elif item in s.punctuation:
                pas_valid[3] += 1

        if all(pas_valid):
            break

    return pas


if __name__ == '__main__':
    print(pas_gen())
