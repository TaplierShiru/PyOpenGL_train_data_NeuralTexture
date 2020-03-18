import glfw
import pyrr


from shaders import Shaders
from objloader.ObjLoader import *
from window import Window
from texture import Texture
from mesh import Mesh
from data import save_screenshot, save_uv


get_uv = False
save_data = True

path_to_v = "data/face/example_with_v.obj"
path_to_vt = "data/face/example_with_vt.obj"
path_to_obj = "data/cube/cube.obj"
# Window size
w_width, w_height = 800, 800

if get_uv:
    path_to_frame_shader = "shaders/shader_uv.fs"
else:
    path_to_frame_shader = "shaders/shader.fs"
path_to_vertex_shader = "shaders/shader.vs"
path_to_texture = "data/cube/box.jpg"

path_save_data = 'result/'

def transformation():
    # Some transformation of mesh
    matrix = pyrr.Matrix44.identity()
    translation = pyrr.Vector3()
    scale = pyrr.Vector3([1.0, 1.0, 1.0])
    rotate = pyrr.quaternion.create()
    # Move relative to the x, y, z axis
    translation += [0.0, 0.0, -0.0]
    translation_matrix = pyrr.matrix44.create_from_translation(translation)
    matrix *= translation_matrix
    # Rotation, Across axis y
    rotation = pyrr.quaternion.create_from_y_rotation(np.pi / 2.0 * glfw.get_time())
    rotate = pyrr.quaternion.cross(rotation, rotate)
    rotate = pyrr.matrix44.create_from_quaternion(rotate)
    matrix *= rotate
    # Scale
    scale_matrix = pyrr.matrix44.create_from_scale(scale)
    matrix *= scale_matrix

    return matrix

def main():
    window = Window(w_width, w_height)
    obj = ObjLoader()

    # First function, load v (according to index) into array
    obj.load_model_with_v(path_to_v)
    obj.load_model_with_vt(path_to_vt)
    # Connect v and vt from different files
    vertices = obj.connect_v_and_vt()

    # Load obj file
    #vertices = obj.load_model_with_v_vt_n(path_to_obj)

    shader = Shaders(path_to_vertex_shader, path_to_frame_shader)
    object = Mesh(vertices)

    def_texture = Texture(path_to_texture)
    shader.useProgram()

    window.clearWindowWithColor()
    # Started position of the mesh and camera
    view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, -10.0]))
    projection = pyrr.matrix44.create_perspective_projection_matrix(12.0, w_width / w_height, 0.01, 1000.0)
    model = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0]))
    # Set into shaders
    shader.set_model(model)
    shader.set_projection(projection)
    shader.set_view(view)

    # Main loop
    while not window.close():
        glfw.poll_events()
        window.clearBuffer()

        # Set transformation to mesh
        shader.set_transform(transformation())

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

