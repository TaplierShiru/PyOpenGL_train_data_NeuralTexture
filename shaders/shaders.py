from OpenGL.GL import *
import OpenGL.GL.shaders


class Shaders:

    def __init__(self, path_to_vertex_shader, path_to_frame_shader):
        # Compile vertex and frame shaders
        vertex_shader = self.load_shader(path_to_vertex_shader)
        frag_shader = self.load_shader(path_to_frame_shader)

        self.__shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
            OpenGL.GL.shaders.compileShader(frag_shader, GL_FRAGMENT_SHADER)
        )

       # glUseProgram(self.__shader)

    def useProgram(self):
        glUseProgram(self.__shader)

    def load_shader(self, shader_file):
        shader_source = ""
        with open(shader_file) as f:
            shader_source = f.read()
        f.close()
        return str.encode(shader_source)

    def set_view(self, view):
        view_loc = glGetUniformLocation(self.__shader, "view")
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
        return True

    def set_model(self, model):
        model_loc = glGetUniformLocation(self.__shader, "model")
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
        return True

    def set_projection(self, projection):
        proj_loc = glGetUniformLocation(self.__shader, "projection")
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
        return True

    def set_transform(self, transform):
        transformLoc = glGetUniformLocation(self.__shader, "transform")
        glUniformMatrix4fv(transformLoc, 1, GL_FALSE, transform)
        return True

