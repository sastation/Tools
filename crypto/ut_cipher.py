#!/usr/bin/env python
# coding: utf-8
'''
* Cipher.py unit test via pytest
*
'''
import Cipher

message = 'this is test message'
pwd = 'abcdef123456'
salt = 'xorg.org8'


def test_aes_ctr():
    mode = 'ctr'
    cipher = Cipher.AESCipher(pwd, salt, mode)
    ciphertext = cipher.encrypt(message)
    cipher = Cipher.AESCipher(pwd, salt, mode)
    plaintext = cipher.decrypt(ciphertext)

    assert ciphertext == 'yUdz7od3EVgNGGQ1hyt60lP/2VcJfqwJQ7Aio3Nvrv4='
    assert plaintext == message


def test_aes_crc():
    mode = 'crc'
    cipher = Cipher.AESCipher(pwd, salt, mode)
    ciphertext = cipher.encrypt(message)
    cipher = Cipher.AESCipher(pwd, salt, mode)
    plaintext = cipher.decrypt(ciphertext)

    assert ciphertext == 'QW/icn8+hd1z2h+rdCaN3/wsbyfL6m+4b6yQEEB4lO0='
    assert plaintext == message


def test_bf_ctr():
    mode = 'ctr'
    cipher = Cipher.BFCipher(pwd, salt, mode)
    ciphertext = cipher.encrypt(message)
    cipher = Cipher.BFCipher(pwd, salt, mode)
    plaintext = cipher.decrypt(ciphertext)

    assert ciphertext == 'iYZ/bFGsSWNaj8Aqwy170+txNuJVUNnG'
    assert plaintext == message


def test_bf_crc():
    mode = 'crc'
    cipher = Cipher.BFCipher(pwd, salt, mode)
    ciphertext = cipher.encrypt(message)
    cipher = Cipher.BFCipher(pwd, salt, mode)
    plaintext = cipher.decrypt(ciphertext)

    assert ciphertext == 'IEWiTsfYb43ZojcwF19N+8dd0fRQcytj'
    assert plaintext == message


# Main
if __name__ == '__main__':
    print "Testing... ..."
