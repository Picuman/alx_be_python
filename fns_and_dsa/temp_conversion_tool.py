FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
  """
  This function converts a temperature from Fahrenheit to Celsius.
  """
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  """
  This function converts a temperature from Celsius to Fahrenheit.
  """
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
  """
  This function handles user interaction and temperature conversion.
  """
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
      if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        unit = 'F'
      elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        unit = 'C'
      else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
      print(f"{temperature:.1f}°{unit} is {converted_temp:.2f}°C" if unit == 'F' else f"{temperature:.1f}°{unit} is {converted_temp:.2f}°F")
      break
    except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()
