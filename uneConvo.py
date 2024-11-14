#! /usr/bin/python3

import random
import sys

# Conversation Mood Table
conversation_mood_table = {
    "loved": {
        "withdrawn": range(1, 2), "guarded": range(2, 7), "cautious": range(7, 17),
        "neutral": range(17, 32), "sociable": range(32, 71), "helpful": range(71, 86), "forthcoming": range(86, 101)
    },
    "friendly": {
        "withdrawn": range(1, 3), "guarded": range(3, 9), "cautious": range(9, 21),
        "neutral": range(21, 41), "sociable": range(41, 77), "helpful": range(77, 90), "forthcoming": range(90, 101)
    },
    "peaceful": {
        "withdrawn": range(1, 4), "guarded": range(4, 12), "cautious": range(12, 26),
        "neutral": range(26, 56), "sociable": range(56, 83), "helpful": range(83, 94), "forthcoming": range(94, 101)
    },
    "neutral": {
        "withdrawn": range(1, 6), "guarded": range(6, 16), "cautious": range(16, 31),
        "neutral": range(31, 61), "sociable": range(71, 86), "helpful": range(86, 96), "forthcoming": range(96, 101)
    },
    "distrustful": {
        "withdrawn": range(1, 8), "guarded": range(8, 19), "cautious": range(19, 47),
        "neutral": range(47, 77), "sociable": range(77, 91), "helpful": range(91, 98), "forthcoming": range(98, 101)
    },
    "hostile": {
        "withdrawn": range(1, 12), "guarded": range(12, 25), "cautious": range(25, 62),
        "neutral": range(62, 82), "sociable": range(82, 94), "helpful": range(94, 99), "forthcoming": range(99, 101)
    },
    "hated": {
        "withdrawn": range(1, 16), "guarded": range(16, 31), "cautious": range(31, 70),
        "neutral": range(70, 85), "sociable": range(85, 95), "helpful": range(95, 100), "forthcoming": range(100, 101)
    }
}

# Bearing Table
bearing_table = {
    "scheming": {
        1: "intent", 2: "bargain", 3: "means", 4: "proposition", 5: "plan",
        6: "compromise", 7: "agenda", 8: "arrangement", 9: "negotiation", 10: "plot"
    },
    "insane": {
        1: "madness", 2: "fear", 3: "accident", 4: "chaos", 5: "idiocy",
        6: "illusion", 7: "turmoil", 8: "confusion", 9: "façade", 10: "bewilderment"
    },
    "friendly": {
        1: "alliance", 2: "comfort", 3: "gratitude", 4: "shelter", 5: "happiness",
        6: "support", 7: "promise", 8: "delight", 9: "aid", 10: "celebration"
    },
    "hostile": {
        1: "death", 2: "capture", 3: "judgment", 4: "combat", 5: "surrender",
        6: "rage", 7: "resentment", 8: "submission", 9: "injury", 10: "destruction"
    },
    "inquisitive": {
        1: "questions", 2: "investigation", 3: "interest", 4: "demand", 5: "suspicion",
        6: "request", 7: "curiosity", 8: "skepticism", 9: "command", 10: "petition"
    },
    "knowing": {
        1: "report", 2: "effects", 3: "examination", 4: "records", 5: "account",
        6: "news", 7: "history", 8: "telling", 9: "discourse", 10: "speech"
    },
    "mysterious": {
        1: "rumor", 2: "uncertainty", 3: "secrets", 4: "misdirection", 5: "whispers",
        6: "lies", 7: "shadows", 8: "enigma", 9: "obscurity", 10: "conundrum"
    },
    "prejudiced": {
        1: "reputation", 2: "doubt", 3: "bias", 4: "dislike", 5: "partiality",
        6: "belief", 7: "view", 8: "discrimination", 9: "assessment", 10: "difference"
    }
}

# Focus Table
focus_table = {
    1: "current scene", 2: "last story", 3: "equipment",
    4: "parents", 5: "history", 6: "retainers",
    7: "wealth", 8: "relics", 9: "last action",
    10: "skills", 11: "superiors", 12: "fame",
    13: "campaign", 14: "future action", 15: "friends",
    16: "allies", 17: "last scene", 18: "contacts",
    19: "flaws", 20: "antagonist", 21: "rewards",
    22: "experience", 23: "knowledge", 24: "recent scene",
    25: "community", 26: "treasure", 27: "the character",
    28: "current story", 29: "family", 30: "power",
    31: "weapons", 32: "previous scene", 33: "enemy"
}

relationships = list(conversation_mood_table.keys())
bearings = list(bearing_table.keys())

def determine_conversation_mood(relationship=None):
    if relationship not in relationships:
        relationship = random.choice(relationships)
    
    roll = random.randint(1, 100)
    
    for mood, range_values in conversation_mood_table[relationship].items():
        if roll in range_values:
            conversation_mood = mood
            break

    return relationship, conversation_mood

def determine_bearing(bearing=None):
    if bearing not in bearings:
        bearing = random.choice(bearings)
    
    roll = random.randint(1, 100)
    bearing_index = (roll - 1) // 10 + 1
    bearing_value = bearing_table[bearing][bearing_index]

    return bearing, bearing_value

def determine_focus():
    roll = random.randint(1, 100)
    focus_index = (roll - 1) // 3 + 1
    focus_value = focus_table[focus_index]
    
    return focus_value

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in ["--help", "-h"]:
            print("Usage: unConvo.py [relationship] [bearing]")
            print("Possible relationships:")
            for relationsihip in relationships:
                print(f"  - {relationsihip}")
            print("Possible bearings:")
            for bearing in bearings:
                print(f"  - {bearing}")
            sys.exit(0)
        relationship_input = sys.argv[1].lower()
    else:
        relationship_input = None
    
    if len(sys.argv) > 2:
        bearing_input = sys.argv[2].lower()
    else:
        bearing_input = None

    relationship, mood = determine_conversation_mood(relationship_input)
    bearing, bearing_value = determine_bearing(bearing_input)
    focus = determine_focus()
    
    print(f"Relationship: {relationship}")
    print(f"Conversation Mood: {mood}")
    print(f"Bearing: {bearing_value} ({bearing})")
    print(f"Focus: {focus}")
    print(f"The {mood} NPC speaks of {bearing_value} regarding the PC's {focus}.")
