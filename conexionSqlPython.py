#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sudo aptitude install unixodbc unixodbc-dev freetds-dev tdsodbc python-dev

import pyodbc

#cnxn = pyodbc.connect('DRIVER={FreeTDS};SERVER=192.168.0.24\SQLEXPRESS;DATABASE=DFC;UID=sa;PWD=123456;')
cnxn = pyodbc.connect('DRIVER={SQL Server};Server=10.25.48.1\SQLEXPRESS;Database=test;UID=sa;PWD=123456;TDS_Version=8.0;Port=1433;')


#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.25.49.117\gdtbase;DATABASE=DFC;UID=sa;PWD=123456;')


cursor = cnxn.cursor()
cursor.execute("SELECT cuit, nombre1 FROM tabla_test")
rows = cursor.fetchall()
for row in rows:
    print row[0], row[1]
    
