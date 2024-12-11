import re
import json
import subprocess

def validate_group_name(group_name):
  """Validates the group name."""
  if not isinstance(group_name, str) or not group_name.strip():
    print("Invalid group name. Please enter a valid text.")
    return False
  return True

def validate_group_tin(group_tin):
  """Validates the group TIN."""
  if not re.match(r"^\d{9}$", group_tin):
    print("Invalid group TIN. Please enter a 9-digit number.")
    return False
  return True

def validate_practitioner_name(practitioner_name):
  """Validates the practitioner name."""
  if not isinstance(practitioner_name, str) or not practitioner_name.strip():
    print("Invalid practitioner name. Please enter a valid text.")
    return False
  if not re.match(r"^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$", practitioner_name):
    print("Invalid practitioner name. Please enter a valid name.")
    return False
  return True

def validate_practitioner_npi(practitioner_npi):
  """Validates the practitioner NPI."""
  if not re.match(r"^\d{10}$", practitioner_npi):
    print("Invalid practitioner NPI. Please enter a 10-digit number.")
    return False
  return True

def validate_credentials(credentials):
  """Validates the credentials."""
  if not credentials:
    print("Credentials cannot be empty. Please enter the credentials.")
    return False
  return True


def main():
  """Collects input, validates it, and formats the output."""

  data = []

  # Get and validate group name and TIN
  while True:
    group_name = input("Enter group name: ")
    if validate_group_name(group_name):
      break

  while True:
    group_tin = input("Enter group TIN (9 digits): ")
    if validate_group_tin(group_tin):
      break

  while True:
    # Get and validate practitioner name
    while True:
      practitioner_name = input("Enter practitioner name: ")
      if validate_practitioner_name(practitioner_name):
        break

    # Get and validate practitioner NPI
    while True:
      practitioner_npi = input("Enter practitioner NPI (10 digits): ")
      if validate_practitioner_npi(practitioner_npi):
        break

    # Get and validate credentials
    while True:
      credentials = input("Enter practitioner credentials: ")
      if validate_credentials(credentials):
        break

    data.append({
        "group_name": group_name,
        "group_tin": group_tin,
        "practitioner_name": practitioner_name,
        "practitioner_npi": practitioner_npi,
        "practitioner_contract_agreement_id": "",
        "practitioner_contract_effective_date": "",
        "practitioner_contract_termination_date": "",
        "credentials": credentials
    })

    another_entry = input("Add another entry? (y/n): ")
    if another_entry.lower() != 'y':
      break

  final_text = "--lob ma --ignore_bypass --create_entity_if_not_exists --local --data '{}'".format(json.dumps(data))

  process = subprocess.Popen(
      "pbcopy", env={"LANG": "en_US.UTF-8"}, stdin=subprocess.PIPE
  )
  process.communicate(final_text.encode("utf-8"))
  print("Formatted string copied to clipboard!")

  print(final_text)

if __name__ == "__main__":
  main()