import random
import string


def generate_strong_password(length: int):
    collect_data = ''
    punctuations = '[.),("?}!:];{'

    collect_data += (''.join(random.choice(string.digits) for _ in range(length)))
    collect_data += (''.join(random.choice(string.ascii_lowercase) for _ in range(length)))
    collect_data += (''.join(random.choice(string.ascii_uppercase) for _ in range(length)))
    collect_data += (''.join(random.choice(punctuations) for _ in range(length)))

    shuffle_pass = list(collect_data)
    random.shuffle(shuffle_pass)
    return ''.join(shuffle_pass)[:length]


print(generate_strong_password(15))
