import random

def generate_map_with_row_letters():
    # Symbols representing different features
    symbols = {
        'c': 'Cave',
        'X': 'City',
        '^': 'Dungeon',
        '!': 'Feature',
        'G': 'Gate',
        '+': 'Keep',
        '#': 'Ruins',
        'T': 'Temple',
        'I': 'Tower',
        'x': 'Town'
    }
    
    # Initialize the grid
    grid = [[' ' for _ in range(8)] for _ in range(8)]
    
    # Fill the grid with symbols based on a 30% chance
    for i in range(8):
        for j in range(8):
            if random.random() < 0.30:
                grid[i][j] = random.choice(list(symbols.keys()))
    
    # Generate the markdown table
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    markdown = "|   | " + " | ".join([str(i+1) for i in range(8)]) + " |\n"
    markdown += "|---" + "|---" * 8 + "|\n"
    for idx, row in enumerate(grid):
        markdown += f"| {letters[idx]} | " + " | ".join(row) + " |\n"
    
    return markdown, symbols

# Generate and print the map with row letters and legend
map_output_with_letters, legend = generate_map_with_row_letters()

# Print the map
print(map_output_with_letters)

# Print the legend
print("\nLegend:")
for symbol, description in legend.items():
    print(f"{symbol}: {description}")
