#!/usr/bin/env python
#coding: utf-8

# pip install PyCrypto
# sudo apt-get install  build-essential libffi-dev
# pip install bcrypt

from Crypto.Hash import SHA512 # 64 bytes, 512 bits
from Crypto.Protocol.KDF import PBKDF2
import base64

class BaseCipher(object):
    """BaseCipher class"""
    def __init__(self):
        super(BaseCipher, self).__init__()
        self.PADDING = '\x00'

        # 函数：填充字符串至块的倍数
        self.pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING

    def generate_cbc_key(self, password, salt, block_size, key_size):
        # 生成高强度的符合需要的real_key与IV
        password = base64.b64encode(password)
        salt = base64.b64encode(SHA512.new(salt).digest())
        key = PBKDF2(password, salt, key_size)
        iv = PBKDF2(salt, password, block_size)

        return key, iv

from Crypto.Cipher import AES
class AESCipher(BaseCipher):
    """AESCipher, support aes256"""
    def __init__(self, password=None, salt=None):
        super(AESCipher, self).__init__()
        self.BLOCK_SIZE = AES.block_size
        self.KEY_SIZE = 32 # AES256

        if salt is None:
            salt = password

        # 生成CBC模式加密用的KEY与IV
        (self.key, self.iv) = self.generate_cbc_key(password, salt, self.BLOCK_SIZE, self.KEY_SIZE)
        
        # 生成AES对象，使用CBC模式
        self.cipher = AES.new(self.key,AES.MODE_CBC,self.iv)
        # 加密函数
        self.encrypt = lambda msg: base64.b64encode(self.cipher.encrypt(self.pad(msg)))
        # 解密函数
        self.decrypt = lambda msg: self.cipher.decrypt(base64.b64decode(msg)).rstrip(self.PADDING)

from Crypto.Cipher import Blowfish
class BFCipher(BaseCipher):
    """BlowFish Cipher"""
    def __init__(self, password=None, salt=None):
        super(BFCipher, self).__init__()
        self.BLOCK_SIZE = Blowfish.block_size
        self.KEY_SIZE = 56 # 448 bits, the maximum key size, range 32-448 bits
        if salt is None:
            salt = password

        # 生成CBC模式加密用的KEY与IV
        (self.key, self.iv) = self.generate_cbc_key(password, salt, self.BLOCK_SIZE, self.KEY_SIZE)

        # 生成Blowfish对象，使用CBC模式
        self.cipher = Blowfish.new(self.key,Blowfish.MODE_CBC,self.iv)
        # 加密函数
        self.encrypt = lambda msg: base64.b64encode(self.cipher.encrypt(self.pad(msg)))
        # 解密函数
        self.decrypt = lambda msg: self.cipher.decrypt(base64.b64decode(msg)).rstrip(self.PADDING)
#Main
if __name__ ==  '__main__':
    print "Testing... ..."
    
    # 明文，口令与盐
    plaintext = 'this is test'   
    pwd = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    salt = 'xorg.org8'

    # 加密明文    
    cipher = AESCipher(pwd, salt)
    #cipher = BFCipher(pwd, salt)
    ciphertext = cipher.encrypt(plaintext)

    # 解密密文
    cipher = AESCipher(pwd, salt)
    #cipher = BFCipher(pwd, salt)
    plaintext = cipher.decrypt(ciphertext)

    print 'ciphertext:\t' + ciphertext
    print 'plaintext:\t' + plaintext