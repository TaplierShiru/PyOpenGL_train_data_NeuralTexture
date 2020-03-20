from OpenGL.GL import *
import OpenGL.GL.shaders
import pyrr

class Shaders:

    def __init__(self, path_to_vertex_shader, path_to_frame_shader):
        # Compile vertex and frame shaders
        vertex_shader = self.load_shader(path_to_vertex_shader)
        frag_shader = self.load_shader(path_to_frame_shader)

        self.__shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
            OpenGL.GL.shaders.compileShader(frag_shader, GL_FRAGMENT_SHADER)
        )


    def get_program(self):
        return self.__shader

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
        glProgramUniformMatrix4fv(self.__shader, view_loc, 1, GL_FALSE, view)
        return True

    def set_model(self, model):
        inverse_model = pyrr.matrix44.inverse(model)
        model_loc = glGetUniformLocation(self.__shader, "model")
        invers_model_loc = glGetUniformLocation(self.__shader, "inverse_model")
        glProgramUniformMatrix4fv(self.__shader, model_loc, 1, GL_FALSE, model)
        glProgramUniformMatrix4fv(self.__shader, invers_model_loc, 1, GL_FALSE, inverse_model)
        return True

    def set_projection(self, projection):
        proj_loc = glGetUniformLocation(self.__shader, "projection")
        glProgramUniformMatrix4fv(self.__shader, proj_loc, 1, GL_FALSE, projection)
        return True

    def set_camera_position(self, pos_camera):
        eyePosition = glGetUniformLocation(self.__shader, "eyePosition")
        glProgramUniform3f(self.__shader, eyePosition, pos_camera.x, pos_camera.y, pos_camera.z)

