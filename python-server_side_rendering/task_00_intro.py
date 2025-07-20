#!/usr/bin/env python3
""" Creates a simple template program """
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees is not a list")
        return
    
    if attendees and not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees is not a list of dictionaries")
        return
    
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        
        placeholders = ["{name}", "{event_title}", "{event_date}", "{event_location}"]
        placeholder_keys = ["name", "event_title", "event_date", "event_location"]
        
        for placeholder, key in zip(placeholders, placeholder_keys):
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(placeholder, str(value))
        
        output_filename = f"output_{index}.txt"
        
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(invitation)
            print(f"Generated {output_filename}")
        except Exception as e:
            print(f"Error writing {output_filename}: {e}")


if __name__ == "__main__":
    
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        print("Error: template.txt file not found")
        exit(1)
    except Exception as e:
        print(f"Error reading template file: {e}")
        exit(1)
    
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]
    
    generate_invitations(template_content, attendees)
