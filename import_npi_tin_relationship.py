import re
import json

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

    # Ask if CA or CPH will be used
    while True:
        ca_or_cph = input("Will you be using CA or CPH? (ca/cph): ").lower()
        if ca_or_cph not in ('ca', 'cph'):
            print("Invalid input. Please enter 'ca' or 'cph'.")
        else:
            break

    # Get and validate group name and TIN
    while True:
        group_name = input("Enter group name: ")
        if validate_group_name(group_name):
            break

    while True:
        group_tin = input("Enter group TIN (9 digits): ")
        if validate_group_tin(group_tin):
            break

    tenant = ""
    lob = ""
    source_ehr = ""
    ehr_username = ""
    ehr_instance_external_id = ""

    if ca_or_cph == 'cph':
        # Get the --tenant value
        tenant = input("Enter the --tenant value: ")

        # Get the --lob value
        lob = input("Enter the --lob value: ")

        # Get optional CPH fields
        source_ehr = input("Enter source EHR (optional): ")
        ehr_username = input("Enter EHR username (optional): ")
        ehr_instance_external_id = input("Enter EHR instance external ID (optional): ")

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

        practitioner_data = {
            "group_name": group_name,
            "group_tin": group_tin,
            "practitioner_name": practitioner_name,
            "practitioner_npi": practitioner_npi,
            "practitioner_contract_agreement_id": "",
            "practitioner_contract_effective_date": "",
            "practitioner_contract_termination_date": "",
            "credentials": credentials
        }

        if ca_or_cph == 'cph':  # Add optional CPH fields to data if CPH is selected
            practitioner_data["source_ehr"] = source_ehr
            practitioner_data["ehr_username"] = ehr_username
            practitioner_data["ehr_instance_external_id"] = ehr_instance_external_id

        data.append(practitioner_data)  # Append the practitioner_data dictionary to the data list

        another_entry = input("Add another entry? (y/n): ")
        if another_entry.lower() != 'y':
            break

    if ca_or_cph == 'cph':
        final_text = f"--tenant {tenant} --lob {lob} --ignore_bypass --create_entity_if_not_exists --local --data '{json.dumps(data)}'"
    else:
        final_text = f"--ignore_bypass --create_entity_if_not_exists --local --data '{json.dumps(data)}'"

    print(final_text)

if __name__ == "__main__":
    main()