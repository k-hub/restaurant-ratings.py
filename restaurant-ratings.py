def alpha_restaurant_ratings(filename):
    """Sorts restaurant names by alphabetical order, includes restaurant rating."""

    restaurant_data = open(filename)

    restaurant_names_ratings = []
    restaurant_guide = {}

    # Get restaurant name and rating as a list and appending to restaurant_names_ratings.  
    for restaurant_info in restaurant_data:
        restaurant_info = restaurant_info.rstrip()
        restaurant_info = restaurant_info.split(':')
        restaurant_names_ratings.append(restaurant_info)

    for name_rating in restaurant_names_ratings:
        restaurant_name = name_rating[0]
        restaurant_rating = name_rating[1]
        restaurant_guide[restaurant_name] = restaurant_rating  # Add restaurant_name : restaurant_rating pairs to dictionary.

    for restaurant_name, restaurant_rating in sorted(restaurant_guide.items()):
        print "{} is rated at {}.".format(restaurant_name, restaurant_rating)

    restaurant_data.close()

alpha_restaurant_ratings("scores.txt")