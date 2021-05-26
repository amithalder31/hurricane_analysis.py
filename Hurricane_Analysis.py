# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
new_damages = []
def update_damages(damage):
    dam = []
    conversion = {"M": 1000000,
              "B": 1000000000}

    for record in damage:
        if record[-1] == "M":
            conv = conversion["M"]
            new_data = float(record[:-1]) * float(conv)
           #print(new_data)
        elif record[-1] == "B":
            conv = conversion["B"]
            new_data = float(record[:-1]) * float(conv)
            #print(new_data)
        else:
            new_data = record
            #print(new_data)
        dam.append(new_data)
    return dam
    
new_damages = update_damages(damages)
print(new_damages)

# write your construct hurricane dictionary function here:
def hurricane_data (name, month, year, max_sustained_wind, area_affected, damage, death):
    hurricane_dict = {}
    len_of_name = len(name)
    i = 0
    for i in range(len_of_name):
        hurricane_dict[names[i]] = {"Name": name[i], "Month": month[i], "Year": year[i], "Max Sustained Wind": max_sustained_wind[i], "Areas Affected": area_affected[i], "Damage": damage[i], "Death": death[i]}
        #new_dict.update(hurricane_dict)
    return hurricane_dict

hurricane = hurricane_data(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)
print(hurricane)
# write your construct hurricane by year dictionary function here:
def hurricane_by_year_dictionary (hurricane_dict):
    hurricane_year_dict = {}
    for i in hurricane_dict:
        current_year = hurricane_dict[i]["Year"]
        current_cane = hurricane_dict[i]
        if current_year not in hurricane_year_dict:
            hurricane_year_dict[current_year] = [current_cane]
        else:
            hurricane_year_dict[current_year].append(current_cane)
    return hurricane_year_dict

hu_by_year = hurricane_by_year_dictionary(hurricane)
print(hu_by_year)

# write your count affected areas function here:

def count_affected_area (hurricane_dict_area):
    hurricane_area_dict_count = {}
    for value in hurricane_dict_area.values():
        for area in value["Areas Affected"]:
            if area not in hurricane_area_dict_count:
                hurricane_area_dict_count[area] = 1
            else:
                hurricane_area_dict_count[area] += 1
                continue
    return hurricane_area_dict_count

print(count_affected_area(hurricane))

# write your find most affected area function here:

affected_area_count = count_affected_area(hurricane)

def most_affected_area(most_affected_area_count):
    most_affected = {}
    count = 0
    for k, v in most_affected_area_count.items():
        if v > count:
            most_affected[k] = v
            count = v
    return most_affected

print(most_affected_area(affected_area_count))


# write your greatest number of deaths function here:
def greatest_number_deaths(data):
    max_death = ""
    count = 0
    for i in data:
        if data[i]["Death"] > count:
            max_death = i
            count = data[i]["Death"]
    return max_death, count
print(greatest_number_deaths(hurricane))

# write your catgeorize by mortality function here:
def hurricanes_mortality(hurricanes_dict_mortality):
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    mortality_scale = {0: 0,
                    1: 100,
                    2: 500,
                    3: 1000,
                    4: 10000}

    for i in hurricanes_dict_mortality:
        if hurricanes_dict_mortality[i]["Death"] == mortality_scale[0]:
            hurricanes_by_mortality[0].append(hurricanes_dict_mortality[i]["Name"])
        elif mortality_scale[0] < hurricanes_dict_mortality[i]["Death"] <= mortality_scale[1]:
            hurricanes_by_mortality[1].append(hurricanes_dict_mortality[i]["Name"])
        elif mortality_scale[1] < hurricanes_dict_mortality[i]["Death"] <= mortality_scale[2]:
            hurricanes_by_mortality[2].append(hurricanes_dict_mortality[i]["Name"])
        elif mortality_scale[2] < hurricanes_dict_mortality[i]["Death"] <= mortality_scale[3]:
            hurricanes_by_mortality[3].append(hurricanes_dict_mortality[i]["Name"])
        elif mortality_scale[3] < hurricanes_dict_mortality[i]["Death"] <= mortality_scale[4]:
            hurricanes_by_mortality[4].append(hurricanes_dict_mortality[i]["Name"])
        else:
            hurricanes_by_mortality[5].append(hurricanes_dict_mortality[i]["Name"])
    return hurricanes_by_mortality
print(hurricanes_mortality(hurricane))


# write your greatest damage function here:
def hurricane_greatest_damage(data_from_dict):
    greatest_damage = ""
    count = 0
    for i in data_from_dict:
        if data_from_dict[i]["Damage"] == "Damages not recorded":
            pass
        elif data_from_dict[i]["Damage"] > count:
            greatest_damage = i
            count = data_from_dict[i]["Damage"]
    return greatest_damage, count
print(hurricane_greatest_damage(hurricane))


# write your catgeorize by damage function here:
def hurricanes_rating_damage(data_from_dict):
    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

    for i in data_from_dict:
        if data_from_dict[i]["Damage"] == "Damages not recorded":
            hurricanes_by_damage[0].append(data_from_dict[i]["Name"])
        elif damage_scale[0] < data_from_dict[i]["Damage"] <= damage_scale[1]:
            hurricanes_by_damage[1].append(data_from_dict[i]["Name"])
        elif damage_scale[1] < data_from_dict[i]["Damage"] <= damage_scale[2]:
            hurricanes_by_damage[2].append(data_from_dict[i]["Name"])
        elif damage_scale[2] < data_from_dict[i]["Damage"] <= damage_scale[3]:
            hurricanes_by_damage[3].append(data_from_dict[i]["Name"])
        elif damage_scale[3] < data_from_dict[i]["Damage"] <= damage_scale[4]:
            hurricanes_by_damage[4].append(data_from_dict[i]["Name"])
        else:
            hurricanes_by_damage[5].append(data_from_dict[i]["Name"])
    return hurricanes_by_damage
print(hurricanes_rating_damage(hurricane))