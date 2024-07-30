def get_profile(name, age, *sports, **awards):
    # Validate that age is an integer
    if not isinstance(age, int):
        raise ValueError("Age must be an integer")
    
    # Validate that no more than 5 sports are provided
    if len(sports) > 5:
        raise ValueError("No more than 5 sports can be provided")
    
    # Create the profile dictionary
    profile = {
        'name': name,
        'age': age
    }
    
    # Add sports to the profile if provided
    if sports:
        profile['sports'] = sorted(sports)
    
    # Add awards to the profile if provided
    if awards:
        profile['awards'] = awards
    
    return profile

# Example usage
print(get_profile('tim', 36))  # Output: {'name': 'tim', 'age': 36}
print(get_profile('tim', 36, 'tennis', 'basketball'))  # Output: {'name': 'tim', 'age': 36, 'sports': ['basketball', 'tennis']}
print(get_profile('tim', 36, 'tennis', 'basketball', champ='helped out team in crisis'))  # Output: {'name': 'tim', 'age': 36, 'sports': ['basketball', 'tennis'], 'awards': {'champ': 'helped out team in crisis'}}
