cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    jeep_list = cars['Jeep']
    jeep_string = ', '.join(jeep_list)
    return jeep_string


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    first_list = []
    for k, v in cars.items():
        f = v[0]
        first_list.append(f)
    return first_list


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    match_list = []
    for k, v in cars.items():
        for i in v:
            if grep.lower() in i.lower():
                match_list.append(i)
    match_list.sort()
    return match_list


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    cars_copy = cars.copy()
    for v in cars_copy.values():
        v.sort()
    return cars_copy
