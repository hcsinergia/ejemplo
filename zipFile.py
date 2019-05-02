#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Programa para empaquetar achivos en zip
#HC Sinergia S.A.
#Cristián R. Olmos 2013-05-16
#cristian.olmos@hcsinergia.com

import zipfile 

locfile = "/opt/archivo.txt"
loczip =  (locfile) + ".zip"
print loczip
zip = zipfile.ZipFile (loczip, "w")
zip.write (locfile)
zip.close()
