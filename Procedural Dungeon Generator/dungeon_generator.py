import random


class DungeonGenerator:
    def __init__(self, width, height, num_levels):
        self.width = width
        self.height = height
        self.num_levels = num_levels
        self.dungeons = []

    def generate(self):
        for _ in range(self.num_levels):
            dungeon = [[' ' for _ in range(self.width)]
                       for _ in range(self.height)]
            self.add_rooms(dungeon)
            self.add_corridors(dungeon)
            self.add_doors(dungeon)
            self.add_enemies(dungeon)
            self.add_treasures(dungeon)
            self.add_traps(dungeon)
            self.add_stairs(dungeon)
            self.dungeons.append(dungeon)

    def add_rooms(self, dungeon):
        num_rooms = random.randint(15, 30)
        for _ in range(num_rooms):
            room_width = random.randint(4, 12)
            room_height = random.randint(4, 10)
            x = random.randint(1, self.width - room_width - 1)
            y = random.randint(1, self.height - room_height - 1)
            self.create_room(dungeon, x, y, room_width, room_height)

    def create_room(self, dungeon, x, y, width, height):
        for i in range(x, x + width):
            for j in range(y, y + height):
                dungeon[j][i] = '.'

    def add_corridors(self, dungeon):
        for i in range(len(dungeon) - 1):
            for j in range(len(dungeon[0]) - 1):
                if dungeon[i][j] == '.' and dungeon[i+1][j] == '.':
                    self.create_vertical_corridor(dungeon, i, j)
                if dungeon[i][j] == '.' and dungeon[i][j+1] == '.':
                    self.create_horizontal_corridor(dungeon, i, j)

    def create_vertical_corridor(self, dungeon, x, y):
        while y < len(dungeon[0]) - 1 and dungeon[x][y] != '#':
            dungeon[x][y] = '#'
            y += 1

    def create_horizontal_corridor(self, dungeon, x, y):
        while x < len(dungeon) - 1 and dungeon[x][y] != '#':
            dungeon[x][y] = '#'
            x += 1

    def add_doors(self, dungeon):
        for i in range(1, len(dungeon) - 1):
            for j in range(1, len(dungeon[0]) - 1):
                if dungeon[i][j] == '.' and random.random() < 0.02:
                    dungeon[i][j] = '+'

    def add_enemies(self, dungeon):
        num_enemies = random.randint(5, 15)
        enemy_types = ['Goblin', 'Skeleton', 'Orc', 'Spider']
        for _ in range(num_enemies):
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if dungeon[y][x] == '.':
                enemy_type = random.choice(enemy_types)
                dungeon[y][x] = 'E(' + enemy_type[0] + ')'

    def add_treasures(self, dungeon):
        num_treasures = random.randint(5, 10)
        treasure_types = ['Gold', 'Gem', 'Artifact']
        for _ in range(num_treasures):
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if dungeon[y][x] == '.':
                treasure_type = random.choice(treasure_types)
                dungeon[y][x] = '$(' + treasure_type[0] + ')'

    def add_traps(self, dungeon):
        num_traps = random.randint(5, 10)
        trap_types = ['Spikes', 'Poison', 'Fire']
        for _ in range(num_traps):
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if dungeon[y][x] == '.':
                trap_type = random.choice(trap_types)
                dungeon[y][x] = '^(' + trap_type[0] + ')'

    def add_stairs(self, dungeon):
        for _ in range(2):
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if dungeon[y][x] == '.':
                dungeon[y][x] = '<' if _ == 0 else '>'

    def print_dungeons(self):
        for level, dungeon in enumerate(self.dungeons, start=1):
            print(f"Level {level} Dungeon:")
            for row in dungeon:
                print(''.join(row))
            print()


# Create a dungeon generator and generate dungeons
dungeon_generator = DungeonGenerator(80, 40, num_levels=3)
dungeon_generator.generate()

# Print the generated dungeons
dungeon_generator.print_dungeons()
