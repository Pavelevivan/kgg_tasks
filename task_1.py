import pyglet
from pyglet.gl import *
import math
# Задачи
# 1 График меняется при изменении ширины, высоты
# 2 Подписать ординаты абсциссы
# 3 

window = pyglet.window.Window(width=500, height=600, resizable=True)
pyglet.gl.glClearColor(1,1,1,1)
A = 1
B = 4
C = -1

X_MIN = -10
X_MAX = 10 

Y_MAX = 0
Y_MIN = 0


def get_parabola(a, b, c):
    return lambda x: a*x**2 + b*x + c

def foo(x):
    return math.sin(x) * x ** 2



def cartesian_to_screen(x, y):
    xx = round((x - X_MIN)*window.width / (X_MAX - X_MIN))
    yy = round((Y_MAX - y)*(window.height -1) / (Y_MAX - Y_MIN))
    return xx, yy

def screen_to_cartesian(x, y):
    xx = (x*(X_MAX - X_MIN)/(window.width)) + X_MIN
    yy = (y*(Y_MAX - Y_MIN)/(window.height)) + Y_MIN
    return xx, yy

def get_vertices_function(a, b, func):
    vertices = []
    for xx in range(1, window.width):
        x, _ = screen_to_cartesian(xx, 0)
        _, yy = cartesian_to_screen(0, func(x))
        vertices.append(xx)
        vertices.append(window.height -yy)

    return tuple(vertices)

def draw_coordinate_lines():
    xx0, yy0 = cartesian_to_screen(0, 0)
    yy0 = window.height - yy0
    pyglet.graphics.draw(2, pyglet.gl.GL_LINE_STRIP,
                        ('v2i', (xx0, window.height, xx0, 0)),
                        ('c3B', (0, 0, 0)*2))
    pyglet.graphics.draw(2, pyglet.gl.GL_LINE_STRIP,
                        ('v2i', (0, yy0, window.width, yy0)),
                        ('c3B', (0, 0, 0)*2))




def draw_notches():
    step = max(1, round(screen_to_cartesian(20, 0)[0] - screen_to_cartesian(0, 0)[0]))
    for x in range(step, min(abs(X_MIN), abs(X_MAX)), step):
        xx_right, yy = cartesian_to_screen(x, 0)
        xx_left, yy = cartesian_to_screen(-x, 0)
        pyglet.graphics.draw(2, pyglet.gl.GL_LINE_STRIP,
                            ('v2i', (xx_right, yy + 2, xx_right, yy - 2)),
                            ('c3B', (0, 0, 0)*2))
        pyglet.graphics.draw(2, pyglet.gl.GL_LINE_STRIP,
                            ('v2i', (xx_left, yy + 2, xx_left, yy - 2)),
                            ('c3B', (0, 0, 0)*2))

        pyglet.text.Label(str(x),
                          font_name='Times New Roman',
                          font_size=5,
                          x=xx_right, y=yy - 10,
                          anchor_x='center', anchor_y='center',
                          color=(0, 0, 0, 255),
                          bold=True).draw()

        pyglet.text.Label(str(-x),
                          font_name='Times New Roman',
                          font_size=5,
                          x=xx_left, y=yy - 10,
                          anchor_x='center', anchor_y='center',
                          color=(0, 0, 0, 255),
                          bold=True).draw()

    step = max(1, round(screen_to_cartesian(0, 20)[1] - screen_to_cartesian(0, 0)[1]))
    lable = None
    for y in range(step, min(abs(Y_MIN), abs(Y_MAX)), step):
        xx, yy_down = cartesian_to_screen(0, y)
        xx, yy_up = cartesian_to_screen(0, -y)
        pyglet.graphics.draw(2, pyglet.gl.GL_LINE_STRIP,
                            ('v2i', (xx - 2, yy_up, xx + 2, yy_up)),
                            ('c3B', (0, 0, 0)*2))
        pyglet.graphics.draw(2, pyglet.gl.GL_LINE_STRIP,
                            ('v2i', (xx - 2, yy_down, xx + 2, yy_down)),
                            ('c3B', (0, 0, 0)*2))

        pyglet.text.Label(str(y),
                          font_name='Times New Roman',
                          font_size=5,
                          x=xx + 10, y=yy_up,
                          anchor_x='center', anchor_y='center',
                          color=(0, 0, 0, 255),
                          bold=True).draw()

        pyglet.text.Label(str(-y),
                          font_name='Times New Roman',
                          font_size=5,
                          x=xx + 10, y=yy_down,
                          anchor_x='center', anchor_y='center',
                          color=(0, 0, 0, 255),
                          bold=True).draw()

        

def draw():
    points = get_vertices_function(X_MIN, X_MAX, parabola)
    pyglet.graphics.draw(int((len(points) // 2)), pyglet.gl.GL_LINE_STRIP,
    ('v2i', points), ('c3B', (255, 0, 0)*int((len(points) // 2))))
    draw_notches()
    

@window.event
def on_resize(width, height):
    window.clear()
    draw()
    
@window.event
def on_draw():
    window.clear()
    draw_coordinate_lines()
    draw()

def find_min_max_function(func):
    ymin = ymax = func(X_MIN)
    for xx in range(window.width):
        x, _ = screen_to_cartesian(xx, 0)
        y = func(x)
        ymin = min(ymin, y)
        ymax = max(ymax, y)
    ymin = round(ymin)
    ymax = round(ymax)
    return ymin, ymax


parabola = foo
Y_MIN, Y_MAX = find_min_max_function(parabola)

pyglet.app.run()


