from .helpers import type_text
from .medical_records import records
from .captains_log import captains_log
import random
import os
import time
from google import genai

def input_dict():
    user_input = input()
    if FUN_DICT.get(user_input) == retrieve_records:
        FUN_DICT.get(user_input)(user_input)
    FUN_DICT.get(user_input, main_menu)()

def main_menu():
    os.system("clear")
    start_message = "\nWELCOME ABOARD \nAll Systems Active"
    start_menu = "What System Would You Like To Access Today? \n"
    start_menu_options = "1. COMMS \n" \
            "2. MEDICAL \n" \
            "3. ENGINEERING \n" \
            "4. ADMIN \n"
    type_text(start_message)
    type_text(start_menu)
    type_text(start_menu_options)

    input_dict()

def run_diagnostics():
    for i in range(10):
            type_text("Processing...")
        
    type_text("\nALL SYSTEMS ACTIVE\n", 1.0)

    input_dict()

def admin():
    os.system("clear")
    type_text("\nENTER PASSWORD TO ACCESS ADMIN:\n")
    user_input = input()
    counter = 0

    while user_input != "1nd3p3nd3nc3c0rp" and counter < 5:
        type_text("ACCESS DENIED PLEASE TRY AGAIN")
        user_input = input()
    
    if user_input == "1nd3p3nd3nc3c0rp":
        for message in captains_log:
            type_text(f"\n{message}\n")
            
    else:
        type_text("TOO MANY ATTEMPTS")

    input_dict()

def comms():
    os.system("clear")
    type_text("\nWELCOME TO COMMS\n")
    for i in range(10):
        type_text("SECURING CONNECTION TO HQ...")
    
    type_text("\nCONNECTION SECURED. PLEASE ENTER MESSAGE:\n")

    user_input = input()
    message = ""

    while user_input != "MAYDAY" and user_input != "OVER":
        message += f" {user_input}"
        user_input = input()
    
        if user_input == "ROGER":
            type_text("\nMESSAGE SENT TO HQ. STAND BY FOR REPLY\n")
            pingGemini(message)
            message = ""

    pingGemini(message)

    if user_input == "MAYDAY":
        for i in range(10):
            type_text("MESSAGE SENDING...")
        type_text("\nCONNECTION TO HQ LOST\n") 
    
    input_dict()


def pingGemini(message):
    client = genai.Client(api_key="AIzaSyDBMGM-YBEcQ52VWyKz_W1hLPpOF_7S5jw")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= f"You're a mission control expert who receives the following message from a remote base. Reply with a simple yet appropriate response. Message: '{message}'"
    )

    type_text(response.text.upper())
def panic(delay_seconds=0.1):
    """
    Outputs a continuous stream of random 1s and 0s to the console.

    Args:
        delay_seconds (float): The time in seconds to wait between each output of a random 1 or 0.
    """
    try:
        while True:
            random_string = random.choice(["0", "1", " "])* random.randint(1, 100)  # Generates either 0 or 1
            print(random_string)
            time.sleep(delay_seconds)
    except KeyboardInterrupt:
        main_menu()

def print_bad_message():
    
        for i in range(10):
            type_text("Processing...")
        
        type_text("\nBREACH\n", 1.0)
        for i in range(10):
            type_text("...")
        type_text("\nRUN\n", 1.5)

        input()
        panic()

def engineering():
    os.system("clear")
    type_text("WELCOME TO ENGINEERING\n")
    engineering_options = "1. RUN DIAGNOSTICS\n" \
            "2. CHECK POWER LEVELS \n" \
            "3. CHECK ANDROID STATUS \n" 
    type_text(engineering_options)

    input_dict()
def check_power_levels():
    os.system("clear")
    for i in range(10):
        type_text("CHECKING POWER LEVELS...")
    power_level = random.randint(25, 100)
    if power_level > 50:
        type_text(f"\nPOWER AT {power_level}%. SYSTEM REMAINS SUSTAINABLE\n")
    else:
        type_text(f"\nPOWER AT {power_level}%. GENERATOR CHECK RECOMMENDED\n")
    
    input_dict()

def check_android_status():
    android_statuses = {
        "ALL FUNCTIONS OPERATIONAL": 75,
        "LOW BATTERY: PLEASE RECHARGE": 25,
    }
    android_status_list = []
    for key, value in android_statuses.items():
        android_status_list.extend([key]*value)
    
    for i in range(10):
        type_text("ASSESSING ANDROID...")

    type_text(f"\nANDROID STATUS: {android_status_list[random.randint(0, 99)]}\n")

    input_dict()

def medical_menu():
    os.system("clear")
    type_text("\mWHOSE RECORDS WOULD YOU LIKE TO ACCESS?\n")
    medical_options = "1. CAPTAIN\n" \
            "2. COOKIE \n" \
            "3. FOUR EYES \n" \
            "4. EINSTEIN \n" \
            "5. BOOMSTICK \n" \
            "6. BEEFCAKE \n" \
            "7. COMPASS \n" \
            "8. MAPQUEST \n" \
            "9. CHATTER \n" \
            "10. ECHO \n" \
            "11. SAWBONES \n" \
            "12. ROOKIE \n" \
            "11. NEWTON \n" 
    
    type_text(medical_options)
    input_dict()

def retrieve_records(officer):
    os.system("clear")
    type_text(f"\n{officer}")
    for key, value in records.get(officer,0).items():
        type_text(f"{key}: {value}")

    input_dict()
            

FUN_DICT = {
    "": main_menu,
    "RUN DIAGNOSTICs": print_bad_message,
    "RUN DIAGNOSTICS": run_diagnostics,
    "MEDICAL": medical_menu,
    "CAPTAIN": retrieve_records,
    "COOKIE": retrieve_records,
    "FOUR EYES": retrieve_records,
    "EINSTEIN": retrieve_records,
    "BOOMSTICK": retrieve_records,
    "BEEFCAKE": retrieve_records,
    "COMPASS": retrieve_records,
    "MAPQUEST": retrieve_records,
    "CHATTER": retrieve_records,
    "ECHO": retrieve_records,
    "ROOKIE": retrieve_records,
    "NEWTON": retrieve_records,
    "SAWBONES": retrieve_records,
    "ENGINEERING": engineering,
    "CHECK POWER LEVELS": check_power_levels,
    "CHECK ANDROID STATUS": check_android_status,
    "ADMIN": admin,
    "COMMS": comms,
}