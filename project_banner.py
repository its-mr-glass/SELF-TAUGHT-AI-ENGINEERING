####################################################################################################################################################
#                                                             [LAMAR]
####################################################################################################################################################
import subprocess
import sys

# Function to install a package if it's not already installed
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Try importing the package; if it fails, install it
try:
    import pyfiglet
except ImportError:
    print("pyfiglet not found. Installing...")
    install("pyfiglet")
    import pyfiglet

# Now you can use pyfiglet as usual
ascii_art = pyfiglet.figlet_format("Lamar")
print(ascii_art)
###################################################################################################################################################
#self practice...


"""
##############################################################
#               Project: [Your Project Name Here]            #
#               Author: Lamar                                #
#               Date: Auto                                  #
#               Description: [Write your goal here]          #
##############################################################
"""

import sys
import subprocess
from datetime import datetime

# Auto-install pyfiglet if not found
try:
    import pyfiglet
except ImportError:
    print("[INFO] pyfiglet not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet"])
    import pyfiglet

# Banner function
def banner(name="LAMAR"):
    print(pyfiglet.figlet_format(name))
    print(f"📅 Script started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 100)

# Call banner
banner()
