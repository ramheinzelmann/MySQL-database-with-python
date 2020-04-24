#!/usr/bin/python
# coding: utf8
"""
Date: 19/06/2018
Autor: Renato Machado
Abjective: Make calls to create the table, insert a record in the created table and retrieve the information from
          the table.
Alteration:
"""

from working_db import Execute_Sql


def main():

    """
    Create the users table in the database.
    """
    sql = f"create table {payload['name_table']} " \
          f"(id INT AUTO_INCREMENT PRIMARY KEY, " \
          f"username VARCHAR(100), " \
          f"email VARCHAR(100), " \
          f"password VARCHAR(100))"

    Execute_Sql.create_table(database=payload['database'],
                             table=payload['name_table'],
                             query_sql=sql)

    """
    Insert user in the table.
    """
    Execute_Sql.insert_user(database=payload['database'],
                            payload=payload)

    """
    Retrieves all database users. Optional.
    """
    Execute_Sql.select_users(database=payload['database'],
                             payload=payload)

    """
    Delete a user from the database.
    """
    # Execute_Sql.delete_user(database=payload['database'],
    #                         username=payload['username'])


if __name__ == "__main__":

    """
    Input data. Inserted in the frontend of the application.  
    """
    payload = {
        'database': 'cfg',
        'name_table': 'users',
        'username': 'admin',
        'email': 'admin@admin.com'
    }

    main()
