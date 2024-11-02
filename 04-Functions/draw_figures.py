import turtle
import figures

window = turtle.Screen()
window.bgcolor("lightgreen")

side_length = 100
length_a = 200
length_b = 250
figures.draw_square(side_length)
figures.draw_triangle(side_length)
figures.draw_rectangle(length_a, length_b)


window.mainloop()
