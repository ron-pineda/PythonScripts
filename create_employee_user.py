import re
import subprocess

def format_input():
  """
  Collects user input for email, TIN, profile, practice group,
  Okta verification skip, and override existing options.
  Formats the input into a command-line argument string.
  Includes validation for email, TIN, and profile selection.
  Practice group is optional, and an empty value is included in the output.
  Copies the formatted string to the clipboard using pbcopy (macOS).
  """

  while True:
    email = input("Enter your email: ")
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Basic email format check
      break
    else:
      print("Invalid email format. Please try again.")

  while True:
    tin = input("Enter your TIN (9 digits): ")
    if tin.isdigit() and len(tin) == 9:
      break
    else:
      print("Invalid TIN. Please enter exactly 9 digits.")

  print("Select a profile from the following list:")
  profiles = [
      "ACCESS_PROFILE_CSA",
      "ACCESS_PROFILE_CSM",
      "ACCESS_PROFILE_PRODUCT",
      "ACCESS_PROFILE_ENGINEERING",
      "ACCESS_PROFILE_DS_ANALYTICS",
      "ACCESS_PROFILE_TECH_LEAD",
      "ACCESS_PROFILE_QA",
      "ACCESS_PROFILE_PRODUCT_SUCCESS",
      "ACCESS_PROFILE_CLINICAL",
  ]
  for i, profile in enumerate(profiles):
    print(f"{i+1}. {profile}")

  while True:
    try:
      selected_profile_index = (
          int(input("Enter the number of your selected profile: ")) - 1
      )
      if 0 <= selected_profile_index < len(profiles):
        selected_profile = profiles[selected_profile_index]
        break
      else:
        print("Invalid profile selection. Please enter a number from the list.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  practice_group = input("Enter your practice group (optional): ")

  skip_okta_verify = input("Skip Okta verify? (y/n): ").lower() == "y"
  override_existing = input("Override existing? (y/n): ").lower() == "y"

  # Build the formatted string
  formatted_string = (
      f"--email={email} "
      f"--tin={tin} "
      f"--access_profile={selected_profile} "
      f'--practice_group="{practice_group}"'
  )
  if skip_okta_verify:
    formatted_string += " --skip_okta_verify"
  if override_existing:
    formatted_string += " --override_existing"

  print(formatted_string)

  # Copy to clipboard using pbcopy (macOS)
  process = subprocess.Popen(
      "pbcopy", env={"LANG": "en_US.UTF-8"}, stdin=subprocess.PIPE
  )
  process.communicate(formatted_string.encode("utf-8"))
  print("Formatted string copied to clipboard!")

if __name__ == "__main__":
  format_input()