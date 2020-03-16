#version 130
in vec2 newTexture;

out vec4 outColor;
uniform sampler2D samplerTexture;
void main()
{
    // return uv of the Mesh
    outColor = vec4(newTexture, 0, 0);
}

