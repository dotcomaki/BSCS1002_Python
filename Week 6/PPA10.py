'''
Question's too long
'''

def group_by_city(scores_dataset):
    cities = dict()
    for student in scores_dataset:
        name, city = student['Name'], student['City']
        if city not in cities:
            cities[city] = [ ]
        cities[city].append(name)
    return cities
    
def busy_cities(scores_dataset):
    cities = group_by_city(scores_dataset)
    busy, busy_count = [ ], 0
    for city, from_city in cities.items():
        if len(from_city) > busy_count:
            busy, busy_count = [city], len(from_city)
        elif len(from_city) == busy_count:
            busy.append(city)
    return busy
