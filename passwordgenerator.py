import argparse
import string
import random


def main():
    length = get_parameters()
    password = generate_password(length)
    print(f'password = {password}')


def generate_password(length):
    alphabet = string.digits + string.ascii_letters + string.punctuation
    return "".join(random.choices(alphabet, k=length))


def get_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'length',
        help='Give the desired length.',
        type=int
    )
    return parser.parse_args().length

if __name__ == '__main__':
    main()
