import argparse
import sys
import requests
from modules.database import create_db
from modules.logger import Customlogger, Logger_type
from modules.parser import parse_writeups
from modules.variables import writeup_src , writeup_file


def setup_argparse():
    parser = argparse.ArgumentParser(description="Daily Read")
    
    parser.add_argument("-n","-number" , dest='number' ,type=int, help="Number of writeups to process.")
    parser.add_argument("-pdf",dest='pdf' ,action="store_true", default=False, help="Generate PDFs from each writeup.")
    
    return parser , parser.parse_args()
    
    

def fetch_writeups():
    try:
        # Make a GET request to the URL
        response = requests.get(writeup_src)
    
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open a local file with write-binary mode and save the content
            with open(writeup_file, 'wb') as file:
                file.write(response.content)
            Customlogger(True, f"[+] File '{writeup_file}' downloaded and saved successfully." , Logger_type.INFO)
            
        else:
            Customlogger(True, f"[-] Failed to download file. Status code: {response.status_code}" , Logger_type.ERROR)
            sys.exit(0)

    except Exception as e:
        Customlogger(True, f"[-] Error {e}" , Logger_type.ERROR)

    
def main():
    Customlogger(True, f"-------------------------------------------------------" , Logger_type.INFO)
    Customlogger(True, f"Fetching writeups." , Logger_type.INFO)
    fetch_writeups()
    create_db()
    parse_writeups(args)
    
    
    
    
    
if __name__ == "__main__":
    parser , args = setup_argparse()
    main()