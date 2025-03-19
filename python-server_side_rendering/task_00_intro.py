"""Module containing python script for sending invitations"""
from os.path import exists


def generate_invitations(template, attendees_list):
    """Function for generating invitations"""

    # Check if template is valid
    if not isinstance(template, str):
        print("ERROR: template must be a string")
        return

    # Check if template is empty
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is valid
    if not isinstance(attendees_list, list):
        print("ERROR: attendees_list must be a list of dictionaries")
        return

    # Check if attendees list is empty
    if not attendees_list:
        print("No data provided, no output files generated.")
        return

    # Check if all items in attendees_list are dictionaries
    if not all(isinstance(item, dict) for item in attendees_list):
        print("ERROR: attendees_list must be a list of dictionaries")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees_list, start=1):
        processed_template = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            placeholder = "{" + key + "}"
            value = attendee.get(key) or "N/A"
            processed_template = processed_template.replace(placeholder, value)
        
        output_filename = f"output_{index}.txt"
        if not exists(output_filename):
            with open(output_filename, "w") as file:
                file.write(processed_template)
        else:
            print(f"ERROR: file {output_filename} already exists")