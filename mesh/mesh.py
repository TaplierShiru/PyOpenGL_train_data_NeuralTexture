from OpenGL.GL import *


class Mesh:

    def __init__(self, vertices, sizeof=4, texture_padding=3, vertex_padding=0, block_size=5):
        self.VBO = glGenBuffers(1)
        self.size_vertices = len(vertices)

        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, sizeof * len(vertices), vertices, GL_STATIC_DRAW)

        # position
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE,
                              sizeof * block_size,
                              ctypes.c_void_p(vertex_padding * sizeof))
        glEnableVertexAttribArray(0)

        # texture
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE,
                              sizeof * block_size,
                              ctypes.c_void_p(texture_padding * sizeof))
        glEnableVertexAttribArray(1)

    def RenderMesh(self):
        #glBindVertexArray(0)
        glDrawArrays(GL_TRIANGLES, 0, self.size_vertices)