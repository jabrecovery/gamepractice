

gamers = []
kimberly = {
    'name': 'Kimberly', 
    'availability': ['Monday', 'Tuesday', 'Friday']
}

def add_gamer(gamer, gamers_list):
    if gamer.get('name') and gamer.get('availability'):
        gamers.append(gamer)

add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

print(gamers)

def build_frequency_table():
    return {
        'Monday': 0,
        'Tuesday': 0,
        'Wednesday': 0,
        'Thursday': 0,
        'Friday': 0,
        'Saturday': 0,
        'Sunday': 0
    }

count_availability = build_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1

calculate_availability(gamers, count_availability)
print(count_availability)

def find_best_night(availability_table):
    best_availability = 0
    for day, count in availability_table.items():
        if count > best_availability:
            best_day = day
            best_availability = count
    return best_day

game_night = find_best_night(count_availability)
print(game_night)

def available_on_night(gamers_list, day):
    attendees = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            attendees.append(gamer)
    return attendees

attending_game_night = (available_on_night(gamers, game_night))
print(attending_game_night)

email_string = '''Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
the Sorcery Society'''

def send_email(gamers_who_can_attend, game, day):
    for gamer in gamers_who_can_attend:
        print(email_string.format(name=gamer['name'], game=game, day_of_week=day ))

send_email(attending_game_night, 'Abrubtly Goblins', game_night)

unable_to_attend_best_night = []
for gamer in gamers:
    if gamer not in attending_game_night:
        unable_to_attend_best_night.append(gamer)
print(unable_to_attend_best_night)

second_night_availability = build_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
print(second_night_availability)

game_night_2_option = find_best_night(second_night_availability)
print(game_night_2_option)

send_email(unable_to_attend_best_night, 'Abrubtly Goblins', game_night_2_option)