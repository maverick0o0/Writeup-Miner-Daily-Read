import json
import os
import random
from modules.database import add_to_db, check_existence_in_db
from modules.logger import Customlogger, Logger_type
from modules.notify import notify
from modules.variables import writeup_file
import sys

def parse_writeups(args):
    # Read writeups data from a file
    if not os.path.exists(writeup_file):
        # fetch()
        Customlogger(True, f"[-] No {writeup_file} found." , Logger_type.ERROR)
        sys.exit(0)
        
    with open(writeup_file, 'r') as file:
        data = file.read()
        data = json.loads(data)
    
    writeups = []
    
    # Select newset writeups
    
    for i, entry in enumerate(data.get('data', [])):
        title = entry['Links'][0]['Title']
        link = entry['Links'][0]['Link']
        authors = entry['Authors'][0] if entry['Authors'] else None
        programs = entry['Programs']
        bugs = entry['Bugs']
        bounty = entry['Bounty']
        publication_date = entry['PublicationDate']
        added_date = entry['AddedDate']
    
        
        if check_existence_in_db(link):
            # select random entry
            # To ensure that th random_entry doesn't already exist in the database
            Customlogger(True, f"[+] No new writeups , select random writeups." , Logger_type.INFO)
            while True:
                random_entry = random.choice(data.get('data', []))
                if not check_existence_in_db(random_entry['Links'][0]['Link']):
                    writeups.append(random_entry)
                    break
        else:
            Customlogger(True, f"[+] New writeups found." , Logger_type.INFO)
            writeups.append(entry)
        
        if i + 1 == args.number:
            break
    
    
    # if len(writeups) == args.number
    add_to_db(writeups)
    for writeup in writeups:
        notify(args , writeup)
    