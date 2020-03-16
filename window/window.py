import glfw
from OpenGL.GL import *


class Window:
    def __init__(self, w_width, w_height):
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

        self.__main_window = window

    def __window_resize(self, window, width, height):
        glViewport(0, 0, width, height)

    def swap_buffers(self):
        glfw.swap_buffers(self.__main_window)

    def close(self):
        return glfw.window_should_close(self.__main_window)

    def window_destroy(self):
        glfw.destroy_window(self.__main_window)
        return True

