from OpenGL.GL import *

class Mesh:

    def __init__(self, program, vertices, get_uv,  normals_padding=5, texture_padding=3, vertex_padding=0, block_size=8):
        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)
        self.VBO = glGenBuffers(1)
        self.size_vertices = len(vertices)
        self.program = program

        if get_uv:
            block_size -= 3

        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices.size * vertices.itemsize, vertices, GL_STATIC_DRAW)

        # position
        pos_loc = glGetAttribLocation(self.program, "position")
        glVertexAttribPointer(pos_loc, 3, GL_FLOAT, GL_FALSE,
                              vertices.itemsize * block_size,
                              ctypes.c_void_p(vertex_padding * vertices.itemsize))
        glEnableVertexAttribArray(pos_loc)

        # texture
        texture_loc = glGetAttribLocation(self.program, "textureCoords")
        glVertexAttribPointer(texture_loc, 2, GL_FLOAT, GL_FALSE,
                              vertices.itemsize * block_size,
                              ctypes.c_void_p(texture_padding * vertices.itemsize))
        glEnableVertexAttribArray(texture_loc)
        if not get_uv:
            # normals
            norm_loc = glGetAttribLocation(self.program, "vertNormal")
            glVertexAttribPointer(norm_loc, 3, GL_FLOAT, GL_FALSE,
                                  vertices.itemsize * block_size,
                                  ctypes.c_void_p(normals_padding * vertices.itemsize))
            glEnableVertexAttribArray(norm_loc)

        glBindVertexArray(0)
        glDisableVertexAttribArray(pos_loc)
        glDisableVertexAttribArray(texture_loc)
        if not get_uv:
            glDisableVertexAttribArray(norm_loc)
        glBindBuffer(GL_ARRAY_BUFFER, 0)


    def RenderMesh(self):
        glBindVertexArray(self.VAO)
        glDrawArrays(GL_TRIANGLES, 0, self.size_vertices)
        glBindVertexArray(0)
