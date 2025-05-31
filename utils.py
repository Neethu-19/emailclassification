import re

def mask_pii(email_body):
    masked_email = email_body
    offset = 0 # To adjust positions in the masked string

    pii_patterns = {
        'full_name': r'[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+', # Basic pattern for names with at least two words
        'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        'phone_number': r'\+?\d{1,3}[-\s]?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}', # Basic international/national format
        'dob': r'\d{1,2}/\d{1,2}/\d{2,4}', # MM/DD/YY or MM/DD/YYYY or DD/MM/YY etc.
        'aadhar_num': r'\d{12}', # Assuming 12 digits
        'credit_debit_no': r'\d{13,19}', # Assuming 13-19 digits
        'cvv_no': r'\d{3,4}', # Assuming 3 or 4 digits
        'expiry_no': r'\d{2}/\d{2}', # Assuming MM/YY
    }

    # Find all matches and sort by start index
    matches = []
    for entity_type, pattern in pii_patterns.items():
        for match in re.finditer(pattern, email_body):
            matches.append({
                'start': match.start(),
                'end': match.end(),
                'entity': match.group(0),
                'classification': entity_type
            })
    matches.sort(key=lambda x: x['start'])

    # Build the masked email and collect the original entities by type
    current_index_original = 0
    masked_email_parts = []
    entities_by_type = {}

    for match in matches:
        start_original, end_original = match['start'], match['end']
        original_entity = match['entity']
        entity_type = match['classification']

        # Add the text before the current match
        masked_email_parts.append(email_body[current_index_original:start_original])

        # Add the masked placeholder
        placeholder = f'[{entity_type}]'
        masked_email_parts.append(placeholder)

        # Collect the original entity under its type
        if entity_type not in entities_by_type:
            entities_by_type[entity_type] = []
        entities_by_type[entity_type].append(original_entity)

        # Update current index in the original email
        current_index_original = end_original

    # Add any remaining text after the last match
    masked_email_parts.append(email_body[current_index_original:])

    final_masked_email = "".join(masked_email_parts)

    # Return the masked email and the dictionary of entities
    return final_masked_email, entities_by_type

# Demasking is not needed as per the output format, which includes the original email body.
# However, if demasking *were* needed, having the original email body makes it simple.
# Let's keep a placeholder demask function for completeness, though it won't be used in the API response.

def demask_pii(original_email_body, masked_entities): # This function is not strictly needed based on API output format
    demasked_email = list(original_email_body)
    # Sort entities by original position in reverse order
    masked_entities.sort(key=lambda x: x['position'][0], reverse=True)

    for entity_info in masked_entities:
        original_start, original_end = entity_info['position'] # These are original positions
        original_entity = entity_info['entity']

        # This demasking logic based on manipulating a list of characters is complex and error-prone
        # if the positions stored are from the *masked* string. Since we are storing original positions,
        # we can conceptually see how it *would* work, but it's not needed for the API.
        pass # Not implementing complex demasking as the API provides the original email.

# Let's add a basic example usage for testing.
if __name__ == '__main__':
    test_email = "Hello, my name is John Doe, and my email is johndoe@example.com. My phone number is +1-555-123-4567 and my DOB is 12/25/1990. My Aadhar number is 123456789012. My credit card is 1234567890123456, CVV 123, expiry 12/24."
    masked_email, masked_entities = mask_pii(test_email)
    print("Original Email:", test_email)
    print("Masked Email:", masked_email)
    print("Masked Entities:", masked_entities) 