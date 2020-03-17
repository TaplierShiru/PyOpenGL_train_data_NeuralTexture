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
from mesh import Mesh

get_uv = False
save_data = False
w_width, w_height = 800, 800

if get_uv:
    path_to_frame_shader = "shaders/shader_uv.fs"
else:
    path_to_frame_shader = "shaders/shader.fs"

path_to_vertex_shader = "shaders/shader.vs"
path_to_obj = "test_data/cube.obj"
path_to_texture = "test_data/box.jpg"


def main():
    window = Window(w_width, w_height)
    obj = ObjLoader()

    obj.load_model_with_v('T:/download/woman_2/stab/stabilized_located_frozen/Video15/mesh/10.obj')
    obj.load_model_with_vt('T:/download/woman_2/test.obj')
    vertices = obj.connect_v_and_vt()
    print(vertices.shape)
    #vertices = np.load('test_data/test_face.npy')

    shader = Shaders(path_to_vertex_shader, path_to_frame_shader)
    object = Mesh(vertices)

    def_texture = Texture(path_to_texture)
    shader.useProgram()

    glClearColor(0.0, 0.0, 0.0, 1.0)

    #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0]))
    projection = pyrr.matrix44.create_perspective_projection_matrix(65.0, w_width / w_height, 0.1, 100.0)
    model = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, -4.0]))

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
        object.RenderMesh()

        if save_data:
            image_buffer = glReadPixels(0, 0, w_width, w_height, OpenGL.GL.GL_RGB, OpenGL.GL.GL_UNSIGNED_BYTE)
            image = np.frombuffer(image_buffer, dtype=np.uint8).reshape(w_width, w_height, 3)
            cv2.imwrite("results/image.png", image)
        
        window.swap_buffers()
        # If you want only single frame, uncomment code below
        #window.window_destroy()
        #break

    def_texture.Clear_texture()
    glfw.terminate()

if __name__ == "__main__":
    main()

