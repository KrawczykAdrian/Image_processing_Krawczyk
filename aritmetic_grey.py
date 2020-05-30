
from PIL import Image
import numpy as np
import math
import os
from os import remove


class Aritmetic_grey:
    def __init__(self, path_picture_one, path_picture_two):
        self.picture1 = Image.open(path_picture_one)
        self.picture1_name = os.path.splitext(os.path.basename(path_picture_one))[0]
        self.picture2 = Image.open(path_picture_two)
        self.picture2_name = os.path.splitext(os.path.basename(path_picture_two))[0]

    def const_sum(self, const):
        picture = self.picture1
        width = picture.width
        height = picture.height

        result = np.zeros((width, height), dtype=np.uint8)

        x = 0
        f_min = 255
        f_max = 0
        q_max = 0
        d_max = 0

        picture = np.array(picture)

        if picture.shape.__len__() == 3:
            picture = picture[:, :, 0]

        for y in range(height):
            for k in range(width):
                L = int(picture[k][y]) + int(const)

                if q_max < L:
                    q_max = L

        if q_max > 255:
            d_max = q_max - 255
            x = (d_max / 255)

        for y in range(height):
            for k in range(width):
                L = (picture[k][y] - (picture[k][y] * x)) + (const - (const * x))

                result[k][y] = math.ceil(L)

                if f_min > L:
                    f_min = L
                if f_max < L:
                    f_max = L

        normalization_array = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for k in range(width):
                normalization_array[k][y] = 255 * ((result[k][y] - f_min) / (f_max - f_min))


        self.show_picture(Image.fromarray(picture, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(result, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(normalization_array, "L"), self.picture1_name)

        self.save_picture(picture, self.picture1_name, "suming_with_const")
        self.save_picture(result, self.picture1_name, "suming_const_result")
        self.save_picture(normalization_array, self.picture1_name, "suming_const_normalization")

    def summing_two_pictures(self):

        picture1 = self.picture1
        picture2 = self.picture2
        height = picture1.height
        width = picture1.width

        result = np.zeros((width, height), dtype=np.uint8)

        q_max= 0
        d_max= 0
        X = 0
        f_min= 255
        f_max= 0

        array_picture1 = np.array(picture1)
        array_picture2 = np.array(picture2)

        # Ustawienie kanałów dla szarego zdjęcia:
        if array_picture1.shape.__len__() == 3:
            array_picture1 = array_picture1[:, :, 0]

        if array_picture2.shape.__len__() == 3:
            array_picture2 = array_picture2[:, :, 0]

        for y in range(height):
            for x in range(width):

                L = int(array_picture1[x][y]) + int(array_picture2[x][y])

                if q_max< L:
                    q_max= L

        if q_max> 255:
            d_max= q_max- 255
            X = (d_max/ 255)

        for y in range(height):
            for x in range(width):
                L = (array_picture1[x][y] - (array_picture1[x][y] * X)) + (
                        array_picture2[x][y] - (array_picture2[x][y] * X))

                result[x][y] = math.ceil(L)

                # Min i maks:
                if f_min> L:
                    f_min= L
                if f_max< L:
                    f_max= L

        # Normalizacja:
        normalization_array = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                normalization_array[x][y] = 255 * ((result[x][y] - f_min) / (f_max- f_min))

        self.show_picture(Image.fromarray(array_picture1, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(array_picture2, "L"), self.picture2_name)
        self.show_picture(Image.fromarray(result, "L"), self.picture1_name + "summing_gray_result")
        self.show_picture(Image.fromarray(normalization_array, "L"), self.picture2_name + "Summing_grey_with_normalization")

        self.save_picture(array_picture1, self.picture1_name, "summing_two_pictures")
        self.save_picture(array_picture2, self.picture2_name, "summing_two_pictures")
        self.save_picture(result, self.picture1_name, "summing_gray_result")
        self.save_picture(normalization_array, self.picture1_name, "Summing_grey_with_normalization")

    def multiplication_by_const(self, const):

        picture = self.picture1
        height = picture.height
        width = picture.width

        result_array = np.zeros((width, height), dtype=np.uint8)

        array_picture = np.array(picture)

        # Dostosowanie kanałów:
        if array_picture.shape.__len__() == 3:
            array_picture = array_picture[:, :, 0]

        min = 255
        max = 0

        for i in range(height):
            for k in range(width):

                temporary = int(array_picture[k][i])
                if temporary == 255:
                    temporary = const
                elif temporary == 0:
                    temporary = 0
                else:
                    temporary = (int(array_picture[k][i]) * const) / 255

                result_array[k][i] = math.ceil(temporary)

                # Min i max:
                if min > temporary:
                    min = temporary
                if max < temporary:
                    max = temporary

        # Normalizowanie
        array_after_norm = np.zeros((width, height), dtype=np.uint8)

        # Rzutowanie na zmienną int
        min = int(min)
        max = int(max)

        for i in range(height):
            for k in range(width):
                array_after_norm[k][i] = 255 * ((result_array[k][i] - min) / (max - min))

        self.show_picture(Image.fromarray(array_picture, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(result_array, "L"), self.picture1_name)
        self .show_picture(Image.fromarray(array_after_norm, "L"), self.picture1_name)

        self.save_picture(array_picture, self.picture1_name, "multiple_via_const_original_Image")
        self.save_picture(result_array, self.picture1_name, "multiple_via_const_original_Image_gray_result")
        self.save_picture(array_after_norm, self.picture1_name, "multiple_via_const_original_Image_gray_result_normalizaction")

    def multiplication_by_picture(self):

        picture1 = self.picture1
        picture2 = self.picture2
        height = picture1.height
        width = picture1.width

        array_picture1 = np.array(picture1)
        array_picture2 = np.array(picture2)

        # Dostosowanie kanałów:
        if array_picture1.shape.__len__() == 3:
            array_picture1 = array_picture1[:, :, 0]

        # Dostosowanie kanałów:
        if array_picture2.shape.__len__() == 3:
                array_picture2 = array_picture2[:, :, 0]

        f_min = 255
        f_max = 0
        result = np.zeros((width, height), dtype=np.uint8)

        for y in range(height):
            for k in range(width):

                L = int(array_picture1[k][y])
                if L == 255:
                    L = array_picture2[k][y]
                elif L == 0:
                    L = 0
                else:
                    L = (int(array_picture1[k][y]) * int(array_picture2[k][y])) / 255

                result[k][y] = math.ceil(L)

                # Min i max:
                if f_min > L:
                    f_min = L
                if f_max < L:
                    f_max = L

        array_after_norm = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for k in range(width):
                array_after_norm[k][y] = 255 * ((result[k][y] - f_min) / (f_max - f_min))

        self.show_picture(Image.fromarray(array_picture1, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(array_picture2, "L"), self.picture2_name)
        self.show_picture(Image.fromarray(result, "L"), "result_multiple_by_another_image")
        self.show_picture(Image.fromarray(array_after_norm, "L"), "result_multiple_by_another_image_after_normalization")

        self.save_picture(array_picture1, self.picture1_name, "oryginal")
        self.save_picture(array_picture2, self.picture2_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "result_multiple_by_another_image")

        self.save_picture(array_after_norm, self.picture1_name,
                    "result_multiple_by_another_image_after_Normalization")


    def mixing_pictures(self, ratio):

        picture1 = self.picture1
        picture2 = self.picture2
        height = picture1.height
        width = picture1.width

        result = np.zeros((width, height), dtype=np.uint8)

        f_min = 255
        f_max = 0

        array_picture1 = np.array(picture1)
        array_picture2 = np.array(picture2)

        #Dostosowanie kanałów:
        if array_picture1.shape.__len__() == 3:
            array_picture1 = array_picture1[:, :, 0]

        #Dostosowanie kanałów:
        if array_picture2.shape.__len__() == 3:
            array_picture2 = array_picture2[:, :, 0]

        for y in range(height):
            for k in range(width):

                L = float(array_picture1[k][y]) * ratio + (1 - ratio) * float(array_picture2[k][y])

                result[k][y] = math.ceil(L)

                # Min i max:
                if f_min > L:
                    f_min = L
                if f_max < L:
                    f_max = L

        array_after_norm = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for k in range(width):
                array_after_norm[k][y] = 255 * ((result[k][y] - f_min) / (f_max - f_min))

        self.show_picture(Image.fromarray(array_picture1, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(array_picture2, "L"), self.picture2_name)
        self.show_picture(Image.fromarray(result, "L"), "result mixing Img")
        self.show_picture(Image.fromarray(array_after_norm, "L"), "result_mixing_with_normalization")

        self.save_picture(array_picture1, self.picture1_name, "oryginal")
        self.save_picture(array_picture2, self.picture2_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "mixing img - result")

        self.save_picture(array_after_norm, self.picture1_name,
                    "mixing img - result with_normalization")


    def exponentiation_picture(self, ratio):

        picture = self.picture1
        height = picture.height
        width = picture.width

        result = np.zeros((width, height), dtype=np.uint8)

        array_picture = np.array(picture)

        #Dostosowanie kanałów:
        if array_picture.shape.__len__() == 3:
            array_picture = array_picture[:, :, 0]

        f_min = 255
        f_max = 0
        f_picture_max = 0

        for y in range(height):
            for k in range(width):
                temporary = int(array_picture[k][y])

                if f_picture_max < temporary:
                    f_picture_max = temporary

        for y in range(height):
            for k in range(width):

                temporary = int(array_picture[k][y])
                if temporary == 255:
                    temporary = 255
                elif temporary == 0:
                    temporary = 0
                else:
                    temporary = math.pow(int(array_picture[k][y]) / f_picture_max, ratio) * 255

                result[k][y] = math.ceil(temporary)

                # Min i max:
                if f_min > temporary:
                    f_min = temporary
                if f_max < temporary:
                    f_max = temporary

        array_after_norm = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for k in range(width):
                array_after_norm[k][y] = 255 * ((result[k][y] - f_min) / (f_max - f_min))

        self.show_picture(Image.fromarray(array_picture, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(result, "L"), "result exponentiation Img")
        self.show_picture(Image.fromarray(array_after_norm, "L"), "result exponentiation Img with_normalization")
        self.save_picture(array_picture, self.picture1_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "result exponentiation Img")
        self.save_picture(array_after_norm, self.picture1_name,
                    "result exponentiation Img with_normalization")


    def division_by_const(self, const):

        picture = self.picture1
        height = picture.height
        width = picture.width

        f_min = 255
        f_max = 0
        q_max = 0

        result = np.zeros((width, height), dtype=np.uint8)

        array_picture = np.array(picture)

        #Dostosowanie kanałów:
        if array_picture.shape.__len__() == 3:
            array_picture = array_picture[:, :, 0]

        for y in range(height):
            for k in range(width):

                L = int(array_picture[k][y]) + int(const)

                if q_max < L:
                    q_max = L

        for y in range(height):
            for k in range(width):

                L = int(array_picture[k][y]) + int(const)
                Q_L = (L * 255) / q_max

                result[k][y] = math.ceil(Q_L)

                # Min i max:
                if f_min > Q_L:
                    f_min = Q_L
                if f_max < Q_L:
                    f_max = Q_L

        array_after_norm = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for k in range(width):
                array_after_norm[k][y] = 255 * ((result[k][y] - f_min) / (f_max - f_min))

        self.show_picture(Image.fromarray(array_picture, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(result, "L"), "result_divide_const_const")
        self.show_picture(Image.fromarray(array_after_norm, "L"), "result_divide_const_with_normalization")

        self.save_picture(array_picture, self.picture1_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "result_divide_const_const")
        self.save_picture(array_after_norm, self.picture1_name,
                    "result_divide_const_const with_normalization")

    def division_by_picture(self):

        picture1 = self.picture1
        picture2 = self.picture2
        height = picture1.height
        width = picture1.width

        result = np.zeros((width, height), dtype=np.uint8)

        f_min = 255
        f_max = 0
        q_max = 0

        array_picture1 = np.array(picture1)
        array_picture2 = np.array(picture2)

        #Dostosowanie kanałów:
        if array_picture1.shape.__len__() == 3:
            array_picture1 = array_picture1[:, :, 0]

        if array_picture2.shape.__len__() == 3:
            array_picture2 = array_picture2[:, :, 0]

        for y in range(height):
            for k in range(width):
                gray = int(array_picture1[k][y]) + int(array_picture2[k][y])
                if q_max < gray:
                    q_max = gray

        for y in range(height):
            for k in range(width):

                gray = int(array_picture1[k][y]) + int(array_picture2[k][y])
                gray2 = (gray * 255) / q_max
                result[k][y] = math.ceil(gray2)

                # ustawienie minimum i maksimum
                if f_min > gray2:
                    f_min = gray2
                if f_max < gray2:
                    f_max = gray2

        array_after_norm = np.zeros((width, height), dtype=np.uint8)
        for y in range(height):
            for k in range(width):
                array_after_norm[k][y] = 255 * ((result[k][y] - f_min) / (f_max - f_min))

        self.show_picture(Image.fromarray(array_picture1, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(array_picture2, "L"), self.picture2_name)
        self.show_picture(Image.fromarray(result, "L"), "result_divide_picture")
        self.show_picture(Image.fromarray(array_after_norm, "L"), "result_divide_picture with_normalization")

        self.save_picture(array_picture1, self.picture1_name, "oryginal")
        self.save_picture(array_picture2, self.picture2_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "result_divide_picture")

        self.save_picture(array_after_norm, self.picture1_name,
                    "result_divide_picture with_normalization")


    def roots_picture(self, moc):
        picture = self.picture1
        height = picture.height
        width = picture.width

        f_min = 255
        f_max = 0
        f_picture_max = 0

        result = np.zeros((width, height), dtype=np.uint8)

        array_picture = np.array(picture)

        #Dostosowanie kanałów:
        if array_picture.shape.__len__() == 3:
            array_picture = array_picture[:, :, 0]


        ratio = 1 / moc

        for y in range(height):
            for k in range(width):

                L = int(array_picture[k][y])

                # Poszukiwanie maksimum
                if f_picture_max < L:
                    f_picture_max = L

        for y in range(height):
            for k in range(width):

                L = int(array_picture[k][y])
                if L == 255:
                    L = 255
                elif L == 0:
                    L = 0
                else:
                    L = math.pow(int(array_picture[k][y]) / f_picture_max, ratio) * 255

                result[k][y] = math.ceil(L)

                # Min i max:
                if f_min > L:
                    f_min = L
                if f_max < L:
                    f_max = L

        array_after_norm = np.zeros((width, height), dtype=np.uint8)

        for y in range(height):
            for k in range(width):
                array_after_norm[k][y] = 255 * ((result[k][y] - f_min) / (f_max - f_min))

        self.show_picture(Image.fromarray(array_picture, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(result, "L"), "result rooting_picture")
        self.show_picture(Image.fromarray(array_after_norm, "L"), "result rooting_picture with_normalization")

        self.save_picture(array_picture, self.picture1_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "result rooting_picture")

        self.save_picture(array_after_norm, self.picture1_name,
                    "result rooting_picture with_normalization")


    def logarithm_picture(self):

        picture = self.picture1
        height = picture.height
        width = picture.width

        f_min = 255
        f_max = 0
        f_picture_max = 0

        result = np.empty((width, height), dtype=np.uint8)

        array_picture = np.array(picture)

        # Kanały dla szarego:
        if array_picture.shape.__len__() == 3:
            array_picture = array_picture[:, :, 0]

        for i in range(height):
            for k in range(width):

                gray = int(array_picture[k][i])

                # maksimum
                if f_picture_max < gray:
                    f_picture_max = gray

        for i in range(height):
            for k in range(width):

                gray = int(array_picture[k][i])

                if gray == 0:
                    gray = 0
                else:
                    gray = (math.log(1 + gray) / math.log(1 + f_picture_max)) * 255

                result[k][i] = math.ceil(gray)

                if f_min > gray:
                    f_min = gray
                if f_max < gray:
                    f_max = gray

        array_after_norm = np.zeros((width, height), dtype=np.uint8)
        for i in range(height):
            for k in range(width):
                array_after_norm[k][i] = 255 * ((result[k][i] - f_min) / (f_max - f_min))


        self.show_picture(Image.fromarray(array_picture, "L"), self.picture1_name)
        self.show_picture(Image.fromarray(result, "L"), "result logaritm_by_picture")
        self.show_picture(Image.fromarray(array_after_norm, "L"),
                          "result logaritm_by_picture with_normalization")
        self.save_picture(array_picture, self.picture1_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "result logaritm_picture")
        self.save_picture(array_after_norm, self.picture1_name,
                    "result logaritm_by_picture with_normalization")

    # Zapisz:
    def save_picture(self, picture, name, zadanie):
        path = "solutions/task_2/" + name + "_" + zadanie + ".bmp"
        Image.fromarray(picture).save(path)
        path = "solutions/task_2/" + name + "_" + zadanie + ".png"
        Image.fromarray(picture).save(path)

    # Pokaż:
    def show_picture(self, picture, name_pliku):
        picture.save("temporary.png")
        picture.show()
        remove("temporary.png")