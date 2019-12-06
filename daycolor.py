list_of_days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]
day_to_color_map = dict()
color_to_day_map = dict()

for day in list_of_days:
    color_for_the_day = input(f"Enter a color for {day}: ")
    day_to_color_map[day] = color_for_the_day
    
    color_to_day_map.setdefault(color_for_the_day, [])
    color_to_day_map[color_for_the_day].append(day)

print("*****Generating Output*****")
for key, value in color_to_day_map.items():
    print(f"{key}: {len(value)}, {value}")
