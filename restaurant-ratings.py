def alpha_restaurant_ratings(filename):
    """Sorts restaurant names by alphabetical order, includes restaurant rating."""

    restaurant_data = open(filename)

    restaurant_names_ratings = []
    restaurant_guide = {}

    for restaurant_info in restaurant_data:
        restaurant_info = restaurant_info.rstrip()
        restaurant_info = restaurant_info.split(':')
        restaurant_names_ratings.append(restaurant_info)

    for name_rating in restaurant_names_ratings:
        restaurant_guide[name_rating[0]] = name_rating[1]
    print restaurant_guide












alpha_restaurant_ratings("scores.txt")    