import glfw
from OpenGL.GL import *
import pyrr

class Window:
    def __init__(self, w_width, w_height, camera_position, FOV=45, near=0.01, far=1000.0):
        # Initialize glfw
        if not glfw.init():
            raise Exception("GLFW initialize was failed")

        # glfw.window_hint(glfw.RESIZABLE, GL_FALSE)
        window = glfw.create_window(w_width, w_height, "U cant see me...", None, None)

        if not window:
            glfw.terminate()
            raise Exception("Window creation was failed")

        glfw.make_context_current(window)
        glfw.set_window_size_callback(window, self.__window_resize)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        self.__w_width = w_width
        self.__w_height = w_height

        self.__main_window = window

        self.__camera_position = camera_position
        self.__front = pyrr.Vector3([0.0, 0.0, -1.0])
        self.__up = pyrr.Vector3([0.0, 1.0, 0.0])

        self.__FOV = FOV
        self.__near = near
        self.__far = far


    def __window_resize(self, window, width, height):
        glViewport(0, 0, width, height)

    def calculateViewMatrix(self):
        return pyrr.matrix44.create_look_at(eye=self.__camera_position,
                                            target=self.__camera_position + self.__front,
                                            up=self.__up)

    def calculateProjection(self):
        return pyrr.matrix44.create_perspective_projection_matrix(self.__FOV,
                                                                  self.__w_width / self.__w_height,
                                                                  self.__near,
                                                                  self.__far)
    def rendern_window(self, shader):
        # Set into shaders
        shader.set_projection(self.calculateProjection())
        shader.set_view(self.calculateViewMatrix())
        shader.set_camera_position( self.__camera_position)

    def swap_buffers(self):
        glfw.swap_buffers(self.__main_window)

    def close(self):
        return glfw.window_should_close(self.__main_window)

    def window_destroy(self):
        glfw.destroy_window(self.__main_window)
        return True

    def clearWindowWithColor(self, r=0.0, g=0.0, b=0.0, alpha=1.0):
        glClearColor(r, g, b, alpha)

    def clearBuffer(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

