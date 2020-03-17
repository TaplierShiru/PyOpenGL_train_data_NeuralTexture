# ***Train data for NeuralTexture with PyOpengl***
This repository generates training data (UV) for NeuralTexture using OpenGL.

---

# ***Prerequisite***
1. [PyOpenGL ***v3.1.5***](https://anaconda.org/conda-forge/pyopengl)
2. [PyGLFW  ***v1.11.0***](https://anaconda.org/conda-forge/pyglfw)
3. [Pyrr ***v0.10.3***](https://anaconda.org/conda-forge/pyrr)
4. Numpy ***v1.15*** or newer

---

# ***Usage***
You may need to modify python code to have different result.

## ***Get UV data***
In `main.py` line 14 change `get_uv` to `True` to get UV data. Otherwise you just can see pure mesh with some texture.

## ***Save data***
To save data, in `main.py` set `save_data` on line 14 as `True`.
Depends of `get_uv` in `main.py` you can save screenshot (as ***png*** file) or numpy array (as ***npy*** file)

---

## ***Load Different obj files.***
...soon...
