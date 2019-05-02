#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sudo aptitude install unixodbc unixodbc-dev freetds-dev tdsodbc python-dev

import pyodbc

#cnxn = pyodbc.connect('DRIVER={FreeTDS};SERVER=192.168.0.24\SQLEXPRESS;DATABASE=DFC;UID=sa;PWD=123456;')


cnxn = pyodbc.connect('DRIVER={FreeTDS};Server=10.25.49.117\gdtbase;Database=DFC;UID=sa;PWD=123456;TDS_Version=8.0;Port=1433;')

cursor = cnxn.cursor()
cursor.execute("SELECT apellido, nombre1 FROM agente")
rows = cursor.fetchall()
for row in rows:
    print row.apellido, row.nombre1
    
    
