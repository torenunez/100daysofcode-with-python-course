NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return list(set([name.title() for name in names]))


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    last_name_tuple = [(name.split()[1], name) for name in names]
    sorted_last_name_tuple = sorted(last_name_tuple, key=lambda tuple_name: tuple_name[0], reverse=True)
    sorted_names = [tuple_name[1].title() for tuple_name in sorted_last_name_tuple]
    return sorted_names


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    first_length_list = [(len(name.split()[0]), name.split()[0]) for name in names]
    sorted_shortest_first_tuple = sorted(first_length_list, key=lambda tuple_name: tuple_name[0])
    shortest_name = sorted_shortest_first_tuple[0][1].title()
    return shortest_name