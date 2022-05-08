#!/usr/bin/python3
import json
import os
import requests
import time
from dotenv import load_dotenv

# this code was written with the help of github copilot.

# parse .env file into environment variables
env_file_found = load_dotenv()

user = os.getenv('GITHUB_USER')
token = os.getenv('GITHUB_TOKEN')

if user is None or token is None:
	if env_file_found:
		print('Found .env file but no GITHUB_USER or GITHUB_TOKEN')
	else:
		print('No .env file found')

# make a curl request with the credentials
url = "https://api.github.com/user/repos"
response = requests.get(url, auth=(user, token)).json()

# get a list of the directories in the current directory
dirs = os.listdir()
# transform the dirs list to lowercase
dirs = [d.lower() for d in dirs]

for repo in response:
	if repo['fork'] == False:
		if repo['name'].lower() in dirs:
			continue
		os.system('git clone ' + repo['ssh_url'])

