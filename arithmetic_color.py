
from PIL import Image
import numpy as np
import math
import os
from os import remove


class Arithmetic_color:
    def __init__(self, path_picture_one, path_picture_two):
        self.picture1 = Image.open(path_picture_one)
        self.picture1_name = os.path.splitext(os.path.basename(path_picture_one))[0]
        self.picture2 = Image.open(path_picture_two)
        self.picture2_name = os.path.splitext(os.path.basename(path_picture_two))[0]


    def const_sum(self, const):
        picture = self.picture1
        width = picture.width
        height = picture.height

        result = np.empty((width, height, 3), dtype=np.uint8)

        x1 = 0
        f_min = 255
        f_max = 0
        q_max = 0
        d_max = 0

        array_picture = np.array(picture)

        for i in range(height):
            for k in range(width):

                r = int(array_picture[k][i][0]) + int(const)
                g = int(array_picture[k][i][1]) + int(const)
                b = int(array_picture[k][i][2]) + int(const)

                if q_max < max([r, g, b]):
                    q_max = max([r, g, b])

        if q_max > 255:
            d_max = q_max - 255
            x1 = (d_max / 255)

        for i in range(height):
            for k in range(width):
                r = (array_picture[k][i][0] - (array_picture[k][i][0] * x1)) + (const - (const * x1))
                g = (array_picture[k][i][1] - (array_picture[k][i][1] * x1)) + (const - (const * x1))
                b = (array_picture[k][i][2] - (array_picture[k][i][2] * x1)) + (const - (const * x1))

                # Zaokrąglenie
                result[k][i][0] = math.ceil(r)
                result[k][i][1] = math.ceil(g)
                result[k][i][2] = math.ceil(b)

                if f_min > min([r, g, b]):
                    f_min = min([r, g, b])
                if f_max < max([r, g, b]):
                    f_max = max([r, g, b])

        # Normalizacja:
        array_after_normalization = np.zeros((width, height, 3), dtype=np.uint8)
        for i in range(height):
            for k in range(width):
                array_after_normalization[k][i][0] = 255 * (
                        (result[k][i][0] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][1] = 255 * (
                        (result[k][i][1] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][2] = 255 * (
                        (result[k][i][2] - f_min) / (f_max - f_min))


        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), self.picture1_name)
        self.show_picture(Image.fromarray(array_after_normalization, "RGB"), self.picture1_name)

        self.save_picture(array_picture, self.picture1_name, "summing_const")
        self.save_picture(result, self.picture1_name, "summing_const_result")
        self.save_picture(array_after_normalization, self.picture1_name, "summing_const_norm")

    def summing_two_pictures(self):

        picture1 = self.picture1
        picture2 = self.picture2
        height = picture1.height
        width = picture1.width

        array_picture1 = np.array(picture1)
        array_picture2 = np.array(picture2)

        result = np.empty((height, width, 3), dtype=np.uint8)

        x1 = 0
        q_max = 0
        d_max = 0
        f_min = 255
        f_max = 0

        for i in range(height):
            for k in range(width):

                r = int(array_picture1[k][i][0]) + int(array_picture2[k][i][0])
                g = int(array_picture1[k][i][1]) + int(array_picture2[k][i][1])
                b = int(array_picture1[k][i][2]) + int(array_picture2[k][i][2])

                if q_max < max([r, g, b]):
                    q_max = max([r, g, b])

        # Zakres:
        if q_max > 255:
            d_max = q_max - 255
            x1 = (d_max / 255)

        for i in range(height):
            for k in range(width):
                r = (array_picture1[k][i][0] - (array_picture1[k][i][0] * x1)) + (
                        array_picture2[k][i][0] - (array_picture2[k][i][0] * x1))
                g = (array_picture1[k][i][1] - (array_picture1[k][i][1] * x1)) + (
                        array_picture2[k][i][1] - (array_picture2[k][i][1] * x1))
                b = (array_picture1[k][i][2] - (array_picture1[k][i][2] * x1)) + (
                        array_picture2[k][i][2] - (array_picture2[k][i][2] * x1))

                # Zaokrąglenie do częsći całkowitej
                result[k][i][0] = math.ceil(r)
                result[k][i][1] = math.ceil(g)
                result[k][i][2] = math.ceil(b)

                if f_min > min([r, g, b]):
                    f_min = min([r, g, b])
                if f_max < max([r, g, b]):
                    f_max = max([r, g, b])

        # Normalizacja:
        array_after_normalization = np.zeros((width, height, 3), dtype=np.uint8)
        for i in range(height):
            for k in range(width):
                array_after_normalization[k][i][0] = 255 * (
                        (result[k][i][0] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][1] = 255 * (
                        (result[k][i][1] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][2] = 255 * (
                        (result[k][i][2] - f_min) / (f_max - f_min))

        # poczatek
        Image._show(self.picture1)
        Image._show(self.picture2)

        self.show_picture(Image.fromarray(array_after_normalization, "RGB"),
        self.picture2_name + "summing result_norm")
        self.save_picture(array_picture1, self.picture1_name, "Summing_two_pictures")
        self.save_picture(array_picture2, self.picture2_name, "Summing_two_pictures")
        self.save_picture(result, self.picture1_name, "summing result")
        self.save_picture(array_after_normalization, self.picture1_name, "summing result_norm")

    def multiplication_by_const(self, const):

        picture = self.picture1
        height = picture.height
        width = picture.width

        result = np.empty((height, width, 3), dtype=np.uint8)

        f_min = 255
        f_max = 0

        array_picture = np.array(picture)

        for i in range(height):
            for k in range(width):

                r = int(array_picture[k][i][0])
                g = int(array_picture[k][i][1])
                b = int(array_picture[k][i][2])

                if r == 255:
                    r = const
                elif r == 0:
                    r = 0
                else:
                    r = (int(array_picture[k][i][0]) * int(const)) / 255

                if g == 255:
                    g = const
                elif g == 0:
                    g = 0
                else:
                    g = (int(array_picture[k][i][1]) * int(const)) / 255

                if b == 255:
                    b = const
                elif b == 0:
                    b = 0
                else:
                    b = (int(array_picture[k][i][2]) * int(const)) / 255

                # Zaokrąglenie do częsći całkowitej
                result[k][i][0] = math.ceil(r)
                result[k][i][1] = math.ceil(g)
                result[k][i][2] = math.ceil(b)

                # Min i Maks:
                if f_min > min([r, g, b]):
                    f_min = min([r, g, b])
                if f_max < max([r, g, b]):
                    f_max = max([r, g, b])

        # Normalizacja:
        array_after_normalization = np.zeros((width, height, 3), dtype=np.uint8)
        for i in range(height):
            for k in range(width):
                array_after_normalization[k][i][0] = 255 * (
                        (result[k][i][0] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][1] = 255 * (
                        (result[k][i][1] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][2] = 255 * (
                        (result[k][i][2] - f_min) / (f_max - f_min))

        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), self.picture1_name)
        self.show_picture(Image.fromarray(array_after_normalization, "RGB"), self.picture1_name)

        self.save_picture(array_picture, self.picture1_name, "multiplication_by_const")
        self.save_picture(result, self.picture1_name, "multiplication_by_constpicture result")
        self.save_picture(array_after_normalization, self.picture1_name,
                    "multiplication_by_const_after_normalization")

    def multiplication_by_picture(self):

        picture1 = self.picture1
        picture2 = self.picture2
        height = picture1.height
        width = picture1.width

        # Alokacja pamięci
        result = np.empty((height, width, 3), dtype=np.uint8)

        f_min = 255
        f_max = 0

        array_picture1 = np.array(picture1)
        array_picture2 = np.array(picture2)

        for i in range(height):
            for k in range(width):

                r = int(array_picture1[k][i][0])
                g = int(array_picture1[k][i][1])
                b = int(array_picture1[k][i][2])

                if r == 255:
                    r = array_picture2[k][i][0]
                elif r == 0:
                    r = 0
                else:
                    r = (int(array_picture1[k][i][0]) * int(array_picture2[k][i][0])) / 255

                if g == 255:
                    g = array_picture2[k][i][1]
                elif g == 0:
                    g = 0
                else:
                    g = (int(array_picture1[k][i][1]) * int(array_picture2[k][i][1])) / 255

                if b == 255:
                    b = array_picture2[k][i][2]
                elif b == 0:
                    b = 0
                else:
                    b = (int(array_picture1[k][i][2]) * int(array_picture2[k][i][2])) / 255

                # Zaokrąglenie do częsći całkowitej
                result[k][i][0] = math.ceil(r)
                result[k][i][1] = math.ceil(g)
                result[k][i][2] = math.ceil(b)

                if f_min > min([r, g, b]):
                    f_min = min([r, g, b])
                if f_max < max([r, g, b]):
                    f_max = max([r, g, b])

        # Normalizacja:
        array_after_normalization = np.zeros((width, height, 3), dtype=np.uint8)
        for i in range(height):
            for k in range(width):
                array_after_normalization[k][i][0] = 255 * (
                        (result[k][i][0] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][1] = 255 * (
                        (result[k][i][1] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][2] = 255 * (
                        (result[k][i][2] - f_min) / (f_max - f_min))

        # przed
        Image._show(self.picture1)
        Image._show(self.picture2)
        self.show_picture(Image.fromarray(result, "RGB"), "result multiplication_by_const picture")
        self.show_picture(Image.fromarray(array_after_normalization, "RGB"),
                          "result multiplication_by_const picture normalization")

        self.save_picture(array_picture1, self.picture1_name, "oryginal")
        self.save_picture(array_picture2, self.picture2_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "multiplication_by_picture color - result")

        self.save_picture(array_after_normalization, self.picture1_name,
                          "multiplication_by_picture color - result_after_normalization")

    def mixing_pictures(self, alfa):

        picture1 = self.picture1
        picture2 = self.picture2
        height = picture1.height
        width = picture1.width

        result = np.empty((height, width, 3), dtype=np.uint8)

        array_picture1 = np.array(picture1)
        array_picture2 = np.array(picture2)

        f_min = 255
        f_max = 0

        for i in range(height):
            for k in range(width):

                r = float(array_picture1[k][i][0]) * alfa + (1 - alfa) * float(array_picture2[k][i][0])
                g = float(array_picture1[k][i][1]) * alfa + (1 - alfa) * float(array_picture2[k][i][1])
                b = float(array_picture1[k][i][2]) * alfa + (1 - alfa) * float(array_picture2[k][i][2])

                # Zaokrąglenie:
                result[k][i][0] = math.ceil(r)
                result[k][i][1] = math.ceil(g)
                result[k][i][2] = math.ceil(b)

                if f_min > min([r, g, b]):
                    f_min = min([r, g, b])
                if f_max < max([r, g, b]):
                    f_max = max([r, g, b])

        # Normalizacja:
        array_after_normalization = np.zeros((width, height, 3), dtype=np.uint8)
        for i in range(height):
            for k in range(width):
                array_after_normalization[k][i][0] = 255 * (
                        (result[k][i][0] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][1] = 255 * (
                        (result[k][i][1] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][2] = 255 * (
                        (result[k][i][2] - f_min) / (f_max - f_min))

        Image._show(self.picture1)
        Image._show(self.picture2)
        self.show_picture(Image.fromarray(result, "RGB"), "result mixing")
        self.show_picture(Image.fromarray(array_after_normalization, "RGB"),
                          "result mixing normalization")

        self.save_picture(array_picture1, self.picture1_name, "oryginal")
        self.save_picture(array_picture2, self.picture2_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "mixing_result")

        self.save_picture(array_after_normalization, self.picture1_name,
                    "result_after_mixing_after_normalization")

    def exponentiation_picture(self, ratio):

        picture = self.picture1
        height = picture.height
        width = picture.width

        result = np.empty((height, width, 3), dtype=np.uint8)
        f_picture = 0
        f_min = 255
        f_max = 0

        array_picture = np.array(picture)

        for i in range(height):
            for k in range(width):

                R = int(array_picture[k][i][0])
                G = int(array_picture[k][i][1])
                B = int(array_picture[k][i][2])

                if f_picture < max([R, G, B]):
                    f_picture = max([R, G, B])

        for i in range(height):
            for k in range(width):

                R = int(array_picture[k][i][0])
                G = int(array_picture[k][i][1])
                B = int(array_picture[k][i][2])

                if R == 0:
                    R = 0
                else:
                    R = 255 * (math.pow(int(array_picture[k][i][0]) / f_picture, ratio))

                if G == 0:
                    G = 0
                else:
                    G = 255 * (math.pow(int(array_picture[k][i][1]) / f_picture, ratio))

                if B == 0:
                    B = 0
                else:
                    B = 255 * (math.pow(int(array_picture[k][i][2]) / f_picture, ratio))

                # Zaokrąglenie do częsći całkowitej
                result[k][i][0] = math.ceil(R)
                result[k][i][1] = math.ceil(G)
                result[k][i][2] = math.ceil(B)

                # Min i Maks:
                if f_min > min([R, G, B]):
                    f_min = min([R, G, B])
                if f_max < max([R, G, B]):
                    f_max = max([R, G, B])

        # Normalizacja:
        array_after_normalization = np.zeros((width, height, 3), dtype=np.uint8)
        for i in range(height):
            for k in range(width):
                array_after_normalization[k][i][0] = 255 * (
                        (result[k][i][0] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][1] = 255 * (
                        (result[k][i][1] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][2] = 255 * (
                        (result[k][i][2] - f_min) / (f_max - f_min))

        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), "result exponentiation")
        self.show_picture(Image.fromarray(array_after_normalization, "RGB"),
                          "result exponentiation after_normalization")

        self.save_picture(array_picture, self.picture1_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "result exponentiation")

        self.save_picture(array_after_normalization, self.picture1_name,
                    "result exponentiation_after_normalization")

    def division_by_const(self, const):
        picture = self.picture1
        height = picture.height
        width = picture.width

        result = np.empty((height, width, 3), dtype=np.uint8)

        f_min = 255
        f_max = 0
        q_max = 0

        array_picture = np.array(picture)

        for i in range(height):
            for k in range(width):

                R = int(array_picture[k][i][0]) + int(const)
                G = int(array_picture[k][i][1]) + int(const)
                B = int(array_picture[k][i][2]) + int(const)

                if q_max < max([R, G, B]):
                    q_max = max([R, G, B])

        for i in range(height):
            for k in range(width):

                R = int(array_picture[k][i][0]) + int(const)
                G = int(array_picture[k][i][1]) + int(const)
                B = int(array_picture[k][i][2]) + int(const)

                Q_R = (R * 255) / q_max
                Q_G = (G * 255) / q_max
                Q_B = (B * 255) / q_max

                # Zaokrąglenie do częsći całkowitej
                result[k][i][0] = math.ceil(Q_R)
                result[k][i][1] = math.ceil(Q_G)
                result[k][i][2] = math.ceil(Q_B)

                if f_min > min([Q_R, Q_G, Q_B]):
                    f_min = min([Q_R, Q_G, Q_B])
                if f_max < max([Q_R, Q_G, Q_B]):
                    f_max = max([Q_R, Q_G, Q_B])

        # Normalizacja:
        array_after_normalization = np.zeros((width, height, 3), dtype=np.uint8)
        for i in range(height):
            for k in range(width):
                array_after_normalization[k][i][0] = 255 * (
                        (result[k][i][0] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][1] = 255 * (
                        (result[k][i][1] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][2] = 255 * (
                        (result[k][i][2] - f_min) / (f_max - f_min))

        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), "result divide_by_const")
        self.show_picture(Image.fromarray(array_after_normalization, "RGB"),
                          "result divide_by_const afer norm")

        self.save_picture(array_picture, self.picture1_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "result divide_by_const")

        self.save_picture(array_after_normalization, self.picture1_name,
                    "result divide_by_const afer norm")

    def division_by_picture(self, show=False, save=False):

        picture1 = self.picture1
        picture2 = self.picture2
        height = picture1.height
        width = picture1.width

        result = np.empty((height, width, 3), dtype=np.uint8)

        q_max = 0
        f_min = 255
        f_max = 0

        array_picture1 = np.array(picture1)
        array_picture2 = np.array(picture2)

        for i in range(height):
            for k in range(width):

                r = int(array_picture1[k][i][0]) + int(array_picture2[k][i][0])
                g = int(array_picture1[k][i][1]) + int(array_picture2[k][i][1])
                b = int(array_picture1[k][i][2]) + int(array_picture2[k][i][2])

                # Poszukiwanie maksimum
                if q_max < max([r, g, b]):
                    q_max = max([r, g, b])

        for i in range(height):
            for k in range(width):

                # Obliczanie sum
                r = int(array_picture1[k][i][0]) + int(array_picture2[k][i][0])
                g = int(array_picture1[k][i][1]) + int(array_picture2[k][i][1])
                b = int(array_picture1[k][i][2]) + int(array_picture2[k][i][2])

                q_r = (r * 255) / q_max
                q_g = (g * 255) / q_max
                q_b = (b * 255) / q_max

                # Zaokrąglenie do częsći całkowitej
                result[k][i][0] = math.ceil(q_r)
                result[k][i][1] = math.ceil(q_g)
                result[k][i][2] = math.ceil(q_b)

                if f_min > min([q_r, q_g, q_b]):
                    f_min = min([q_r, q_g, q_b])
                if f_max < max([q_r, q_g, q_b]):
                    f_max = max([q_r, q_g, q_b])

        # Normalizacja:
        array_after_normalization = np.zeros((width, height, 3), dtype=np.uint8)
        for i in range(height):
            for k in range(width):
                array_after_normalization[k][i][0] = 255 * (
                        (result[k][i][0] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][1] = 255 * (
                        (result[k][i][1] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][2] = 255 * (
                        (result[k][i][2] - f_min) / (f_max - f_min))

        Image._show(self.picture1)
        Image._show(self.picture2)
        self.show_picture(Image.fromarray(result, "RGB"), "result divide_by picture")
        self.show_picture(Image.fromarray(array_after_normalization, "RGB"),
                          "result divide_by picture after norm")

        self.save_picture(array_picture1, self.picture1_name, "oryginal")
        self.save_picture(array_picture2, self.picture2_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "result_division_by_picture")

        self.save_picture(array_after_normalization, self.picture1_name,
                    "result_normalization_division_by_picture")

    def roots_picture(self, stopien):

        picture = self.picture1
        height = picture.height
        width = picture.width

        result = np.empty((height, width, 3), dtype=np.uint8)

        f_min = 255
        f_max = 0
        f_picture = 0

        ulamek = 1 / stopien

        array_picture = np.array(picture)

        for i in range(height):
            for k in range(width):

                r = int(array_picture[k][i][0])
                g = int(array_picture[k][i][1])
                b = int(array_picture[k][i][2])

                if f_picture < max([r, g, b]):
                    f_picture = max([r, g, b])

        for i in range(height):
            for k in range(width):

                r = int(array_picture[k][i][0])
                g = int(array_picture[k][i][1])
                b = int(array_picture[k][i][2])

                if r == 0:
                    r = 0
                else:
                    r = 255 * (math.pow(int(array_picture[k][i][0]) / f_picture, ulamek))

                if g == 0:
                    g = 0
                else:
                    g = 255 * (math.pow(int(array_picture[k][i][1]) / f_picture, ulamek))

                if b == 0:
                    b = 0
                else:
                    b = 255 * (math.pow(int(array_picture[k][i][2]) / f_picture, ulamek))

                # Zaokrąglenie do częsći całkowitej
                result[k][i][1] = math.ceil(g)
                result[k][i][2] = math.ceil(b)

                if f_min > min([r, g, b]):
                    f_min = min([r, g, b])
                if f_max < max([r, g, b]):
                    f_max = max([r, g, b])

        # Normalizacja:
        array_after_normalization = np.zeros((width, height, 3), dtype=np.uint8)

        for i in range(height):
            for k in range(width):
                array_after_normalization[k][i][0] = 255 * (
                        (result[k][i][0] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][1] = 255 * (
                        (result[k][i][1] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][2] = 255 * (
                        (result[k][i][2] - f_min) / (f_max - f_min))

        Image._show(self.picture1)
        Image._show(self.picture2)
        self.show_picture(Image.fromarray(array_after_normalization, "RGB"),
                          "result rooting_by_img_after_normalization")

        self.save_picture(array_picture, self.picture1_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                    "result rooting_by_img")

        self.save_picture(array_after_normalization, self.picture1_name,
                    "result rooting_by_img_after_normalization")

    def logarithm_picture(self):

        picture1 = self.picture1
        height = picture1.height
        width = picture1.width

        result = np.empty((height, width, 3), dtype=np.uint8)

        f_picture = 0
        f_min = 255
        f_max = 0

        array_picture1 = np.array(picture1)

        for i in range(height):
            for k in range(width):

                r = int(array_picture1[k][i][0])
                g = int(array_picture1[k][i][1])
                b = int(array_picture1[k][i][2])

                # Poszukiwanie maksimum
                if f_picture < max([r, g, b]):
                    f_picture = max([r, g, b])

        for i in range(height):
            for k in range(width):

                r = int(array_picture1[k][i][0])
                g = int(array_picture1[k][i][1])
                b = int(array_picture1[k][i][2])

                if r == 0:
                    r = 0
                else:
                    r = math.log(1 + int(array_picture1[k][i][0])) / math.log(1 + int(f_picture)) * 255

                if g == 0:
                    g = 0
                else:
                    g = math.log(1 + int(array_picture1[k][i][1])) / math.log(1 + int(f_picture)) * 255

                if b == 0:
                    b = 0
                else:
                    b = math.log(1 + int(array_picture1[k][i][2])) / math.log(1 + int(f_picture)) * 255

                # Zaokroglenie
                result[k][i][0] = math.ceil(r)
                result[k][i][1] = math.ceil(g)
                result[k][i][2] = math.ceil(b)

                # Min i Maks:
                if f_min > min([r, g, b]):
                    f_min = min([r, g, b])
                if f_max < max([r, g, b]):
                    f_max = max([r, g, b])

        # Normalizacja:
        array_after_normalization = np.zeros((width, height, 3), dtype=np.uint8)
        for i in range(height):
            for k in range(width):
                array_after_normalization[k][i][0] = 255 * (
                        (result[k][i][0] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][1] = 255 * (
                        (result[k][i][1] - f_min) / (f_max - f_min))
                array_after_normalization[k][i][2] = 255 * (
                        (result[k][i][2] - f_min) / (f_max - f_min))

        Image._show(self.picture1)
        self.show_picture(Image.fromarray(result, "RGB"), "result logaritm")
        self.show_picture(Image.fromarray(array_after_normalization, "RGB"),
                          "result logaritm_after norm")

        self.save_picture(array_picture1, self.picture1_name, "oryginal")
        self.save_picture(result, self.picture1_name,
                     "result logaritm_after norm")

        self.save_picture(array_after_normalization, self.picture1_name,
                    "result_logaritm_after_normalization")


    # Zapisz:
    def save_picture(self, picture, name, zadanie):
        path = "solutions/task_3/" + name + "_" + zadanie + ".bmp"
        Image.fromarray(picture).save(path)
        path = "solutions/task_3/" + name + "_" + zadanie + ".png"
        Image.fromarray(picture).save(path)

    # Pokaż:
    def show_picture(self, picture, name_pliku):
        picture.save("temporary.png")
        picture.show()
        remove("temporary.png")