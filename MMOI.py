import math
from math import pi


def L_stringer(height, lower_width, thickness):  # horizontal part of L is width and vertical part is height
    x_lower = lower_width / 2
    x_height = 0
    y_lower = 0
    y_height = height / 2

    x_bar = (lower_width * thickness * x_lower + height * thickness * x_height) / (
                lower_width * thickness + height * thickness)  # left bottom corner is datum feature
    y_bar = (lower_width * thickness * y_lower + height * thickness * y_height) / (
                lower_width * thickness + height * thickness)  # left bottom corner is datum feature

    tot_area = thickness * lower_width + thickness * height

    Ixx = (thickness * height ** 3) / 12 + height * thickness * (y_bar - y_height) ** 2 + lower_width * thickness * (
                y_bar - y_lower) ** 2
    Iyy = (thickness * lower_width ** 3) / 12 + lower_width * thickness * (
                x_bar - x_lower) ** 2 + height * thickness * (x_bar - x_height) ** 2

    return Ixx, Iyy, tot_area, x_bar, y_bar,


print("L-stringer: Ixx, Iyy, L_area, x_bar_L, y_bar_L = ", L_stringer(2, 1, 0.001))


def I_stringer(height, lower_width, upper_width, thickness):
    x_lower = 0
    x_height = 0
    x_upper = 0
    y_lower = 0
    y_height = height / 2
    y_upper = height

    x_bar = (lower_width * thickness * x_lower + height * thickness * x_height + upper_width * thickness * x_upper) / (
                lower_width * thickness + height * thickness + upper_width * thickness)  # bottom center is datum feature, a.k.a symmetric around y-axis
    y_bar = (height * thickness * y_height + lower_width * thickness * y_lower + upper_width * thickness * y_upper) / (
                height * thickness + lower_width * thickness + upper_width * thickness)  # bottom center is datum feature, a.k.a symmetric around y-axis

    tot_area = height * thickness + lower_width * thickness + upper_width * thickness

    Ixx = (thickness * height ** 3) / 12 + lower_width * thickness * (y_bar - y_lower) ** 2 + height * thickness * (
                y_height - y_bar) ** 2 + upper_width * thickness * (y_upper - y_bar) ** 2
    Iyy = (thickness * lower_width ** 3) / 12 + (thickness * upper_width ** 3) / 12
    return Ixx, Iyy, tot_area, x_bar, y_bar


print("I-stringer: Ixx, Iyy, I_area, x_bar_I, y_bar_I = ", I_stringer(2, 1, 1, 0.001))


def S_stringer(height, lower_width, width_upper, thickness):
    x_lower = -lower_width / 2
    x_height = 0
    x_upper = width_upper / 2
    y_lower = 0
    y_height = height / 2
    y_upper = height

    x_bar = (lower_width * thickness * x_lower + height * thickness * x_height + width_upper * thickness * x_upper) / (
            lower_width * thickness + height * thickness + width_upper * thickness)  # bottom center is datum feature
    y_bar = (lower_width * thickness * y_lower + height * thickness * y_height + width_upper * thickness * y_upper) / (
            lower_width * thickness + height * thickness + width_upper * thickness)  # bottom center is datum feature

    tot_area = lower_width * thickness + height * thickness + width_upper * thickness

    Ixx = (thickness * height ** 3) / 12 + lower_width * thickness * (y_bar - y_lower) ** 2 + height * thickness * (
                y_bar - y_height) ** 2 + width_upper * thickness * (y_bar - y_upper) ** 2
    Iyy = (thickness * lower_width ** 3) / 12 + (thickness * width_upper ** 3) / 12 + lower_width * thickness * (
                x_bar - x_lower) ** 2 + height * thickness * (x_bar - x_height) ** 2 + width_upper * thickness * (
                      x_bar - x_upper) ** 2
    return Ixx, Iyy, tot_area, x_bar, y_bar


print("S-stringer: Ixx, Iyy, S_area, x_bar_S, y_bar_S = ", S_stringer(2, 1, 1, 0.001))


def C_stringer(lower_width, height, upper_width, thickness):
    x_lower = lower_width / 2
    x_height = 0
    x_upper = upper_width / 2
    y_lower = 0
    y_height = height / 2
    y_upper = height

    x_bar = (lower_width * thickness * x_lower + height * thickness * x_height + upper_width * thickness * x_upper) / (
            lower_width * thickness + height * thickness + upper_width * thickness)  # left bottom corner is datum feature
    y_bar = (lower_width * thickness * y_lower + height * thickness * y_height + upper_width * thickness * y_upper) / (
            lower_width * thickness + height * thickness + upper_width * thickness)  # left bottom corner is datum feature

    tot_area = lower_width * thickness + height * thickness + upper_width * thickness

    Ixx = (thickness * height ** 3) / 12 + lower_width * thickness * (y_bar - y_lower) ** 2 + height * thickness * (
                y_bar - y_height) ** 2 + upper_width * thickness * (y_bar - y_upper) ** 2
    Iyy = (thickness * lower_width ** 3) / 12 + (thickness * upper_width ** 3) / 12 + lower_width * thickness * (
                x_bar - x_lower) ** 2 + height * thickness * (x_bar - x_height) ** 2 + upper_width * thickness * (
                      x_bar - x_upper) ** 2
    return Ixx, Iyy, tot_area, x_bar, y_bar


