capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# print Lille
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]] ## This is a nested list inside a list
print(nested_list[2][1])  ## This statement helps us to do list the letter "D"


travel_log = { ## This are dictionaries insde a dictionaries
    "France": {
    "cities_visited":["Paris", "Lille", "Dijon"],
    "total_visits": 12
    },
    "Germany":{
    "cities_visited":["Stuttgart", "Berlin"],
    "total_visits": 5
    },
}

print(travel_log["Germany"]["cities_visited"][1])


