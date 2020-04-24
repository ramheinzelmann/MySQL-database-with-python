#!/usr/bin/python
# coding: utf8
"""
Date: 19/06/2018
Autor: Renato Machado
Abjective: Performs a MySQL connection.
Alteration:
"""

import pymysql
import os


def connection_db(database):
    try:
        db = pymysql.connect(host=os.environ['MYSQL_HOST'],
                             user=os.environ['MYSQL_USERNAME'],
                             password=os.environ['PASSWORD_MYSQL_USER'],
                             db=database)
        cursor = db.cursor()
        return cursor, db, 200

    except Exception as e:
        print(e)
        msg = 'Connection to the database failed.'
        return {'erro': msg}, 401
