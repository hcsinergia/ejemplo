#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyodbc

#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=CNU93230JV\SQLEXPRESS;DATABASE=DFC;UID=sa;PWD=123456;')
#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=CNU93230JV\SQLEXPRESS;DATABASE=DFC;Trusted_Connection=yes;')
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=CNU93230JV\SQLEXPRESS;DATABASE=DFC;TDS_Version=8.0;Port=1433;Trusted_Connection=yes;')


cursor = cnxn.cursor()
#cursor.execute("SELECT apellido, nombre1 FROM agente")
cursor.execute("SELECT * FROM agente")
rows = cursor.fetchall()
for row in rows:
    print row.apellido, row.nombre1, row.legajo