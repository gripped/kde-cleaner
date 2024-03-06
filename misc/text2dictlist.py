#!/usr/bin/python
#
#  text2dictlist.py - convert text list of kde config files to list of dicts for kde-cleaner
#

with open('list.txt', 'r') as file:
    lines = file.readlines()

cfg_dict_list = []
for line in lines:
    parts = line.split(',')
    if len(parts) != 3:
        print("Invalid list (Blank lines?)")
        quit()
    the_dict = {'file': parts[0], 'desc': parts[1], 'prog': parts[2]}
    cfg_dict_list.append(the_dict)

cfg_dict_list_str = "cfg_dict_list = [\n"
for entry in cfg_dict_list:
    cfg_dict_list_str += (
        "{'file':'" + entry['file'] + "', "
        "'desc':'" + entry['desc'] + "', "
        "'prog':'" + entry['prog'].strip() + "'},\n"
    )
cfg_dict_list_str += "]"


with open('list-dict', 'w') as file:
    file.write(f"{cfg_dict_list_str}")
