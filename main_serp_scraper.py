import os

from search_result_scraper import Scraper

os.system('color 2f')

def mainSerpScraper(directorio, captcha, keyword, maxPaginas):
    scraper = Scraper(directorio)
    scraper.initDriver(False)
    scraper.scrapear(keyword, captcha, maxPaginas)
    scraper.endDriver()

if __name__ == "__main__":
    print('\n**************    SCRIPT DESARROLLADO POR PATXI JUARISTI PAGEGI [juaristech.com]    **************\n')
    while True:
        fichero = input('----------\n[1] Introduce la carpeta para guardar el resultado. Introduce un punto (.) para la carpeta actual: ')
        if(os.path.isdir(fichero) == False):
            print("----------\n** Error ** That is not a valid folder. Enter a valid folder\n")
            continue
        else:
            caracter = fichero[len(fichero)-1]
            if(caracter != '/' or caracter != '\\'):
                fichero = fichero.replace('/','\\')+'\\'
            break
    
    while True:
        captcha = input('----------\n[2] Captcha si o no (Introduce Y o N): ')
        captcha = captcha.upper()
        if(captcha != 'Y' and captcha != 'N'):
            print("----------\n** Error ** Tienes que introducir una Y o una N solo. Y = Si / N = No\n")
            continue
        else:
            break
    
    while True:
        maxPag = input('----------\n[3] Máximo de paginas de resultados de Google a analizar: ')
        if(maxPag.isnumeric() == False):
            print("----------\n** Error ** Tienes que introducir un valor numérico\n")
            continue
        else:
            break
    
    keyword = input('----------\n[4] Introduce tu keyword o footprint para buscar: ')
    
    captchaSiNo = False
    if(captcha == 'Y'):
        captchaSiNo = True
    
    mainSerpScraper(fichero, captchaSiNo, keyword, int(maxPag))