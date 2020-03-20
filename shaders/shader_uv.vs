#version 130
in vec3 position;
in vec2 textureCoords;
in vec3 vertNormal;

uniform mat4 view;
uniform mat4 inverse_model;
uniform mat4 model;
uniform mat4 projection;

out vec2 newTexture;

void main()
{
    newTexture = textureCoords;
    gl_Position = projection * view * model * vec4(position, 1.0f);
}