# draw_figures.py

import turtle
import figures   # twój moduł z funkcją

# Ustawienia okna
window = turtle.Screen()
window.bgcolor("lightgreen")

# Tworzymy żółwia
pen = turtle.Turtle()
pen.speed(5)

# Przenosimy sterowanie na tego żółwia,
# bo moduł figures używa globalnego turtle
turtle.pen = pen

# Rysujemy kwadrat
figures.draw_square(100)

# Wykończenie
pen.hideturtle()
window.mainloop()
