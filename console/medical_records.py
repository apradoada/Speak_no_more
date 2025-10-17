import random
STATUSES = ["Alive", "DECEASED", "Medical Analysis Required", "Alive", "Medical Analysis Required", "Alive", "Medical Analysis Required", "Alive", "Alive", "Alive", "Alive", "Alive", "Alive"]

records = {
    "COOKIE" : {
        "NAME": "J. Von Schramm",
        "AGE": "32",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    },
    "CAPTAIN" : {
        "NAME": "K. MEEHAN",
        "AGE": "27",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    },
    "FOUR EYES" : {
        "NAME": "N. Dunaway",
        "AGE": "33",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    },
    "SAWBONES" : {
        "NAME": "J. Maxwell",
        "AGE": "34",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    },
    "EINSTEIN" : {
        "NAME": "C. Arlauskas",
        "AGE": "29",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    },
    "BOOMSTICK" : {
        "NAME": "A. Saenz",
        "AGE": "30",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    },
    "BEEFCAKE" : {
        "NAME": "N. Lafayette",
        "AGE": "22",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    },
    "COMPASS" : {
        "NAME": "T. Jitkoff",
        "AGE": "35",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    },
    "MAPQUEST" : {
        "NAME": "S. McCormick",
        "AGE": "36",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    },
    "CHATTER" : {
        "NAME": "K. Badr",
        "AGE": "26",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    },
    "ECHO" : {
        "NAME": "A. Prado",
        "AGE": "33",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    },
    "ROOKIE" : {
        "NAME": "A. Rodriguez",
        "AGE": "38",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    },
    "NEWTON" : {
        "NAME": "K. Hassandras",
        "AGE": "30",
        "STATUS": f"{STATUSES[random.randint(0, len(STATUSES)-1)]}"
    }

}