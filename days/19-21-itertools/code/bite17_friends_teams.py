from itertools import combinations, permutations

friends = 'Sal Alba Teo Valeriano Celia Alex Seth Martha Joel Levi Mary Lila Jules Dora Diego Alissa Max Elodie Lucio Claudia'.split()


def friends_teams(friends, team_size=2, order_does_matter=True):

    if order_does_matter:
        return list(permutations(friends, team_size))
    else:
        return list(combinations(friends, team_size))



if __name__ == '__main__':
    friends_teams()