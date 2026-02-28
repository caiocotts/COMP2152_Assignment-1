"""
Author: Caio dos Santos Cotts Quintao
Assignment: #1
"""
import sys
import re

# Step b: Create 4 variables
gym_member = 'Alex Alliton'
preferred_weight_kg = 20.5
highest_reps = 25
membership_active = True

# Step c: Create a dictionary named workout_stats
workout_stats = {
    #        yoga, running, weightlifting
    'jade': (10, 32, 23),
    'ash': (30, 43, 53),
    'cody': (43, 17, 30),
    'caleb': (54, 30, 43)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
[workout_stats.update({f'{name}_Total': sum(times)}) for name, times in list(workout_stats.items())]

# Step e: Create a 2D nested list called workout_list
workout_list = []
[workout_list.append([name, *times]) for name, times in workout_stats.items() if 'Total' not in name]

# Step f: Slice the workout_list
print('yoga and weightlifting times for all friends:')
[print(f"[{times[1]}, {times[-1]}]") for times in workout_list]
print('weightlifting times for the last two friends:')
[print(times[-1]) for times in workout_list[-2:]]

# Step g: Check if any friend's total >= 120
[print(f'Great job staying active, {times[0]}!') for times in workout_list if sum(times[1:]) > 120]

# Step h: User input to look up a friend
inp = input("enter a friend's name to see their workout stats: ").lower()
if inp not in workout_stats:
    print(f'friend "{inp}" not found in the records')
else:
    workout_names = ['Yoga', 'Running', 'Weight Lifting']
    i = 0
    print(f'workout stats for {inp}')
    for time in workout_stats[inp]:
        print(f'\t{workout_names[i]}: {time}')
        i += 1

# Step i: Friend with highest and lowest total workout minutes

friend_with_least_time = ''
friend_with_most_time = ''
least_time = sys.maxsize
most_time = -sys.maxsize - 1

for name, total in list(workout_stats.items()):
    if 'Total' in name:
        if total > most_time:
            friend_with_most_time = re.match(r'^(.+)_Total$', name)[1]
            most_time = total
        if total < least_time:
            friend_with_least_time =  re.match(r'^(.+)_Total$', name)[1]
            least_time = total
print('friend with most workout time:', friend_with_most_time)
print('friend with least workout time:', friend_with_least_time)