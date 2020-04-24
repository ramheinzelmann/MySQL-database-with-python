#!/usr/bin/python
# coding: utf8
"""
Date: 19/06/2018
Autor: Renato Machado
Abjective: Creates a 16-character password, inserts a hash into the password and validates the password for future
           access.
Alteration:
"""

import random
import bcrypt


def create_password(num_caract):

    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&"
    if num_caract != 16:
        return {'erro': 'Falha na criação da senha.'}

    passwd = ""
    while len(passwd) != num_caract:
        passwd = passwd + random.choice(char)
    if len(passwd) == num_caract:
        return passwd


class TrataHash(object):

    @staticmethod
    def insere_hash(passwd):
        hash_passwd = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
        return hash_passwd

    @staticmethod
    def validates_senha(password, hash_passwd):
        return bcrypt.hashpw(password.encode('utf-8'), hash_passwd.encode('utf-8')) == hash_passwd.encode('utf-8')
