#!/usr/bin/env python3
"""
Test file to verify error handling in the templating program
"""

from task_00_intro import generate_invitations

print("Testing error handling scenarios:\n")

# Test 1: Invalid template type (not a string)
print("Test 1: Template is not a string")
generate_invitations(123, [{"name": "Alice"}])
print()

# Test 2: Invalid attendees type (not a list)
print("Test 2: Attendees is not a list")
generate_invitations("Hello {name}", "not a list")
print()

# Test 3: Attendees is not a list of dictionaries
print("Test 3: Attendees is not a list of dictionaries")
generate_invitations("Hello {name}", ["string", 123])
print()

# Test 4: Empty template
print("Test 4: Empty template")
generate_invitations("", [{"name": "Alice"}])
print()

# Test 5: Template with only whitespace
print("Test 5: Template with only whitespace")
generate_invitations("   \n\t  ", [{"name": "Alice"}])
print()

# Test 6: Empty attendees list
print("Test 6: Empty attendees list")
generate_invitations("Hello {name}", [])
print()

# Test 7: Normal operation with missing data
print("Test 7: Normal operation with missing data")
attendees_with_missing_data = [
    {"name": "David"},  # Missing event_title, event_date, event_location
    {"event_title": "Conference"},  # Missing name, event_date, event_location
]
generate_invitations("Hello {name}, {event_title} on {event_date} at {event_location}", attendees_with_missing_data)
print()

print("All tests completed!")
