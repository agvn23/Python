### Destination City ###

# array = paths find final city (the one with no departures 1 flight)
# example 1
#input: paths = [['London', 'New York'], ['New York', 'Lima'], ['Lima', 'sao Paulo']]
#output
paths = [['London', 'New York'], ['New York', 'Lima'], ['Lima', 'Sao Paulo']]
#1 Solution O(n°)  
# def destination(paths):
#     for i in range(0, len(paths)):
#         for j in range(i + 1, len(paths)):
#             if [i][1]!=[j][0]:
#                 print([1])
def destination_city(paths):
    for i in range(len(paths)):
        possible_final_city = paths[i][1]          # checking new york
        for j in range(len(paths)):                # Not + 1 cos we want to check all 
            if paths[j][0] == possible_final_city: # against 1st city in each nested array
                break                              # if yes break loop
        else:                                      # if no match then that city must be final city 
            return possible_final_city
    return ''                                      # Encase we never find city             
print(destination_city(paths))
              
#2nd Solution O(n) Faster

# for i in range(0, len(paths)):
#     for j in range(i + 1, len(paths)):
#         #if [i][1]!=[j][0]:
#         print(paths[j][1])
def desination_city_2(paths):
    outgoing_cities = set()                        # create empty set not {} but set()

    for i in range(len(paths)):
        # outgoing_city = paths[i][0]
        # outgoing_cities.add(outgoing_city)
        outgoing_cities.add(paths[i][0])          # check set London, New York, Lima

    for i in range (len(paths)):
        possible_final_city = paths[i][1]         # against 2nd city in each nested array
        if possible_final_city not in outgoing_cities:
            return possible_final_city            # if not then that city must be final city

    return ''                                     # anser should remain str None is bool
print(desination_city_2(paths))