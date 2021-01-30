#!/bin/python3

import os
import sys
import json
import datetime
import fileinput
import subprocess
import pathlib

import requests

if len(sys.argv) > 1 and sys.argv[1] == 'cron':
    # Only make API calls while the game is running, unless run directly
    output = subprocess.check_output(['ps', '-e']).decode('utf-8')
    running = False
    for line in output.split('\n'):
        if 'GW2-64.exe' in line:
            running = True;
            break;
    if not running:
        exit(0)

with open(pathlib.Path(__file__).parent / 'config.json', 'r') as conf:
    config=json.load(conf)

now = datetime.datetime.now()
day = datetime.date.today()
if now.hour < int(config['reset']):
    day -= datetime.timedelta(days=1)
file = os.path.expanduser(config['path'] + '/' + day.isoformat() + '.md')
#print(file)

if not os.path.isfile(file):
    print(f'File {file} doesn\'t exist')
    exit(1)

headers = requests.structures.CaseInsensitiveDict()
headers['Authorization'] = 'Bearer ' + config['key']

response = requests.get('https://api.guildwars2.com/v2/account/worldbosses', headers=headers)
if response.status_code != 200:
    print('API error')
    exit(2)
bosses = [x.lower().replace('_', ' ') for x in response.json()]

response = requests.get('https://api.guildwars2.com/v2/account/dailycrafting', headers=headers)
if response.status_code != 200:
    print('API error')
    exit(2)
materials = [' '.join(x.lower().split('_')[2:]) for x in response.json()]

check = bosses + materials
for line in fileinput.input(files=file, inplace=True):
    for item in check:
        if item in line.lower():
            if '- [ ]' in line:
                line = line.replace('- [ ]', '- [X]')
            break
    print(line, end='')
