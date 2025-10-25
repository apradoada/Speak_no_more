import random
STATUSES = ["Alive", "DECEASED", "Medical Analysis Required", "Alive", "Medical Analysis Required", "Alive", "Medical Analysis Required", "Alive", "Alive", "Alive", "Alive", "Alive", "Alive"]

records = {
    "COOKIE" : {
        "NAME": "J. Von Schramm",
        "AGE": "32",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "NONE", 
        "ALLERGIES": "NONE"
    },
    "CAPTAIN" : {
        "NAME": "K. MEEHAN",
        "AGE": "27",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "Seasonal allergies, Mild asthma", 
        "ALLERGIES": "Pollen"
    },
    "FOUR EYES" : {
        "NAME": "N. Dunaway",
        "AGE": "33",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "Migraines, Acid reflux", 
        "ALLERGIES": "Shellfish"
    },
    "SAWBONES" : {
        "NAME": "J. Maxwell",
        "AGE": "34",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "Eczema, Mild anxiety", 
        "ALLERGIES": "Peanuts, Penicillin"
    },
    "EINSTEIN" : {
        "NAME": "C. Arlauskas",
        "AGE": "29",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "NONE",
        "ALLERGIES": "Dust mites"
    },
    "BOOMSTICK" : {
        "NAME": "A. Saenz",
        "AGE": "30",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "Sinus infections, Mild hypertension, Acid reflux", 
        "ALLERGIES": "NONE"
    },
    "BEEFCAKE" : {
        "NAME": "N. Lafayette",
        "AGE": "22",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "Tension headaches, Mild joint pain",
        "ALLERGIES": "Gluten"
    },
    "COMPASS" : {
        "NAME": "T. Jitkoff",
        "AGE": "35",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "Asthma, Seasonal allergies", 
        "ALLERGIES": "Pet dander, Pollen"
    },
    "MAPQUEST" : {
        "NAME": "S. McCormick",
        "AGE": "36",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "NONE", 
        "ALLERGIES": "Latex"
    },
    "CHATTER" : {
        "NAME": "K. Badr",
        "AGE": "26",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "Eczema, Mild back pain", 
        "ALLERGIES": "NONE"
    },
    "ECHO" : {
        "NAME": "A. Prado",
        "AGE": "33",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "Migraines, Acid reflux, Seasonal allergies", 
        "ALLERGIES": "Dairy"
    },
    "ROOKIE" : {
        "NAME": "A. Rodriguez",
        "AGE": "38",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "Mild hypertension", 
        "ALLERGIES": "Peanuts"
    },
    "NEWTON" : {
        "NAME": "K. Hassandras",
        "AGE": "30",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}",
        "MEDICAL HISTORY": "Sinus infections, Mild anxiety", 
        "ALLERGIES": "Pollen, Shellfish"
    }

}