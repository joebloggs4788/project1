import random

# Strategy Interface
class MazeGenerationStrategy:
    # def __init__(self,width,height):
    #     self.width = width
    #     self.height = height

    def generate_maze(self, width, height):
        raise NotImplementedError("This method should be overridden by subclasses.")

# Strategy 1: Randomized Prim's Algorithm
class RandomizedPrimsStrategy(MazeGenerationStrategy):
    def generate_maze(self, width, height):
        maze = [['#' for _ in range(width)] for _ in range(height)]
        start_x, start_y = 1, 1
        maze[start_y][start_x] = ' '

        walls = [(start_x, start_y + 1), (start_x, start_y - 1), (start_x + 1, start_y), (start_x - 1, start_y)]
        random.shuffle(walls)

        while walls:
            x, y = walls.pop()
            if 0 < x < width and 0 < y < height and maze[y][x] == '#':
                adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                if sum(1 for ax, ay in adjacent if 0 < ax < width and 0 < ay < height and maze[ay][ax] == ' ') == 1:
                    maze[y][x] = ' '
                    walls.extend(adjacent)
                    random.shuffle(walls)

        return maze

# Strategy 2: Recursive Backtracking
class RecursiveBacktrackingStrategy(MazeGenerationStrategy):
    def generate_maze(self, width, height):
        maze = [['#' for _ in range(width)] for _ in range(height)]
        self.carve_passages_from(1, 1, maze, width, height)
        return maze

    def carve_passages_from(self, cx, cy, maze, width, height):
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
                maze[cy + dy // 2][cx + dx // 2] = ' '
                maze[ny][nx] = ' '
                self.carve_passages_from(nx, ny, maze, width, height)

# Strategy 3: Aldous-Broder Algorithm
class AldousBroderStrategy(MazeGenerationStrategy):
    def generate_maze(self, width, height):
        maze = [['#' for _ in range(width)] for _ in range(height)]
        x, y = random.randint(1, (width - 1) // 2) * 2, random.randint(1, (height - 1) // 2) * 2
        maze[y][x] = ' '
        visited = {(x, y)}
        total_cells = (width // 2) * (height // 2)
        cells_visited = 1

        while cells_visited < total_cells:
            direction = random.choice([(2, 0), (-2, 0), (0, 2), (0, -2)])
            nx, ny = x + direction[0], y + direction[1]

            if 0 < nx < width and 0 < ny < height and (nx, ny) not in visited:
                maze[y + direction[1] // 2][x + direction[0] // 2] = ' '
                maze[ny][nx] = ' '
                visited.add((nx, ny))
                x, y = nx, ny
                cells_visited += 1
            else:
                x, y = random.choice(list(visited))

        return maze

# Maze Generator Class
class MazeGenerator:
    def __init__(self, strategy: MazeGenerationStrategy):
        self.strategy = strategy

    def generate(self, width, height):
        return self.strategy.generate_maze(width, height)

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# User Interaction
def main():
    print("Choose a maze generation strategy:")
    print("1. Randomized Prim's Algorithm")
    print("2. Recursive Backtracking")
    print("3. Aldous-Broder Algorithm")
    
    choice = int(input("Enter the number: "))
    generator = None
    
    match choice:
        case 1:
            generator = MazeGenerator(RandomizedPrimsStrategy())
        case 2:
            generator = MazeGenerator(RandomizedPrimsStrategy())
        case 3:
            generator = MazeGenerator(RandomizedPrimsStrategy())
        case _:
            raise RuntimeError(f"choice {choice} of maze generation strategy not supported.")
    
    maze = generator.generate(30,10)
    print_maze(maze)

if __name__ == '__main__':
    main()

