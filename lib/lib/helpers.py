def get_user_input(prompt):
  """Gets user input with a prompt."""
  while True:
    value = input(prompt)
    if value.strip():
      return value
    else:
      print("Please enter a value.")

def get_integer_input(prompt, min_value=None, max_value=None):
  """Gets integer input with validation."""
  while True:
    try:
      value = int(get_user_input(prompt))
      if min_value is not None and value < min_value:
        print(f"Error: Please enter a value greater than or equal to {min_value}.")
      elif max_value is not None and value > max_value:
        print(f"Error: Please enter a value less than or equal to {max_value}.")
      else:
        return value
    except ValueError:
      print("Error: Please enter a valid integer.")

def get_yes_no_confirmation(prompt):
  """Gets yes/no confirmation from the user."""
  while True:
    response = get_user_input(f"{prompt} (y/n): ").lower().strip()
    if response in ("y", "yes"):
      return True
    elif response in ("n", "no"):
      return False
    else:
      print("Please enter 'y' or 'n'.")

# Additional helper functions for data validation
def is_valid_name(name):
  """Checks if the name string is valid (alphanumeric with spaces)."""
  return name.isalnum() or name.isspace()

def is_valid_price(price):
  """Checks if the price is a positive integer."""
  return isinstance(price, int) and price > 0

def is_valid_commission_rate(rate):
  """Checks if the commission rate is an integer between 1 and 100."""
  return isinstance(rate, int) and 1 <= rate <= 100
