def read_grid_from_file(file_path):
    # Create a dictionary to hold the characters at their (x, y) positions
    grid = {}

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        # Skip the header line
        next(file)
        
        # Process each line in the file
        for line in file:
            # Split the line into components
            parts = line.strip().split('\t')
            if len(parts) == 3:
                x = int(parts[0])  # x-coordinate
                character = parts[1]  # Character
                y = int(parts[2])  # y-coordinate
                
                # Store the character in the grid dictionary
                grid[(x, y)] = character
    return grid

def print_grid(grid):
    # Determine the dimensions of the grid
    max_x = max(x for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())

    # Print the grid
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            # Print the character if it exists, otherwise print a space
            # print(grid.get((x, y), ' '), end=' ')

            # Print unicode
            ch = grid.get((x,y), ' ')
            print(ch, end=' ')
            # prints raw byte numeral, Unicode escape sequence
            # print(f'\\u{ord(ch):04x}', end=' ')
        print()  # New line after each row


def rotate_grid_clockwise(grid):
    max_x = max([x for x,y in grid.keys()])
    max_y = max([y for x,y in grid.keys()])
    rotated = {}
    for (x,y),val in grid.items():
        new_x = y
        new_y = max_x - x
        rotated[(new_x,new_y)] = val
    return rotated


# Example usage
file_path = 'C:/Users/huali/Downloads/downloaded_doc.txt'  # Replace with your actual file path
grid1 = read_grid_from_file(file_path)
print_grid(grid1)
print('----------------------------')
grid2 = rotate_grid_clockwise(grid1)
print_grid(grid2)

