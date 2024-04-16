import tbapy
import csv

f = open("tba_api_key.txt", "r")
key = f.read()
tba = tbapy.TBA(key)

event = input("Event code: ")

matches = tba.event_matches(event, simple=True)
teams = tba.event_teams(event)

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

with open('teams.csv', 'w', newline='', encoding='utf-8') as csvfile2:
    writer = csv.writer(csvfile2, delimiter=',')
    writer.writerow(['Team Number', 'Team Name', 'Image URL'])
    for team in teams:
        team_key = team['key']
        team_num = team['key'][3:]
        image=""
        if len(tba.team_media(team_key, 2024)) > 1:
            image=tba.team_media(team_key, 2024)[1]['direct_url']
        writer.writerow([team_num, team['nickname'], image])




# for team in teams:
#     print(team['nickname'])

# print(tba.team_media(4028, 2024)[1]['direct_url'])