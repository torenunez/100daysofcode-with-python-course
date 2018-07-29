#!python3

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
    'Wyoming': 'WY',
}


states_list = ['Oklahoma',
               'Kansas',
               'North Carolina',
               'Georgia',
               'Oregon',
               'Mississippi',
               'Minnesota',
               'Colorado',
               'Alabama',
               'Massachusetts',
               'Arizona',
               'Connecticut',
               'Montana',
               'West Virginia',
               'Nebraska',
               'New York',
               'Nevada',
               'Idaho',
               'New Jersey',
               'Missouri',
               'South Carolina',
               'Pennsylvania',
               'Rhode Island',
               'New Mexico',
               'Alaska',
               'New Hampshire',
               'Tennessee',
               'Washington',
               'Indiana',
               'Hawaii',
               'Kentucky',
               'Virginia',
               'Ohio',
               'Wisconsin',
               'Maryland',
               'Florida',
               'Utah',
               'Maine',
               'California',
               'Vermont',
               'Arkansas',
               'Wyoming',
               'Louisiana',
               'North Dakota',
               'South Dakota',
               'Texas',
               'Illinois',
               'Iowa',
               'Michigan',
               'Delaware']

# Print out the 10th item in each.
i = 0
for k, v in us_state_abbrev.items():
    if i == 9:
        print(k, v)
        i += 1
    else:
        i += 1

print(states_list[9])

# Print out the 45th key in the dictionary.
i = 0
for k in us_state_abbrev.keys():
    if i == 44:
        print(k)
        i += 1
    else:
        i += 1


# Print out the 27th value in the dictionary.
i = 0
for v in us_state_abbrev.values():
    if i == 26:
        print(v)
        i += 1
    else:
        i += 1
