# ***Train data for NeuralTexture with PyOpengl***
This repository generates training data (UV) for NeuralTexture using OpenGL.

---

# ***Prerequisite***
1. Python ***v3.x***
2. PyOpenGL ***v3.1.5***
3. PyGLFW  ***v1.11.0***
4. [Pyrr ***v0.10.3***](https://github.com/adamlwgriffiths/Pyrr)
5. Numpy ***v1.15*** or newer
6. PIL ***v6.2.0*** or newer

---

# ***Usage***
You may need to modify python code to have different result. All results will be saved in ***result*** folder.

## ***Get UV data***
In `main.py` on line 13 change `get_uv` to `True` to get UV data. Otherwise you can just see mesh with some texture.

## ***Save data***
To save data, in `main.py` set `save_data` on line 14 as `True`.
Depends of `get_uv` in `main.py` you can save screenshot (as ***png*** file) if you set `get_uv` equal `True`,
otherwise or numpy array (as ***npy*** file)

## ***Transformation  used on loading Mesh (3D object)***
Examples of transformation:
Create identity matrix and variables that will be store transformation such as translation and rotate.
`
matrix = pyrr.Matrix44.identity()
translation = pyrr.Vector3()
rotate = pyrr.quaternion.create()
`
Move mesh relative to the x, y, z axis. After that you need multiply general matrix to this transformation 
(further we do this with others transformations).
`
translation += [0.0, 0.0, -0.0]
translation_matrix = pyrr.matrix44.create_from_translation(translation)
matrix *= translation_matrix
`
Rotation. Here example across axis y.
`
rotation = pyrr.quaternion.create_from_y_rotation(np.pi / 2.0 * glfw.get_time())
rotate = pyrr.quaternion.cross(rotation, rotate)
rotate = pyrr.matrix44.create_from_quaternion(rotate)
matrix *= rotate
`
Scale. Vector3(x, y, z) means that scale will be used on certain axis with certain coefficient.
`
scale_matrix = pyrr.matrix44.create_from_scale(pyrr.Vector3([1.0, 1.0, 1.0]))
matrix *= scale_matrix
`
After that, we should put this matrix into shader. In `main.py` this doing by pass value into
 `shader.set_transform(transformation())`
More example you can find in pyrr official github: https://github.com/adamlwgriffiths/Pyrr

## ***Load Different obj files.***
Class `ObjLoader` from objloader folder have several function to load mesh.
To load obj file just use:
`
obj = ObjLoader()
vertices = obj.load_model_with_v_vt_n(path_to_obj)
`
Or you can combine v and vt from different obj files:
Фfter we have created `obj` object when:
First function, load v (according to index) into array
`obj.load_model_with_v(path_to_v)`
Second function, load vt (according to index) into array.
NOTICE! In `path_to_vt` file there is v, vt, vn components (and indexes for every components),
while in `path_to_v` there is just v (and index for one component v). So load vt:
`obj.load_model_with_vt(path_to_vt)`
Connect v and vt from different files
`vertices = obj.connect_v_and_vt()`
and pass this array into Mesh then we create it, like in `main.py` on line 69.
