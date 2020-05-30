from aritmetic_grey import Aritmetic_grey
from unification import Unification
from arithmetic_color import Arithmetic_color
from geometric import Geometric

# # Zadanie 1
task_1 = Unification("pictures/task_1/Grey_512_view.bmp", "pictures/task_1/indeks.bmp")
task_1.unificationGeometric()
task_1.unificationRozdzielczosciowe()
task_1b = Unification("pictures/task_1/Lake_grey_512.bmp", "pictures/task_1/Moon_256x256_grey.bmp")
task_1b.unificationGeometric()
task_1b.unificationRozdzielczosciowe()
task_1c = Unification("pictures/task_1/golden_retriver_512_color.bmp", "pictures/task_1/belgian_256_color.bmp")
task_1c.unificationGeometricRGB()
task_1c.unificationRozdzielczoscioweRgb()
task_1d = Unification("pictures/task_1/Koala_512_color.bmp", "pictures/task_1/fox_256_color.bmp")
task_1d.unificationGeometricRGB()
task_1d.unificationRozdzielczoscioweRgb()
#
# # Zadanie 2
#
# task_2a = Aritmetic_grey("pictures/task_2/Moon_256x256_grey.bmp", "pictures/task_2/pupies_256x256-grey.bmp")
# task_2a.const_sum(50)
# task_2a.multiplication_by_const(40)
# task_2a.multiplication_by_picture()
# task_2a.mixing_pictures(0.8)
# task_2a.exponentiation_picture(3)
# task_2a.summing_two_pictures()
# task_2a.division_by_const(15)
# task_2a.division_by_picture()
# task_2a.roots_picture(3)
# task_2a.logarithm_picture()
#
#
# task_2b = Aritmetic_grey("pictures/task_2/Lake_grey_512.bmp", "pictures/task_2/rose_512.bmp")
# task_2b.const_sum(70)
# task_2b.summing_two_pictures()
# task_2b.multiplication_by_const(55)
# task_2b.multiplication_by_picture()
# task_2b.mixing_pictures(0.9)
# task_2b.exponentiation_picture(4)
# task_2b.division_by_const(87)
# task_2b.division_by_picture()
# task_2b.roots_picture(1.45)
# task_2b.logarithm_picture()


# # Zadanie 3

task_3 = Arithmetic_color("pictures/task_3/belgian_256_color.bmp", "pictures/task_3/fox_256_color.bmp")
task_3.const_sum(55)
task_3.summing_two_pictures()
task_3.multiplication_by_const(80)
task_3.multiplication_by_picture()
task_3.mixing_pictures(0.5)
task_3.exponentiation_picture(3)
task_3.division_by_const(5)
task_3.division_by_picture()
task_3.roots_picture(1.5)
task_3.logarithm_picture()



task_3b = Arithmetic_color("pictures/task_3/images.bmp", "pictures/task_3/Koala_512_color.bmp")
task_3b.const_sum(80)
task_3b.summing_two_pictures()
task_3b.multiplication_by_const(90)
task_3b.multiplication_by_picture()
task_3b.mixing_pictures(0.8)
task_3b.exponentiation_picture(2)
task_3b.division_by_const(37)
task_3b.division_by_picture()
task_3b.roots_picture(1.5)
task_3b.logarithm_picture()


# # Zadanie 4

task_4 = Geometric("pictures/task_4/belgian_256_color.bmp", "pictures/task_4/fox_256_color.bmp")
task_4.movement(74,28)
task_4.graduation_homogeneous(2)
task_4.graduation_non_homogeneous(2,2)
task_4.rotating(30)
task_4.symetric_x()
task_4.symetric_y()
task_4.symetric_parameter_x()
task_4.symetric_parameter_y()
task_4.piece_cutting(25,78,49,78)
task_4.duplication(70,120,80,200)

task_4b = Geometric("pictures/task_4/Koala_512_color.bmp", "pictures/task_4/images.bmp")
task_4b.movement(145,75)
task_4b.graduation_homogeneous(1.5)
task_4b.graduation_non_homogeneous(1,2)
task_4b.rotating(180)
task_4b.symetric_x()
task_4b.symetric_y()
task_4b.symetric_parameter_x()
task_4b.symetric_parameter_y()
task_4b.piece_cutting(25,78,49,78)
task_4b.duplication(70,120,80,200)