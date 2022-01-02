import sys
import os
from os import listdir, write
from os.path import isfile, join
import csv

def resource_path(relative_path):
    """ To get resources path for creating the .exe with PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def readFolderFiles(rutaFicheros):
    onlyfiles = [f for f in listdir(rutaFicheros) if isfile(join(rutaFicheros, f))]
    return onlyfiles

def convertirKwEnFilename(s):
        replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),(" ","-"),("|",""),(".",""),(":",""),(",",""),("'",""),("´",""),("`",""),("¿",""),("¡",""),("?",""),("!",""),("@",""),("*",""),("/",""),("\\",""),("\"",""),("$",""),("%",""),("&",""),("(",""),(")",""),("ö","o"),("ü","u"),("ä","a"),("ë","e"),("è","e"),("à","a"),("ì","i"),("ù","u"),("ò","o"),("’",""),("ğ","g"),("„",""),("“",""),("ć","c"),("ß","s"),("ş","s"),("--","-"))
        s = s.lower()
        for a, b in replacements:
            s = s.replace(a, b)
        return s

def escribirFichero(rutaFichero, keyword, listaResultados):
    with open(rutaFichero+'/'+convertirKwEnFilename(keyword)+'.txt', 'w', encoding='utf-8') as f:
        for result in listaResultados:
            f.write(result.enlace)
            f.write('\n')

def escribirCsv(rutaFichero, keyword, listaResultados):
    print(convertirKwEnFilename(keyword))
    with open(rutaFichero+'/'+convertirKwEnFilename(keyword)+'.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        encabezado = ['Titulo','Enlace','Meta-Descripcion']
        writer.writerow(encabezado)

        for res in listaResultados:
            writer.writerow(res.getLineaCsv())