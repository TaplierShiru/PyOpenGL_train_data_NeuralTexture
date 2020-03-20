#version 130
in vec2 newTexture;
in vec3 fragNormal;
in vec3 FragPos;

out vec4 outColor;
uniform sampler2D samplerTexture;
uniform vec3 eyePosition;

uniform vec3 colour_light;
uniform vec3 ambientIntensity;
uniform vec3 diffuseIntensity;
uniform vec3 specularIntensity;
uniform vec3 direction;
uniform float shininess;

vec4 CalcLightByDirection(){

	vec4 ambientColour = vec4(colour_light * ambientIntensity, 1.0f);

	float diffuseFactor = max(dot(normalize(fragNormal), normalize(direction)), 0.0f);

	vec4 diffuseColour = vec4(colour_light * diffuseIntensity * diffuseFactor , 1.0f);

	vec4 specularColour = vec4(0, 0, 0, 0);

	if (diffuseFactor > 0.0f)
	{
		vec3 fragToEye = normalize(eyePosition - FragPos);
		vec3 reflectedVertex = normalize(reflect(direction, normalize(fragNormal)));

		float specularFactor = dot(fragToEye, reflectedVertex);

		if (specularFactor > 0.0f)
		{
			specularFactor = pow(specularFactor, shininess);
			specularColour = vec4(colour_light * specularIntensity * specularFactor, 1.0f);
		}

	}

	return ambientColour + diffuseColour + specularColour;
}


void main()
{
    vec4 finalColour = CalcLightByDirection();

    outColor = texture(samplerTexture, newTexture) * finalColour;
}