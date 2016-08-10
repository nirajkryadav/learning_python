def KelvinToFahrenheit(Temperature):
	assert (Temperature >= 0),"bitch ,please temp can't be Colder than absolute zero!"
	return ((Temperature-273)*1.8)+32
print KelvinToFahrenheit(273)
print int(KelvinToFahrenheit(505.78))
print KelvinToFahrenheit(-5)