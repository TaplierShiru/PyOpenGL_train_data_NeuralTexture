import glfw
import numpy as np
import cv2
from PIL import Image
from OpenGL.GL import *
import pyrr


from shaders import Shaders
from objloader.ObjLoader import *
from window import Window
from texture import Texture

show_uv = False
w_width, w_height = 800, 800

if show_uv:
    path_to_frame_shader = "shaders/shader_uv.fs"
else:
    path_to_frame_shader = "shaders/shader.fs"

path_to_vertex_shader = "shaders/shader.vs"
path_to_obj = "test_data/cube.obj"
path_to_texture = "test_data/box.jpg"


def main():
    window = Window(w_width, w_height)

    obj = ObjLoader()
    obj.load_model(path_to_obj)#test_data/cube.obj

    texture_offset = len(obj.vertex_index)*12 # step 12, better rebuild this loader into something better
    shader = Shaders(path_to_vertex_shader, path_to_frame_shader)

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, obj.model.itemsize * len(obj.model), obj.model, GL_STATIC_DRAW)

    #position
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj.model.itemsize * 3, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)
    #texture
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj.model.itemsize * 2, ctypes.c_void_p(texture_offset))
    glEnableVertexAttribArray(1)

    def_texture = Texture(path_to_texture)
    shader.useProgram()

    glClearColor(0.0, 0.0, 0.0, 1.0)

    #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, -3.0]))
    projection = pyrr.matrix44.create_perspective_projection_matrix(65.0, w_width / w_height, 0.1, 100.0)
    model = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0]))

    # Started position of the mesh and camera
    shader.set_model(model)
    shader.set_projection(projection)
    shader.set_view(view)

    while not window.close():
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        rot_x = pyrr.Matrix44.from_x_rotation(0.5 * glfw.get_time() )
        rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time() )

        shader.set_transform(rot_x * rot_y)
        # Bind texture to current Mesh
        def_texture.use_texture()
        glDrawArrays(GL_TRIANGLES, 0, len(obj.vertex_index))

        image_buffer = glReadPixels(0, 0, w_width, w_height, OpenGL.GL.GL_RGB, OpenGL.GL.GL_UNSIGNED_BYTE)
        image = np.frombuffer(image_buffer, dtype=np.uint8).reshape(w_width, w_height, 3)
        cv2.imwrite("image.png", image)
        
        window.swap_buffers()
        # If you want only single frame, uncomment code below
        #window.window_destroy()
        #break

    def_texture.Clear_texture()
    glfw.terminate()

if __name__ == "__main__":
    main()

