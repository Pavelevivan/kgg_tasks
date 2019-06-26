import pyglet
from pyglet.gl import *


window = pyglet.window.Window()
# vertices = [0, 0,
#             window.width, 0,
#             window.width, window.height]
# vertices_gl_array = (GLfloat * len(vertices))(*vertices)

# glEnableClientState(GL_VERTEX_ARRAY)
# glVertexPointer(2, GL_FLOAT, 0, vertices_gl_array)



def get_vertices_function_1(a, b, func):
    vertices = []
    for x in range(a, b + 1):
        vertices.append(int(func(x) + window.height // 2))
        vertices.append(int(x + window.width // 2))
        
    return tuple(vertices)


@window.event
def on_draw():
    window.clear()
    points = get_vertices_function_1(0, 50, lambda x: x**2 + 2*x + 5 ) 
    pyglet.graphics.draw(int((len(points) // 2)), pyglet.gl.GL_POINTS,
    ('v2i', points))
    
@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')

pyglet.app.run()


