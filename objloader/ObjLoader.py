import numpy as np

class ObjLoader:
    def __init__(self):
        self.vert_coords = []
        self.text_coords = []
        self.norm_coords = []

        self.vertex_index = []
        self.texture_index = []
        self.normal_index = []

        self.model = []

    def load_model_with_v_vt_n(self, file):
        for line in open(file, 'r'):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue

            if values[0] == 'v':
                self.vert_coords.append(values[1:4])
            if values[0] == 'vt':
                self.text_coords.append(values[1:3])
            if values[0] == 'vn':
                self.norm_coords.append(values[1:4])

            if values[0] == 'f':
                face_i = []
                text_i = []
                norm_i = []
                for v in values[1:4]:
                    w = v.split('/')
                    face_i.append(int(w[0])-1)
                    text_i.append(int(w[1])-1)
                    norm_i.append(int(w[2])-1)
                self.vertex_index.append(face_i)
                self.texture_index.append(text_i)
                self.normal_index.append(norm_i)

        self.vertex_index = [y for x in self.vertex_index for y in x]
        self.texture_index = [y for x in self.texture_index for y in x]
        self.normal_index = [y for x in self.normal_index for y in x]

        for i in self.vertex_index:
            self.model.extend(self.vert_coords[i])

        for i in self.texture_index:
            self.model.extend(self.text_coords[i])

        for i in self.normal_index:
            self.model.extend(self.norm_coords[i])

        self.model = np.array(self.model, dtype='float32')

    def load_model_with_v(self, file):
        vert_coords = []
        vertex_index = []
        for line in open(file, 'r'):
            if line.startswith('#'):
                continue

            values = line.split()

            if not values:
                continue

            if values[0] == 'v':
                vert_coords.append(values[1:4])

            if values[0] == 'f':
                face_i = []
                for v in values[1:4]:
                    face_i.append(int(v)-1)
                vertex_index.append(face_i)

        vertex_index = [y for x in vertex_index for y in x]

        for i in vertex_index:
            self.vert_coords.extend(vert_coords[i])

        self.vert_coords = np.array(self.vert_coords, dtype='float32')

    def load_model_with_vt(self, file):
        text_coords = []
        texture_index = []
        for line in open(file, 'r'):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue

            if values[0] == 'vt':
                text_coords.append(values[1:3])

            if values[0] == 'f':
                text_i = []
                for v in values[1:4]:
                    w = v.split('/')
                    text_i.append(int(w[1])-1)
                texture_index.append(text_i)

        texture_index = [y for x in texture_index for y in x]

        for i in texture_index:
            self.text_coords.extend(text_coords[i])

        self.text_coords = np.array(self.text_coords, dtype='float32')

    def connect_v_and_vt(self):
        vertices = []
        vert = 0
        text = 0

        while vert < len(self.vert_coords):
            vertices.extend(self.vert_coords[vert: vert + 3])
            vertices.extend(self.text_coords[text: text + 2])

            vert += 3
            text += 2

        return np.array(vertices, dtype='float32')