print("C-stringer: Ixx, Iyy, C_area, x_bar_C, y_bar_C = ", C_stringer(1, 1, 1, 0.001))


def T_stringer(height, lower_width, thickness):
    x_lower = 0
    x_height = 0
    y_lower = 0
    y_height = height / 2

    x_bar = (lower_width * thickness * x_lower + height * thickness * x_height) / (
                lower_width * thickness + height * thickness)  # center bottom is datum feature
    y_bar = (lower_width * thickness * y_lower + height * thickness * y_height) / (
                lower_width * thickness + height * thickness)  # center bottom is datum feature

    tot_area = thickness * lower_width + thickness * height

    Ixx = (thickness * height ** 3) / 12 + height * thickness * (y_bar - y_height) ** 2 + lower_width * thickness * (
                y_bar - y_lower) ** 2
    Iyy = (thickness * lower_width ** 3) / 12 + lower_width * thickness * (
                x_bar - x_lower) ** 2 + height * thickness * (x_bar - x_height) ** 2
    return Ixx, Iyy, tot_area, x_bar, y_bar


print("T-stringer: Ixx, Iyy, T_area, x_bar_T, y_bar_T = ", T_stringer(1, 1, 0.001))


def J_stringer(height, lower_width, radius_top, thickness):  # J stringer with round head
    x_lower = 0
    x_height = 0
    x_round = radius_top
    y_lower = 0
    y_height = height / 2
    y_round = height + (4 * radius_top) / (3 * math.pi)

    x_bar = (
                        lower_width * thickness * x_lower + height * thickness * x_height + math.pi * radius_top * thickness * x_round) / (
                        lower_width * thickness + height * thickness + math.pi * radius_top * thickness)  # center bottom is datum feature
    y_bar = (
                        lower_width * thickness * y_lower + height * thickness * y_height + math.pi * radius_top * thickness * y_round) / (
                        lower_width * thickness + height * thickness + math.pi * radius_top * thickness)  # center bottom is datum feature

    tot_area = lower_width * thickness + height * thickness + math.pi * radius_top * thickness

    Ixx = (thickness * height ** 3) / 12 + (1 / 8) * math.pi * radius_top ** 4 + lower_width * thickness * (
                y_bar - y_lower) ** 2 + height * thickness * (
                      y_bar - y_height) ** 2 + pi * radius_top * thickness * (y_bar - y_round) ** 2
    Iyy = (thickness * lower_width ** 3) / 12 + (1 / 8) * math.pi * radius_top ** 4 + lower_width * thickness * (
                x_bar - x_lower) ** 2 + height * thickness * (
                      x_bar - x_height) ** 2 + math.pi * radius_top * thickness * (x_bar - x_round) ** 2
    return Ixx, Iyy, tot_area, x_bar, y_bar


print("J-stringer: Ixx, Iyy, J_area, x_bar_J, y_bar_J = ", J_stringer(1, 1, 1, 0.001))

def Hat_stringer(heigth, lowerleft_width,lowerright_width, upper_width, thickness):
    x_lowerleft = -((1/2)*upper_width+(1/2)*lowerleft_width)
    x_lowerright = (1/2)*upper_width+(1/2)*lowerright_width
    x_upper = 0
    x_heightleft = -(1/2)*upper_width
    x_heightright = (1/2)*upper_width
    y_lowerleft = 0 
    y_lowerright = 0
    y_upper = heigth
    y_heightleft = heigth/2
    y_heightright = heigth/2

    x_bar = (lowerleft_width*thickness*x_lowerleft+lowerright_width*thickness*x_lowerright+heigth*thickness*x_heightleft +heigth*thickness*x_heightright+upper_width*thickness*x_upper)/ (lowerleft_width*thickness+lowerright_width*thickness+heigth*thickness +heigth*thickness+upper_width*thickness)
    y_bar = (lowerleft_width*thickness*y_lowerleft+lowerright_width*thickness*y_lowerright+heigth*thickness*y_heightleft +heigth*thickness*y_heightright+upper_width*thickness*y_upper)/ (lowerleft_width*thickness+lowerright_width*thickness+heigth*thickness +heigth*thickness+upper_width*thickness)

    tot_area = lowerleft_width*thickness + lowerright_width*thickness+2*heigth*thickness+upper_width*thickness

#    Ixx = 2*(thickness*heigth**3)/12 + heigth*thickness*(y_bar - y_heightleft)**2 + heigth*thickness*(y_heightright-y_bar)**2 + lowerleft_width*thickness(y_bar-y_lowerleft)**2 + lowerright_width*thickness*(y_bar-y_lowerright)**2 + upper_width*thickness*(y_bar-y_upper)**2
    Iyy = (thickness*lowerleft_width**3)/12 + (thickness*lowerleft_width**3)/12 + (thickness*upper_width**3)/12 + lowerleft_width*thickness*(x_bar-x_lowerleft)**2 + lowerright_width*thickness*(x_bar-x_lowerright)**2 + heigth*thickness*(x_bar-x_heightleft)**2 +heigth*thickness*(x_bar-x_heightright)**2 + upper_width*thickness*(x_bar-x_upper)**2
    return Iyy, tot_area, x_bar, y_bar

print("Hat-stringer: Ixx, Iyy, Hat_area, x_bar_Hat, y_bar_Hat = ", Hat_stringer(1, 0.25, 0.25, 0.5, 0.001))

