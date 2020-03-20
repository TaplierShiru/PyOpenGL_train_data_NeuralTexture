from OpenGL.GL import *

class DirectionalLight:

    def __init__(self, light_colour, ambientIntensity, diffuseIntensity, specularIntensity, direction, shininess):
        self.light_colour = light_colour
        self.ambientIntensity = ambientIntensity
        self.diffuseIntensity = diffuseIntensity
        self.specularIntensity = specularIntensity
        self.direction = direction
        self.shininess = shininess

    def use_light(self, shader):
        light_loc = glGetUniformLocation(shader.get_program(), "colour_light")

        ambientIntensity_loc = glGetUniformLocation(shader.get_program(), "ambientIntensity")
        diffuseIntensity_loc = glGetUniformLocation(shader.get_program(), "diffuseIntensity")
        specularIntensity_loc = glGetUniformLocation(shader.get_program(), "specularIntensity")

        direction_loc = glGetUniformLocation(shader.get_program(), "direction")
        shininess_loc = glGetUniformLocation(shader.get_program(), "shininess")

        glProgramUniform3f(shader.get_program(), light_loc, self.light_colour.x, self.light_colour.y, self.light_colour.z)
        glProgramUniform3f(shader.get_program(), ambientIntensity_loc, self.ambientIntensity.x, self.ambientIntensity.y, self.ambientIntensity.z)
        glProgramUniform3f(shader.get_program(), diffuseIntensity_loc, self.diffuseIntensity.x, self.diffuseIntensity.y, self.diffuseIntensity.z)
        glProgramUniform3f(shader.get_program(), specularIntensity_loc, self.specularIntensity.x, self.specularIntensity.y, self.specularIntensity.z)
        glProgramUniform3f(shader.get_program(), direction_loc, self.direction.x, self.direction.y, self.direction.z)
        glProgramUniform1f(shader.get_program(), shininess_loc, self.shininess)

