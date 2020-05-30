from PIL import Image
import numpy as np
import math
import os
from os import remove

class Geometric:
    def __init__(self, path_picture_one, path_picture_two):
        self.picture1 = Image.open(path_picture_one)
        self.picture1_name = os.path.splitext(os.path.basename(path_picture_one))[0]
        self.picture2 = Image.open(path_picture_two)
        self.picture2_name = os.path.splitext(os.path.basename(path_picture_two))[0]



    def movement(self, wektor_x, wektor_y):
        picture = self.picture1
        width = picture.width
        height = picture.height

        array_picture = np.array(picture)

        if(array_picture.shape[2] == 4):

            array_picture = array_picture[..., :3]

        wektor_y = 0 - wektor_y

        result = np.zeros((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for k in range(width):
                if 0 < i + wektor_y < height and 0 < k + wektor_x < width:
                    result[i + wektor_y][k + wektor_x] = array_picture[i][k]


        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), self.picture1_name)
        self.save_picture(array_picture, self.picture1_name, "movement")
        self.save_picture(result, self.picture1_name, "result_after_movement")


    def graduation_homogeneous(self, skala):
        picture = self.picture1
        width = picture.width
        height = picture.height

        array_pictureu = np.array(picture)


        if(array_pictureu.shape[2] == 4):
            array_pictureu = array_pictureu[..., :3]
        result = np.zeros((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for k in range(width):
                if skala * i < height and skala * k < width:
                    result[int(skala * i)][int(skala * k)] = array_pictureu[i][k]

        result_pictureu2 = np.copy(result)
        temporary_zmienna = np.ones((height, width, 3), dtype=np.uint8)

        # Interpolacja:
        for i in range(height):
            for j in range(width):
                r, g, b = 0, 0, 0
                n = 1
                temporary_zmienna[i, j] = result_pictureu2[i, j]
                if (result_pictureu2[i, j][0] < 1) & (result_pictureu2[i, j][1] < 1) & (result_pictureu2[i, j][2] < 1):
                    for a in range(-1, 2):
                        for jOff in range(-1, 2):
                            b = i if ((i + a) > (height - 2)) | ((i + a) < 0) else (i + a)
                            c = j if ((j + jOff) > (width - 2)) | ((j + jOff) < 0) else (j + jOff)
                            if (result_pictureu2[b, c][0] > 0) | (result_pictureu2[b, c][1] > 0) | (
                                    result_pictureu2[b, c][2] > 0):
                                r += result_pictureu2[b, c][0]
                                g += result_pictureu2[b, c][1]
                                b += result_pictureu2[b, c][2]
                                n += 1
                    temporary_zmienna[i, j] = (r / n, g / n, b / n)
                    result_pictureu2[i, j] = temporary_zmienna[i, j]

        Image._show(self.picture1)
        # po skalowaniu
        self.show_picture(Image.fromarray(result, "RGB"), self.picture1_name)
        # interpolacja
        self.show_picture(Image.fromarray(result_pictureu2, "RGB"), self.picture1_name)
        self.save_picture(array_pictureu, self.picture1_name, "graduation_homogeneous")
        self.save_picture(result, self.picture1_name, "graduation_homogeneous_result")
        self.save_picture(result_pictureu2, self.picture1_name, "graduation_homogeneous_interpolation")


    def graduation_non_homogeneous(self, wektor_x, wektor_y):

        picture = self.picture1
        width = picture.width
        height = picture.height

        # Alokacja pamieci
        result = np.zeros((height, width, 3), dtype=np.uint8)

        array_picture = np.array(picture)

        if(array_picture.shape[2] == 4):
            array_picture = array_picture[..., :3]

        for i in range(height):
            for k in range(width):
                if wektor_y * i < height and wektor_x * k < width:
                    result[int(wektor_y * i)][int(wektor_x * k)] = array_picture[i][k]

        result2 = np.copy(result)
        temporary_zmienna = np.ones((height, width, 3), dtype=np.uint8)

        # Interpolacja
        for i in range(height):
            for j in range(width):
                r, g, b = 0, 0, 0
                n = 1
                temporary_zmienna[i, j] = result2[i, j]
                if (result2[i, j][0] < 1) & (result2[i, j][1] < 1) & (result2[i, j][2] < 1):
                    for a in range(-1, 2):
                        for b in range(-1, 2):
                            a_zmienna = i if ((i + a) > (height - 2)) | ((i + a) < 0) else (i + a)
                            b_zmienna = j if ((j + b) > (width - 2)) | ((j + b) < 0) else (j + b)
                            if (result2[a_zmienna, b_zmienna][0] > 0) | (result2[a_zmienna, b_zmienna][1] > 0) | (
                                    result2[a_zmienna, b_zmienna][2] > 0):
                                r += result2[a_zmienna, b_zmienna][0]
                                g += result2[a_zmienna, b_zmienna][1]
                                b += result2[a_zmienna, b_zmienna][2]
                                n += 1
                    temporary_zmienna[i, j] = (r / n, g / n, b / n)
                    result2[i, j] = temporary_zmienna[i, j]

        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), self.picture1_name)
        self.show_picture(Image.fromarray(result2, "RGB"), self.picture1_name)
        self.save_picture(array_picture, self.picture1_name, "graduation_non_homogeneous")
        self.save_picture(result, self.picture1_name, "graduation_non_homogeneous_result")
        self.save_picture(result2, self.picture1_name, "graduation_non_homogeneous_interpolation")

    def rotating(self, promien=0):

        picture = self.picture1
        width = picture.width
        height = picture.height

        array_picture = np.array(picture)

        if(array_picture.shape[2] == 4):
            array_picture = array_picture[..., :3]

        promien_radiany = math.radians(promien)

        result = np.zeros((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for k in range(width):
                nowy_x = (k - width / 2) * math.cos(promien_radiany) - (i - height / 2) * math.sin(promien_radiany) + (width / 2)
                nowy_y = (k - width / 2) * math.sin(promien_radiany) + (i - height / 2) * math.cos(promien_radiany) + (height / 2)
                if nowy_y < height and nowy_y >= 0 and nowy_x >= 0 and nowy_x < width:
                    result[int(nowy_y)][int(nowy_x)] = array_picture[i][k]

        result2 = np.copy(result)
        temporary = np.ones((height, width, 3), dtype=np.uint8)

        # interpolacja
        for i in range(height):
            for j in range(width):
                r, g, b = 0, 0, 0
                n = 1
                temporary[i, j] = result2[i, j]
                if (result2[i, j][0] < 1) & (result2[i, j][1] < 1) & (result2[i, j][2] < 1):
                    for a in range(-1, 2):
                        for b in range(-1, 2):
                            a_zmienna = i if ((i + a) > (height - 2)) | ((i + a) < 0) else (i + a)
                            b_zmienna = j if ((j + b) > (width - 2)) | ((j + b) < 0) else (j + b)
                            if (result2[a_zmienna, b_zmienna][0] > 0) | (result2[a_zmienna, b_zmienna][1] > 0) | (
                                    result2[a_zmienna, b_zmienna][2] > 0):
                                r += result2[a_zmienna, b_zmienna][0]
                                g += result2[a_zmienna, b_zmienna][1]
                                b += result2[a_zmienna, b_zmienna][2]
                                n += 1
                    temporary[i, j] = (r / n, g / n, b / n)
                    result2[i, j] = temporary[i, j]

        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), self.picture1_name)
        self.show_picture(Image.fromarray(result2, "RGB"), self.picture1_name)

        self.save_picture(array_picture, self.picture1_name, "rotating_homogeneous ")
        self.save_picture(result, self.picture1_name, "rotating_result")
        self.save_picture(result2, self.picture1_name, "rotating_interpolation")

    def symetric_x(self):

        picture = self.picture1
        width = picture.width
        height = picture.height

        result = np.zeros((height, width, 3), dtype=np.uint8)

        array_picture = np.array(picture)

        if(array_picture.shape[2] == 4):
            array_picture = array_picture[..., :3]

        height_zmieniona = height - 1

        for i in range(height):
            for k in range(width):
                result[i][k] = array_picture[height_zmieniona - i][k]

        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), self.picture1_name)
        self.save_picture(array_picture, self.picture1_name, "symetric_x")
        self.save_picture(result, self.picture1_name, "symetric_x_interpolation")

    def symetric_y(self):

        picture = self.picture1
        width = picture.width
        height = picture.height

        array_picture = np.array(picture)


        if(array_picture.shape[2] == 4):
            array_picture = array_picture[..., :3]

        result = np.zeros((height, width, 3), dtype=np.uint8)
        width_zmieniona = width - 1

        for i in range(height):
            for k in range(width):
                result[i][k] = array_picture[i][width_zmieniona - k]


        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), self.picture1_name)

        self.save_picture(array_picture, self.picture1_name, "symetric_y_result")
        self.save_picture(result, self.picture1_name, "symetric_y_interpolation")

    def symetric_parameter_y(self):

        picture = self.picture1
        width = picture.width
        height = picture.height

        result = np.zeros((height, width, 3), dtype=np.uint8)
        array_picture = np.array(picture)

        if(array_picture.shape[2] == 4):
            array_picture = array_picture[..., :3]

        height_zmieniona = height - 1

        parametr_y = height / 2

        for i in range(height):
            for k in range(width):
                if i < parametr_y:
                    result[i][k] = array_picture[i][k]
                else:
                    result[i][k] = array_picture[height_zmieniona - i][k]

        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), self.picture1_name)
        self.save_picture(array_picture, self.picture1_name, "symetric_parameter_y_result")
        self.save_picture(result, self.picture1_name, "symetric_parameter_y_interpolation")

    def symetric_parameter_x(self):
        picture = self.picture1
        width = picture.width
        height = picture.height

        array_picture = np.array(picture)

        if(array_picture.shape[2] == 4):
            array_picture = array_picture[..., :3]

        result = np.zeros((height, width, 3), dtype=np.uint8)
        width_zmieniona = width - 1

        param_x = width / 2

        for y in range(height):
            for x in range(width):
                if x < param_x:
                    result[y][x] = array_picture[y][x]
                else:
                    result[y][x] = array_picture[y][width_zmieniona - x]

        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), self.picture1_name)
        self.save_picture(array_picture, self.picture1_name, "symetric_parameter_x")
        self.save_picture(result, self.picture1_name, "symetric_parameter_x_interpolation")

    def piece_cutting(self, x_min, x_max, y_min, y_max):

        picture = self.picture1
        width = picture.width
        height = picture.height

        array_picture = np.array(picture)

        # 3 kanały:
        if(array_picture.shape[2] == 4):
            array_picture = array_picture[..., :3]

        result = np.zeros((height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                if x > x_min and x < x_max and y < height - y_min and y > height - y_max:
                    result[y][x] = 0
                else:
                    result[y][x] = array_picture[y][x]

        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), self.picture1_name)
        self.save_picture(array_picture, self.picture1_name, "piece_cutting_result")
        self.save_picture(result, self.picture1_name, "piece_cutting_interpolation")

    def duplication(self, x_min, x_max, y_min, y_max):

        picture = self.picture1
        width = picture.width
        height = picture.height

        array_picture = np.array(picture)

        # 3 kanały:
        if(array_picture.shape[2] == 4):
            array_picture = array_picture[..., :3]

        result = np.zeros((height, width, 3), dtype=np.uint8)

        # Alokacja:
        wycieta_array = np.zeros((y_max - y_min + 1, x_max - x_min + 1, 3), dtype=np.uint8)

        wyciete_y = 0
        for y in range(height):
            wyciete_x = 0
            for x in range(width):
                if x >= x_min and x <= x_max and y <= height - y_min and y >= height - y_max:
                    result[y][x] = array_picture[y][x]
                    wycieta_array[wyciete_y][wyciete_x] = array_picture [y][x]
                    wyciete_x += 1
            if wyciete_x > 0:
                wyciete_y += 1

        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), self.picture1_name)
        self.show_picture(Image.fromarray(wycieta_array, "RGB"), self.picture1_name)
        self.save_picture(array_picture, self.picture1_name, "copy fraction")
        self.save_picture(result, self.picture1_name, "copy fraction_result")
        self.save_picture(wycieta_array, self.picture1_name, "copy fraction_interpolation")

    # Zapisz:
    def save_picture(self, picture, name, zadanie):
        path = "solutions/task_4/" + name + "_" + zadanie + ".bmp"
        Image.fromarray(picture).save(path)
        path = "solutions/task_4/" + name + "_" + zadanie + ".png"
        Image.fromarray(picture).save(path)

    # Pokaż:
    def show_picture(self, picture, name_pliku):
        picture.save("temporary.png")
        picture.show()
        remove("temporary.png")