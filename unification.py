from os import remove
import numpy as np
from PIL import Image
import os


class Unification:
    def __init__(self, path_picture_one, path_picture_two):
        self.picture1 = Image.open(path_picture_one)
        self.picture1_name = os.path.splitext(os.path.basename(path_picture_one))[0]
        self.picture2 = Image.open(path_picture_two)
        self.picture2_name = os.path.splitext(os.path.basename(path_picture_two))[0]

    def unificationGeometric(self):

        width1 = self.picture1.width
        width2 = self.picture2.width

        if (width1 > width2):
            max_width = width1
        else:
            max_width = width2

        height1 = self.picture1.height
        height2 = self.picture2.height

        if (height1 > height2):
            max_height = height1
        else:
            max_height = height2
        #Współrzędne dla zdjęcia nr 1
        poczatek_width = int(round((max_width - width1) / 2))
        poczatek_height = int(round((max_height - height1) / 2))

        # Alokacja pamięci:
        result1 = np.empty((max_height, max_width), dtype=np.uint8)
        result2 = np.empty((max_height, max_width), dtype=np.uint8)

        # wypełnienie czarnym:

        for i in range(0, max_height):
            for k in range(0, max_width):
                result1[i, k] = 1

        # sprawdzenie ilości kanałów dla gray:
        array_picture_1 = np.array(self.picture1)
        array_picture_2 = np.array(self.picture2)

        if array_picture_1.shape.__len__() == 3:
            array_picture_1 = array_picture_1[:, :, 0]

        if array_picture_2.shape.__len__() == 3:
            array_picture_2 = array_picture_2[:, :, 0]


        # narysowanie zdjęcia:
        for i in range(0, height1):
            for k in range(0, width1):
                result1[i + poczatek_height, k + poczatek_width] = array_picture_1[i, k]

        # współrzędne początku rysowania zdjęcia 1:
        poczatek_width = int(round((max_width - width2) / 2))
        poczatek_height = int(round((max_height - height2) / 2))

        # wypełnienie czarnym:
        for i in range(0, max_height):
            for k in range(0, max_width):
                result2[i, k] = 1
        #narysuj
        for i in range(0, height2):
            for k in range(0, width2):
                result2[i + poczatek_height, k + poczatek_width] = array_picture_2[i, k]

        self.show_picture(Image.fromarray(result1, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(result2, "L"), self.picture2_name)
        self.save_picture(result1, self.picture1_name, "unification_geometric")
        self.save_picture(result2, self.picture2_name, "unification_geometric")

    def unificationRozdzielczosciowe(self):

        width1 = self.picture1.width
        width2 = self.picture2.width

        height1 = self.picture1.height
        height2 = self.picture2.height

        # alokacja pamięci
        result1 = np.zeros((height1, width1), dtype=np.uint8)
        result2 = np.zeros((height1, width1), dtype=np.uint8)

        # Sprawdzenie ilości kanałów:
        array_picture_1 = np.array(self.picture1)
        array_picture_2 = np.array(self.picture2)

        if array_picture_1.shape.__len__() == 3:
            array_picture_1 = array_picture_1[:, :, 0]

        if array_picture_2.shape.__len__() == 3:
            array_picture_2 = array_picture_2[:, :, 0]

        for i in range(height1):
            for k in range(width1):
                result1[i, k] = array_picture_1[i, k]

        podzial_widthi = width1 / width2
        podzial_heighti = height1 / height2

        #  Czarnym:
        ilosc = 0
        for i in range(height2):
            for k in range(width2):
                if (ilosc == 0):
                    result2[int(podzial_heighti * i), int(round(podzial_widthi * k)) + 1] = array_picture_2[i, k]
                    ilosc += 1
                if (ilosc == 1):
                    result2[int(round(podzial_heighti * i)) + 1, int(podzial_widthi * k)] = array_picture_2[i, k]
                    ilosc = 0

        temp = np.zeros((height1, width1), dtype=np.uint8)

        # interpolacja 
        for i in range(height1):
            for k in range(width1):
                x = 0
                wartosc = 0
                temp[i, k] = result2[i, k]
                if (result2[i, k] < 1):
                    for odstep_i in range(-1, 2):
                        for odstep_k in range(-1, 2):
                            if ((i + odstep_i) > (height1 - 2)) | ((i + odstep_i) < 0):
                                wypelnienie_i = i
                            else:
                                wypelnienie_i = (i + odstep_i)

                            if ((k + odstep_k) > (width1 - 2)) | ((k + odstep_k) < 0):
                                wypelnienie_k = k
                            else:
                                wypelnienie_k = (k + odstep_k)

                            if result2[wypelnienie_i, wypelnienie_k] > 0:
                                wartosc += result2[wypelnienie_i, wypelnienie_k]
                                x += 1

                    temp[i, k] = wartosc / x
                    result2[i, k] = temp[i, k]

        self.show_picture(Image.fromarray(result1, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(result2, "L"), self.picture2_name)
        self.save_picture(result1, self.picture1_name, "unification_distributiveness")
        self.save_picture(result2, self.picture2_name, "unification_distributiveness")

    def unificationGeometricRGB(self):

        width1 = self.picture1.width
        width2 = self.picture2.width

        if (width1 > width2):
            max_width = width1
        else:
            max_width = width2

        height1 = self.picture1.height
        height2 = self.picture2.height

        if (height1 > height2):
            max_height = height1
        else:
            max_height = height2

        result1 = np.empty((max_height, max_width, 3), dtype=np.uint8)
        result2 = np.empty((max_height, max_width, 3), dtype=np.uint8)

        poczatek_width = int(round((max_width - width1) / 2))
        poczatek_height = int(round((max_height - height1) / 2))

        array_picture1 = np.array(self.picture1)
        array_picture2 = np.array(self.picture2)

        # 3 kanały
        array_picture1 = array_picture1[..., :3]
        array_picture2 = array_picture2[..., :3]

        # wypełnienie białym
        for i in range(0, max_height):
            for k in range(0, max_width):
                result1[i, k] = (1, 1, 1)

        for i in range(0, height1):
            for k in range(0, width1):
                result1[i + poczatek_height, k + poczatek_width] = array_picture1[i, k]

        # współrzędne początku zdjęcia 1:
        poczatek_width = int(round((max_width - width2) / 2))
        poczatek_height = int(round((max_height - height2) / 2))

        # Białym kolorem:
        for i in range(0, max_height):
            for k in range(0, max_width):
                result2[i, k] = (1, 1, 1)

        for i in range(0, height2):
            for k in range(0, width2):
                result2[i + poczatek_height, k + poczatek_width] = array_picture2[i, k]

        self.show_picture(Image.fromarray(result1, "RGB"), self.picture1_name)
        self.show_picture(Image.fromarray(result2, "RGB"), self.picture2_name)
        self.save_picture(result1, self.picture1_name, "unification_geometric_rgb")
        self.save_picture(result2, self.picture2_name, "unification_geometric_rgb")

    def unificationRozdzielczoscioweRgb(self):

        width1 = self.picture1.width
        width2 = self.picture2.width

        height1 = self.picture1.height
        height2 = self.picture2.height

        slpitwidth = width1 / width2
        slpitheight = height1 / height2

        array_picture1 = np.array(self.picture1)
        array_picture2 = np.array(self.picture2)

        array_picture1 = array_picture1[..., :3]
        array_picture2 = array_picture2[..., :3]

        # alokacja pamięci
        result1 = np.zeros((height1, width1, 3), dtype=np.uint8)
        result2 = np.zeros((height1, width1, 3), dtype=np.uint8)

        temporary = np.zeros((height1, width1, 3), dtype=np.uint8)

        for i in range(height1):
            for k in range(width1):
                result1[i, k] = array_picture1[i, k]


        ilosc = 0
        for i in range(height2):
            for k in range(width2):
                if ilosc == 0:
                    result2[int(slpitheight * i), int(round(slpitwidth * k)) + 1] = array_picture2[i, k]
                    ilosc += 1
                if ilosc == 1:
                    result2[int(round(slpitheight * i)) + 1, int(slpitwidth * k)] = array_picture2[i, k]
                    ilosc = 0

        # Interpolacja:
        for i in range(height1):
            for k in range(width1):
                x = 0
                r, g, b = 0, 0, 0

                temporary[i, k] = result2[i, k]
                if (result2[i, k][0] < 1) & (result2[i, k][1] < 1) & (result2[i, k][2] < 1):
                    for opuszczone_i in range(-1, 2):
                        for opuszczone_j in range(-1, 2):
                            wypelnienie_i = i if ((i + opuszczone_i) > (height1 - 2)) | ((i + opuszczone_i) < 0) else (i + opuszczone_i)
                            wypelnienie_j = k if ((k + opuszczone_j) > (width1 - 2)) | ((k + opuszczone_j) < 0) else (k + opuszczone_j)
                            if (result2[wypelnienie_i, wypelnienie_j][0] > 0) | (result2[wypelnienie_i, wypelnienie_j][1] > 0) | (
                                    result2[wypelnienie_i, wypelnienie_j][2] > 0):
                                r += result2[wypelnienie_i, wypelnienie_j][0]
                                g += result2[wypelnienie_i, wypelnienie_j][1]
                                b += result2[wypelnienie_i, wypelnienie_j][2]
                                x += 1
                    temporary[i, k] = (r / x, g / x, b / x)
                    result2[i, k] = temporary[i, k]
                    

        self.show_picture(Image.fromarray(result1, "RGB"), self.picture1_name)
        self.show_picture(Image.fromarray(result2, "RGB"), self.picture2_name)
        self.save_picture(result1, self.picture1_name, "unification_distributiveness_rgb")
        self.save_picture(result2, self.picture2_name, "unification_distributiveness_rgb")




    def save_picture(self, picture, name, zadanie):
        path = "solutions/task_1/" + name + "_" + zadanie + ".bmp"
        Image.fromarray(picture).save(path)
        path = "solutions/task_1/" + name + "_" + zadanie + ".png"

        Image.fromarray(picture).save(path)

    # Pokaż:
    def show_picture(self, picture, name_pliku):
        picture.save("temporary.png")
        picture.show()
        remove("temporary.png")