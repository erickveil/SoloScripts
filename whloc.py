#!/bin/python3

import json
import random

# Load JSON data
with open("natures.json") as file:
    locations = json.load(file)

# Step 1: Randomly select three nature objects
selected_natures = random.sample(locations, 3)

# Step 2: Aggregate their descriptions, 'canAlways', 'aesthetic', and 'folklore'
nature_descriptions = []
can_always_actions = []
aesthetic_elements = []
folklore_elements = []

for nature in selected_natures:
    nature_descriptions.append(f"**{nature['nature']}**\n- {nature['description']}")
    can_always_actions.extend(nature['canAlways'])
    aesthetic_elements.extend(nature['aesthetic'])
    folklore_elements.extend(nature['folklore'])

# Step 3: Select random aesthetic and folklore elements
selected_aesthetics = random.sample(aesthetic_elements, 2)
selected_folklore = random.choice(folklore_elements)

# Step 4: Format the output
output = "# Natures\n\n"
output += "\n\n".join(nature_descriptions) + "\n\n"
output += "# This Place Can Always:\n\n"
output += "- " + "\n- ".join(can_always_actions) + "\n\n"
output += "# Aesthetic Elements:\n\n"
output += "- " + "\n- ".join(selected_aesthetics) + "\n\n"
output += "# Folklore\n\n"
output += "- " + selected_folklore

# Print the result
print(output)
