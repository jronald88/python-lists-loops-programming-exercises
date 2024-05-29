celsius_values = [-2, 34, 56, -10]

def celsius_to_fahrenheit(celsius):
    # The magic happens here
   cel_to_far = 1.8 * celsius + 32
   return cel_to_far

result = list(map(celsius_to_fahrenheit, celsius_values)) #maps the c-2-f function to the list c-v

print(result)
