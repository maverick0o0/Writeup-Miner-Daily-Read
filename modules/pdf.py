import subprocess
import pdfkit
from modules.logger import Customlogger, Logger_type
import os


def convert_webpage_to_pdf(url, output_path):
    
    # Delete all *.pdf 
    Customlogger(True, f"[+] Cleanup all PDFs. (*.pdf)", Logger_type.INFO)
    working_dir = os.getcwd()
    rm_command = f'rm -rf {working_dir}/*.pdf'
    subprocess.run(rm_command, shell=True)
    
    try:
        pdfkit.from_url(url, output_path)
        print(f"")
        Customlogger(True, f"[+] Conversion successful. PDF saved to {output_path}", Logger_type.INFO)
        return output_path
        
    except Exception as e:
        Customlogger(True, f"[-] Error converting web page to PDF: {e}", Logger_type.ERROR)
        return None


