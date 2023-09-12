#!/usr/bin/env python

import requests
import json
from dotenv import load_dotenv
import os
import urllib3

# Disable HTTP warnings
urllib3.disable_warnings()

# Set credentials
load_dotenv()
user = os.environ.get('user')
password = os.environ.get('pass')
auth = (user, password)

# Open json file to read
file = open('data.json', 'r')

# Load the json as JSON file
data = json.load(file)

for i in data:
    # Fetch relevant data
    code = i['JSON_KEY']
    name = i['JSON_KEY_2']

    # Set the title and content of the page to create
    page_title = name

    parent_page_id = 123
    space_key = 'NRKL'

    # Request URL - API for creating a new page as a child of another page
    url = 'https://API_URL_HERE'

    # Request Headers
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    # Format the page content
    page_html = '<h1>HTML {code} HERE</h1>'.format(code=code)

    # Request body
    data = {
        "type": "page",
        "title": page_title,
        "ancestors": [{
            "id": parent_page_id
        }],
        "space": {
            "key": space_key
        },
        "body": {
            "storage": {
                "value": page_html,
                "representation": "storage"
            }
        }
    }

    # Call the API
    try:
        r = requests.post(url=url, verify=False, data=json.dumps(
            data), auth=auth, headers=headers)  # type: ignore
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Print the hostname that failed and continue
        print(name)
        continue
        #print(json.dumps(data, indent=2))
        # raise SystemExit(e)

file.close()