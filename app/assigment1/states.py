# Question 9: You are presented with  a us_state_abbrev dict and a states list. Complete these four methods  : 
# File path for question in repo: app/assignment1/states.py
# get_every_nth_state -> Return a list with every nth item (default argument n=10, so every  10th item) of the states list above (remember: lists keep order)
# get_state_abbrev -> Look up a state abbreviation by querying the us_state_abbrev  dict by full state name, for instance 'Alabama' returns 'AL', 'Illinois' returns 'IL'. If the state is not in the dict, return 'N/A' which we stored   in the NOT_FOUND constant (takeaway: dicts are great for lookups)
# get_longest_state -> Receives data, which can be the us_state_abbrev dict or the states  list . It returns the longest state measured by the length of the string
# combine_state_names_and_abbreviations -> Get the first 10 state abbreviations ('AL', 'AK', 'AZ', ...) from  the us_state_abbrev dict, and the last 10 states from the states list and combine them into a new list without losing alphabetical order

# Note: us_state_abbrev dict and a states list both these datas are provided app/assignment1/states.py file

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

states = [
    'Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon', 'Mississippi',
    'Minnesota', 'Colorado', 'Alabama', 'Massachusetts', 'Arizona',
    'Connecticut', 'Montana', 'West Virginia', 'Nebraska', 'New York',
    'Nevada', 'Idaho', 'New Jersey', 'Missouri', 'South Carolina',
    'Pennsylvania', 'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
    'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky', 'Virginia',
    'Ohio', 'Wisconsin', 'Maryland', 'Florida', 'Utah', 'Maine', 'California',
    'Vermont', 'Arkansas', 'Wyoming', 'Louisiana', 'North Dakota',
    'South Dakota', 'Texas', 'Illinois', 'Iowa', 'Michigan', 'Delaware'
]

NOT_FOUND = 'N/A'

def get_every_nth_state(states, n=10):
    """Return a list with every nth item (default argument n=10) of the states list."""
    return states[n-1::n]

def get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev):
    """Look up a state abbreviation by querying the us_state_abbrev dict by full state name."""
    return us_state_abbrev.get(state_name, NOT_FOUND)

def get_longest_state(data):
    """Receives data, which can be the us_state_abbrev dict or the states list.
    It returns the longest state measured by the length of the string."""
    if isinstance(data, dict):
        data = data.keys()
    return max(data, key=len)

def combine_state_names_and_abbreviations(us_state_abbrev=us_state_abbrev, states=states):
    """Get the first 10 state abbreviations from the us_state_abbrev dict,
    and the last 10 states from the states list and combine them into a new list without losing alphabetical order."""
    first_10_abbrevs = sorted(list(us_state_abbrev.values()))[:10]
    last_10_states = sorted(states)[-10:]
    return first_10_abbrevs + last_10_states

# Example usage
if __name__ == "__main__":
    print(get_every_nth_state(states))  # Example output: ['Massachusetts', 'Missouri', 'Hawaii', 'Arkansas', 'Michigan']
    print(get_state_abbrev('Alabama'))  # Example output: 'AL'
    print(get_state_abbrev('Unknown'))  # Example output: 'N/A'
    print(get_longest_state(states))    # Example output: 'North Carolina'
    print(get_longest_state(us_state_abbrev))  # Example output: 'North Carolina'
    print(combine_state_names_and_abbreviations())  # Example output: ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']