#Python program to convert the temperature in degree centigrade to Fahrenheit

def celsius_to_fahrenheit(celsius):
 fahrenheit = (celsius * 9/5) + 32
 return fahrenheit
celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")


#25°C is equal to 77.0°F
