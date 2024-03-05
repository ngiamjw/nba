teams = {}
file_path = "warriordata.csv"

with open(file_path, 'r') as data:
    for lines in data:
        line = lines.strip()
        split_line = line.split(',')
        teams[split_line[6]] = teams.get(split_line[6], {'times played' : 0, 'W' : 0, 'L': 0, 'W/L' : 0, 'average margin':[]})
        teams[split_line[6]]['times played'] = teams.get(split_line[6]).get('times played') + 1
        if split_line[7] == 'W':
            teams[split_line[6]]['W'] = teams.get(split_line[6]).get('W') + 1
        else:
            teams[split_line[6]]['L'] = teams.get(split_line[6]).get('L') + 1
        try:
            ratio = teams[split_line[6]]['W']/teams[split_line[6]]['L']
            teams[split_line[6]]['W/L'] = round(ratio, 2)
        except:
            if teams[split_line[6]]['W'] == 0:
                teams[split_line[6]]['W/L'] = 0
            else:
                teams[split_line[6]]['W/L'] = 100
        average_margin = teams[split_line[6]]['average margin']
        average_margin.append(float(split_line[9])-float(split_line[10]))
with open(file_path, 'w') as data:
    for team in teams:
        data.write(f"{team} : {teams[team]}\n")

        



        
