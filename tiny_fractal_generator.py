#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      themi
#
# Created:     20-10-2020
# Copyright:   (c) themi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter.font import Font
from math import sqrt, sin, cos, pi, degrees, acos, asin
from time import sleep

def kochsnow(canvas, degree, final_lines):
    for i in range(degree):
        new_final_lines = []
        for line in final_lines:
            first_pos = [line[0], line[1]]

            length = sqrt((line[2] - line[0])**2 + (line[3] - line[1])**2)
            length_third = length/3
            direction = (line[3] - line[1]) / (line[2] - line[0])

            second_pos = [line[0] - (length_third * (line[0] - line[2]))/length,
                          line[1] - (length_third * (line[1] - line[3]))/length]

            theta = 2 * pi / 3

            third_pos = [((first_pos[0] - second_pos[0]) * cos(theta) + (first_pos[1] - second_pos[1]) * sin(theta) ) + second_pos[0],
                       (-(first_pos[0] - second_pos[0]) * sin(theta) + (first_pos[1] - second_pos[1]) * cos(theta) ) + second_pos[1]]

            fourth_pos = [line[2] - (length_third * (line[2] - line[0]))/length,
                          line[3] - (length_third * (line[3] - line[1]))/length]

            fifth_pos = [line[2],
                         line[3]]

            new_final_lines.append([first_pos[0], first_pos[1], second_pos[0], second_pos[1]])
            new_final_lines.append([second_pos[0], second_pos[1], third_pos[0], third_pos[1]])
            new_final_lines.append([third_pos[0], third_pos[1], fourth_pos[0], fourth_pos[1]])
            new_final_lines.append([fourth_pos[0], fourth_pos[1], fifth_pos[0], fifth_pos[1]])

        final_lines = new_final_lines

    for coord in final_lines:
        canvas.create_line(coord[0], coord[1], coord[2], coord[3])

def ccurve(canvas, degree, final_lines):
    for i in range(degree):
        new_final_lines = []
        for line in final_lines:
            first_pos = [line[0], line[1]]
            third_pos = [line[2], line[3]]

            length = sqrt((line[2] - line[0])**2 + (line[3] - line[1])**2)
            length_new = length/2

            extra_pos = [line[0] - (length_new * (line[0] - line[2]))/length,
                         line[1] - (length_new * (line[1] - line[3]))/length]

            theta = pi / 2

            second_pos = [((first_pos[0] - extra_pos[0]) * cos(theta) + (first_pos[1] - extra_pos[1]) * sin(theta) ) + extra_pos[0],
                          (-(first_pos[0] - extra_pos[0]) * sin(theta) + (first_pos[1] - extra_pos[1]) * cos(theta) ) + extra_pos[1]]

            new_final_lines.append([first_pos[0], first_pos[1], second_pos[0], second_pos[1], "red"])
            new_final_lines.append([second_pos[0], second_pos[1], third_pos[0], third_pos[1], "black"])

        final_lines = new_final_lines

    for coord in final_lines:
        canvas.create_line(coord[0], coord[1], coord[2], coord[3], fill=coord[4])

def create_frac(root, canvas, degrees, fractal_type):
    canvas.delete("all")
    if fractal_type == 1:
        for i in range(degrees + 1):
            root.after(100*i-1, canvas.delete, "all")
            root.after(100*i, kochsnow, canvas, i, [[250, 10, 50, 350], [50, 350, 450, 350], [450, 350, 250, 10]])

    elif fractal_type == 2:
        for i in range(degrees + 1):
            root.after(100*i-1, canvas.delete, "all")
            root.after(100*i, ccurve, canvas, i, [[200, 250, 300, 250, "black"]])

def main():
    root = Tk(screenName="Koch's Triangle and C-Curve")
    root.title("Fractal Genorator")
    cv = Canvas(root, width=500, height=500)
    cv.grid(row= 0, column = 0)

    frame = Frame(root)
    frame.grid(row= 0, column = 1)

    degree_scale = Scale(frame, from_=0, to=13, orient="horizontal",)
    degree_scale.grid(row=0, column = 0, pady= 10)

    fractal_type = IntVar()
    fractal_type.set(2)

    def change_scale():
        if fractal_type.get() == 2:
            degree_scale.config(to=13)
        elif fractal_type.get() == 1:
            degree_scale.config(to=20)

    ccurve_f_type = Radiobutton(frame, text="C-Curve", variable=fractal_type, value=2, indicatoron=True, anchor="w", command=lambda:change_scale())
    ccurve_f_type.grid(row = 1, column = 0)

    koch_f_type = Radiobutton(frame, text= "Koch Snowflake", variable=fractal_type, value=1, indicatoron=True, anchor="w", command=lambda:change_scale())
    koch_f_type.grid(row = 2, column = 0)

    start_button = Button(frame, text="Start", command=lambda:create_frac(root, cv, degree_scale.get(), fractal_type.get()))
    start_button.grid(row=3, column=0)

    root.mainloop()


if __name__ == '__main__':
    main()
