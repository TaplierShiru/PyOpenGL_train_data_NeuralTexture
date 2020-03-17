import cv2
from OpenGL.GL import *
import numpy as np


def save_screenshot(path, w_width, w_height):
    image_buffer = glReadPixels(0, 0, w_width, w_height, OpenGL.GL.GL_RGB, OpenGL.GL.GL_UNSIGNED_BYTE)
    image = np.frombuffer(image_buffer, dtype=np.uint8).reshape(w_width, w_height, 3)
    image = np.flip(image, axis=0)
    cv2.imwrite(path, image)
    return True


def save_uv(path, w_width, w_height):
    image_buffer = glReadPixels(0, 0, w_width, w_height, OpenGL.GL.GL_RGB, OpenGL.GL.GL_UNSIGNED_BYTE)
    image = np.frombuffer(image_buffer, dtype=np.uint8).reshape(w_width, w_height, 3)
    image = image[:,:, :2]
    image = np.flip(image, axis=0)
    np.save(path, image)
    return True

