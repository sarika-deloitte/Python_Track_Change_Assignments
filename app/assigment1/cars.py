# Question 7: Mr. Tony is planning to acquire a cars company. He wants to understand if the business would be profitable to him or not. For the same, he needs to process some data to get a better understanding of the company. Given the cars data in dictionary, write a program and help Mr. Tony to:
# 1. Get list of all jeeps
# 2. Get the first car of every manufacturer
# 3. Get all vehicles containing the string “Trail” in their names
# 4. Sort the models(values) alphabetically
# File path for question in repo: app/assignment1/cars.py
# Input:
# cars = { 'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'], 'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'], 'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'], 'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'], 'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk'] }

def get_jeeps(cars_dict):
    return cars_dict.get('Jeep', [])

def get_first_car_of_each_manufacturer(cars_dict):
    return [models[0] for models in cars_dict.values()]

def get_all_vehicles_containing_trail(cars_dict):
    return [model for models in cars_dict.values() for model in models if 'Trail' in model]

def sort_models_alphabetically(cars_dict):
    for manufacturer in cars_dict:
        cars_dict[manufacturer].sort()
    return cars_dict

# Example usage
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
print(get_jeeps(cars)) # Output: ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
print(get_first_car_of_each_manufacturer(cars)) # Output: ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
print(get_all_vehicles_containing_trail(cars)) # Output: ['Trailblazer', 'Trailhawk']
print(sort_models_alphabetically(cars))
# Output: {'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
# 'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
# 'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
# 'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
# 'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk']}
