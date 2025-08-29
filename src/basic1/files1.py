
import os
import re

# Define the function to read the file and create the dictionary
def read_g1_file(filename):
    data_dict = {}
    
    with open(filename, 'r', encoding='utf-8') as file:
        # Skip the header line
        next(file)
        
        for line in file:
            # Strip whitespace and split by '|'
            # parts = line.strip().split('\t')
            parts = re.split('\t+',line.strip())
            if len(parts) == 3:
                # Extract x, character, and y values
                x = int(parts[0].strip())
                character = parts[1].strip().encode('utf-8').decode('unicode_escape')
                y = int(parts[2].strip())
                
                # Store in the dictionary
                data_dict[(x, y)] = character
    
    return data_dict

def build_grid(points : dict) -> str:
    xs = [x for (x,y) in points.keys()]
    ys = [y for (x,y) in points.keys()]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    width = xmax - xmin + 1
    height = ymax - ymin + 1

    grid = [[" " for _ in range(width)] for _ in range(height)]
    for (x,y), char in points.items():
        col = x - xmin
        row = y - ymin
        if 0<= row < height and 0 <= col < width:
            grid[row][col] = char

    grid_dict = {}
    y = ymin
    for row in grid:
        x = xmin
        for col in row:            
            grid_dict[(y,x)] = col
            x += 1
        y += 1

    grid1 = {}
    for (x,y), z in grid_dict.items():
        grid1[(y,x)] = z

    # convert dict{(int,int), char} to list[list[str]]
    ret_grid = [["" for _ in range(height)] for _ in range(width)]
    for (x,y), char in grid1.items():
        if 0<= x < width and 0 <= y < height:
            ret_grid[x][y] = char

    return ret_grid

# Main function to execute the script
def main():

    # full_path = os.path.join(drive, folder, filename)
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_folder, 'files1_g1(escaped).txt')
    print(file_path)
    os.chdir(script_folder)
    files = os.listdir()
    filename = 'files1_g1(escaped).txt'  # Specify the filename
    data = read_g1_file(filename)

    # # Print the resulting dictionary
    # for key, value in data.items():
    #     print(f"{key}: {value}")

    printable = build_grid(data)

    #print list[list[str]]
    printstr = "\n".join(["".join(row) for row in printable])
 

    print(printstr)

if __name__ == '__main__':
    main()