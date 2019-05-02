#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sudo aptitude install unixodbc unixodbc-dev freetds-dev tdsodbc python-dev

import pyodbc

#cnxn = pyodbc.connect('DRIVER={FreeTDS};SERVER=192.168.0.24\SQLEXPRESS;DATABASE=DFC;UID=sa;PWD=123456;')

#Esta conex está OK
#cnxn = pyodbc.connect('DRIVER={FreeTDS};Server=10.25.49.117\gdtbase;Database=DFC;UID=ARBA\cristian.olmos;PWD=hermes2;TDS_Version=8.0;Port=1433;')
#cnxn = pyodbc.connect('DRIVER={FreeTDS};Server=10.25.49.117\gdtbase;Database=DFC;UID=sa;PWD=123456;TDS_Version=8.0;Port=1433;')

cnxn = pyodbc.connect('DRIVER={FreeTDS};Server=cachorra\gestion;Database=operativos;UID=ARBA\cristian.olmos;PWD=hermes2;TDS_Version=8.0;Port=1433;')

#
#cnxn = pyodbc.connect('DRIVER={FreeTDS};cachorra\gestion;Database=operativos;TDS_Version=8.0;Port=1433;Trusted_Connection=yes;')




cursor = cnxn.cursor()
#cursor.execute("SELECT apellido, nombre1 FROM agente")
cursor.execute("SELECT * FROM gdtip")
rows = cursor.fetchall()
for row in rows:
    print row.partido, row.partida
    
    
