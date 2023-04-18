#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat April  8 09:05:11 2022
@author: joshua ik
"""
import argparse
import MySQLdb

parser = argparse.ArgumentParser(description='Retrieve states whose names begin with N from a MySQL database.')
parser.add_argument('username', type=str, help='the username to connect to the database')
parser.add_argument('password', type=str, help='the password to connect to the database')
parser.add_argument('database', type=str, help='the name of the database to connect to')
args = parser.parse_args()

with MySQLdb.connect(host='localhost', user=args.username, passwd=args.password, db=args.database, port=3306) as conn:
    with conn.cursor() as cursor:
        num_rows = cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

