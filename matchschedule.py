import tbapy
import csv

f = open("tba_api_key.txt", "r")
key = f.read()
tba = tbapy.TBA(key)

doritos = input("Event code: ")

matches = tba.event_matches(doritos, simple=True)

with open('matches.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(['Match', 'Red 1', 'Red 2', 'Red 3', 'Blue 1', 'Blue 2', 'Blue 3'])
    
    for match in matches:
        if match['comp_level'] == 'qm':
            match_num = match['match_number']
            red_alliance = match['alliances']['red']['team_keys']
            blue_alliance = match['alliances']['blue']['team_keys']

            writer.writerow([match_num, red_alliance[0][3:-1],
                             red_alliance[1][3:-1], red_alliance[2][3:-1],
                             blue_alliance[0][3:-1], blue_alliance[1][3:-1],
                             blue_alliance[2][3:-1]])

# match_number
# comp_level: qm
# alliances: blue, red
# blue, red : team_keys: frc### (remove frc)
