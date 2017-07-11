["cow", "dog", "cat"]
{1: "cow", 2: "dog", 3: "cat"}

"Your int is in range 0-10"

if 1 in range(0, 2):
    print("hej")


def travel(departure, destination, duration, overnight):
    return {
        "departure": departure,
        "destination": destination,
        "duration": duration,
        "overnight": overnight
    }

{'departure': 'sthlm', 'destination': 'oslo', 'duration': 10, 'overnight': True}

['sthlm', 'oslo', 'copenhagen', 'krakow']
list_of_plans = ['sthlm', 10, True, 'oslo', 11, True, 'copenhagen', 15, False, 'krakow']

def produce_travel_structure(list_of_plans):
    list_of_dicts = []
    for i in range(0, len(list_of_plans) - 1, 3):
        list_of_dicts.append(
            travel(list_of_plans[i], list_of_plans[i + 3], list_of_plans[i + 1], list_of_plans[i + 2])
        )
    return list_of_dicts

[{'departure': 'sthlm', 'destination': 'oslo', 'duration': 10, 'overnight': True}, {'departure': 'oslo', 'destination': 'copenhagen', 'duration': 11, 'overnight': True}, {'departure': 'copenhagen', 'destination': 'krakow', 'duration': 15, 'overnight': False}]

print(produce_travel_structure(list_of_plans))

def sum_the_trip(list_of_dicts):
    sum_of_hours = 0
    for d in list_of_dicts:
        sum_of_hours += d["duration"]
        if d["overnight"]:
            sum_of_hours += 10
    return sum_of_hours

print(sum_the_trip([{'departure': 'sthlm', 'destination': 'oslo', 'duration': 10, 'overnight': True}, {'departure': 'oslo', 'destination': 'copenhagen', 'duration': 11, 'overnight': True}, {'departure': 'copenhagen', 'destination': 'krakow', 'duration': 15, 'overnight': False}]))

def show_the_trip(list_of_dicts):
    string_to_print = ""
    for d in list_of_dicts:
        if d["overnight"]:
            duration = str(d["duration"] + 10) + " hours including sleep"
        else:
            duration = str(d["duration"]) + " hours"
        string_to_print += d["departure"] + " -> " + d["destination"] + ", will take: " + duration + " ->\n"
    string_to_print += "The whole trip will take: " + str(sum_the_trip(list_of_dicts))
    return string_to_print

print(show_the_trip([{'departure': 'sthlm', 'destination': 'oslo', 'duration': 10, 'overnight': True}, {'departure': 'oslo', 'destination': 'copenhagen', 'duration': 11, 'overnight': True}, {'departure': 'copenhagen', 'destination': 'krakow', 'duration': 15, 'overnight': False}]))
