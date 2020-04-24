#!/usr/bin/python
# coding: utf8
"""
Date: 19/06/2018
Autor: Renato Machado
Abjective: Executes the SQL commands.
Alteration:
"""

import pymysql
from connect import connection_db


class Execute_Sql(object):

    @staticmethod
    def create_table(database, table, query_sql):

        cursor = connection_db(database)
        if cursor[1] == 401:
            print(cursor[0])
            return cursor[0]

        try:
            cursor[0].execute(query_sql)
            print(f'Table {table} successfully created.')

        except pymysql.err.InternalError:
            print(f'Table {table} already exists')
            return {'erro': f'Table {table} already exists'}

    @staticmethod
    def insert_user(database, payload):

        cursor = connection_db(database)
        if cursor[1] == 401:
            print(cursor[0])
            return cursor[0]

        try:
            sql = f"select * from users where username='{payload['username']}'"
            user_exists = cursor[0].execute(sql)

            if not user_exists:
                import password
                passwd = password.create_password(16)
                password = password.TrataHash.insere_hash(passwd)

                val = (payload['username'], payload['email'], str(password))
                sql = f"insert into users (username, email, password) values {val}"

                cursor[0].execute(sql)
                cursor[1].commit()
                cursor[1].close()
                print(f"Record ID {cursor[0].lastrowid} successfully inserted. Password {passwd}", )

            else:
                print(f'User {payload["username"]} already exists.')
                return {'msg': f'User {payload["username"]} already exists.'}

        except pymysql.err.InternalError:
            cursor[1].rollback()
            cursor[1].close()
            print('Failed to insert the record.')
            return {'erro': 'Failed to insert the record.'}

    @staticmethod
    def select_users(database, payload):

        cursor = connection_db(database)
        if cursor[1] == 401:
            print(cursor[0])
            return cursor[0]

        try:
            sql = f"select * from {payload['name_table']} where username='{payload['username']}'"
            cursor[0].execute(sql)
            lines = cursor[0].fetchall()
            cursor[0].close()
            print(lines)
            return lines

        except pymysql.err.InternalError:
            print('Data recovery failed.')
            return {'erro': 'Data recovery failed.'}

    @staticmethod
    def delete_user(database, username):

        cursor = connection_db(database)
        if cursor[1] == 401:
            print(cursor[0])
            return cursor[0]

        try:
            sql = f"select * from users where username='{username}'"
            user_exists = cursor[0].execute(sql)

            if user_exists:

                sql = f"delete from users where username='{username}'"

                cursor[0].execute(sql)
                cursor[1].commit()
                cursor[1].close()
                print(f"User {username} successfully deleted.")

            else:
                print(f'User {username} not found.')
                return {'msg': f'User {username} not found.'}

        except pymysql.err.InternalError:
            cursor[1].rollback()
            cursor[1].close()
            print('Failed to insert the record.')
            return {'erro': 'Failed to insert the record.'}
