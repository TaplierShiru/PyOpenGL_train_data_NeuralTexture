#version 130
in vec2 newTexture;

out vec2 outColor;

uniform sampler2D samplerTexture;
uniform vec3 eyePosition;

void main()
{
    outColor = newTexture;
}