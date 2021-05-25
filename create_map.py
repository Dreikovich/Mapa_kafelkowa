import numpy as np
import random
from PIL import Image, ImageDraw


def generate_value(height, width):
    random_kafelek_x = random.randint(0, height-1)
    random_kafelek_y = random.randint(0, width-1)
    return random_kafelek_x, random_kafelek_y

#  height = row = y
#  width = column = x


def czy_krotka_sprawdzona(sprawdzana_kratka):
    # sprawdzenie czy krotka już sprawdzała sie
    if sprawdzana_kratka[0]-1 >= 0:
        if mapa_kafelkow[sprawdzana_kratka[0]-1][sprawdzana_kratka[1]] == 0:
            return False
    if sprawdzana_kratka[0] < height-1:
        if mapa_kafelkow[sprawdzana_kratka[0]+1][sprawdzana_kratka[1]] == 0:
            return False
    if sprawdzana_kratka[1] - 1 >= 0:
        if mapa_kafelkow[sprawdzana_kratka[0]][sprawdzana_kratka[1]-1] == 0:
            return False
    if sprawdzana_kratka[1] < width-1:
        if mapa_kafelkow[sprawdzana_kratka[0]][sprawdzana_kratka[1]+1] == 0:
            return False
    return True


def usun():
    for sprawdzana_kratka in array_of_1:
        czy_krotka_sprawdzona(sprawdzana_kratka)
        array_of_1.remove(sprawdzana_kratka)


def get_mapa_kafelkow():
    # generowanie macierzy zerowej rozmiaru height X width
    mapa_kafelkow = np.zeros((height, width), dtype=int)
    return mapa_kafelkow


def create(y, x):
    global array_of_1
    mapa_kafelkow[y][x] = 1
    array_of_1 = [(y, x)]
    for i in range(200):
        moja_wybrana = random.choice(array_of_1)
        tymczasowa_lista = []
        # sprawdzenie czy wartosc nie przekracza granicy wierszow
        if moja_wybrana[0]-1 >= 0:
            tymczasowa_lista.append((moja_wybrana[0]-1, moja_wybrana[1]))
        if moja_wybrana[0] < height-1:
            tymczasowa_lista.append((moja_wybrana[0]+1, moja_wybrana[1]))
        # sprawdzenie czy wartosc nie przekracza granicy kolumn
        if moja_wybrana[1] - 1 >= 0:
            tymczasowa_lista.append((moja_wybrana[0], moja_wybrana[1]-1))
        if moja_wybrana[1] < width-1:
            tymczasowa_lista.append((moja_wybrana[0], moja_wybrana[1]+1))
        # zapisuje sie lisowy kafelek i oznacz sie jako jedynka 
        losowy_kafelek = random.choice(tymczasowa_lista)
        mapa_kafelkow[losowy_kafelek] = 1
        array_of_1.append(losowy_kafelek)
        usun()
    return mapa_kafelkow


def create_map(entry_h, entry_w, entry_l):
    global height
    global width
    global mapa_kafelkow
    height = entry_h
    width = entry_w
    liczba_wysp = entry_l
    mapa_kafelkow = get_mapa_kafelkow()
    for i in range(liczba_wysp):
        x = create(y=generate_value(height, width)[0], x=generate_value(height, width)[1])  
    size_of_kafalek = 15
    # domnażamy na size_of_kafełek żeby odrysować kafelki i czarnu kontur
    height1 = height * size_of_kafalek
    width1 = width * size_of_kafalek
    img = Image.new("RGB", (width1, height1))
    draw = ImageDraw.Draw(img)
    # rysowanie kafelek i colorowanie w zależności od warosci w macierzy(0 - \
    # blue, pozostałe(1) - green)
    for y in range(height):
        for x in range(width):
            rog_1 = (x*size_of_kafalek, y*size_of_kafalek)
            rog_2 = ((x+1)*size_of_kafalek, (y+1)*size_of_kafalek)
            if mapa_kafelkow[y][x] == 0:
                color = (0, 0, 256)
            else:
                color = (0, 256, 0)
            draw.rectangle([rog_1, rog_2], fill=color)
    idx = 0
    # rysowanie czarnych linii, kontur kafełka
    while idx < height1:
        draw.line([0, idx, width1, idx], fill=(0, 0, 0))
        idx += size_of_kafalek
    idx2 = 0
    while idx2 < width1:
        draw.line([idx2, 0, idx2, height1], fill=(0, 0, 0))
        idx2 += size_of_kafalek
    # img.show()
    img.save("output.png")
