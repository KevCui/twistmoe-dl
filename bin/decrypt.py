#!/usr/bin/env python3
from Crypto.Cipher import AES
from hashlib import md5
import argparse
import base64


def unpad(data):
    return data[:-(data[-1] if type(data[-1]) == int else ord(data[-1]))]


def bytes_to_key(data, salt, output=48):
    assert len(salt) == 8, len(salt)
    data += salt
    key = md5(data).digest()
    final_key = key
    while len(final_key) < output:
        key = md5(key + data).digest()
        final_key += key
    return final_key[:output]


def decrypt(encrypted, passphrase):
    encrypted = base64.b64decode(encrypted)
    assert encrypted[0:8] == b"Salted__"
    salt = encrypted[8:16]
    key_iv = bytes_to_key(passphrase, salt, 32+16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(encrypted[16:]))


def print_decrypted_text(encrypted, key):
    print('---')
    print(encrypted)
    print(decrypt(encrypted.encode('utf-8'), key).decode('utf-8'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--string', nargs=1, dest='string', help='encrypted string')
    parser.add_argument('-f', '--file', nargs=1, dest='file', help='encrypted file')

    args = parser.parse_args()
    KEY = b"267041df55ca2b36f2e322d05ee2c9cf"

    if args.string:
        print_decrypted_text(args.string[0], KEY)

    if args.file:
        with open(args.file[0]) as fn:
            for l in fn.readlines():
                print_decrypted_text(l, KEY)


if __name__ == '__main__':
    main()
