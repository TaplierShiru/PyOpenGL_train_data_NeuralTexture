import glfw
import cv2
from OpenGL.GL import *
import pyrr

from shaders import Shaders
from objloader.ObjLoader import *
from window import Window
from texture import Texture
from mesh import Mesh
from data import save_screenshot, save_uv

get_uv = False
save_data = False
w_width, w_height = 800, 800

if get_uv:
    path_to_frame_shader = "shaders/shader_uv.fs"
else:
    path_to_frame_shader = "shaders/shader.fs"

path_to_vertex_shader = "shaders/shader.vs"
path_to_obj = "data/cube.obj"
path_to_texture = "data/box.jpg"

path_save_data = 'result/'

def main():
    window = Window(w_width, w_height)
    obj = ObjLoader()

    obj.load_model_with_v('T:/download/woman_2/stab/stabilized_located_frozen/Video15/mesh/10.obj')
    obj.load_model_with_vt('T:/download/woman_2/test.obj')
    vertices = obj.connect_v_and_vt()

    shader = Shaders(path_to_vertex_shader, path_to_frame_shader)
    object = Mesh(vertices)

    def_texture = Texture(path_to_texture)
    shader.useProgram()

    glClearColor(0.0, 0.0, 0.0, 1.0)

    view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0]))
    projection = pyrr.matrix44.create_perspective_projection_matrix(45.0, w_width / w_height, 0.1, 100.0)
    model = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, -4.0]))

    # Started position of the mesh and camera
    shader.set_model(model)
    shader.set_projection(projection)
    shader.set_view(view)

    # Main loop
    while not window.close():
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Some transformation on mesh
        rot_x = pyrr.Matrix44.from_x_rotation(0.5 * glfw.get_time())
        rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time())
        shader.set_transform(rot_x * rot_y)

        # Bind texture to current Mesh
        def_texture.use_texture()
        object.RenderMesh()

        if save_data:
            if get_uv:
                save_uv(path_save_data + 'uv_text.npy', w_width, w_height)
            else:
                save_screenshot(path_save_data + 'screen.png', w_width, w_height)
        
        window.swap_buffers()
    else:
        def_texture.clear_texture()
        window.window_destroy()
        glfw.terminate()

if __name__ == "__main__":
    main()

