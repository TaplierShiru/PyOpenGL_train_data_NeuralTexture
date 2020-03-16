from OpenGL.GL import *
from PIL import Image
import numpy as np


class Texture:

    def __init__(self, path_to_texture):
        # Bind texture
        self.__texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.__texture)
        # Set the texture wrapping parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        # Set texture filtering parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        # load image for texture
        image = Image.open(path_to_texture)
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = np.array(list(flipped_image.getdata()), np.uint8)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
        glEnable(GL_TEXTURE_2D)

    def use_texture(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.__texture)
        return True

    def Clear_texture(self):
        glDeleteTextures([self.__texture])
        return True

