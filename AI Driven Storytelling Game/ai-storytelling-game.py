import random


class StoryNode:
    def __init__(self, text, options=None, effects=None):
        self.text = text
        self.options = options or []
        self.effects = effects or {}


class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.traits = {}


class StoryGame:
    def __init__(self):
        self.story_map = {}
        self.current_node = None
        self.player = None

    def add_node(self, node_id, text, options=None, effects=None):
        self.story_map[node_id] = StoryNode(text, options, effects)

    def start(self, node_id):
        self.current_node = self.story_map.get(node_id)

    def make_choice(self, choice_idx):
        if self.current_node and choice_idx < len(self.current_node.options):
            next_node_id = self.current_node.options[choice_idx]
            self.current_node = self.story_map.get(next_node_id)

    def apply_effects(self, effects):
        for key, value in effects.items():
            if key == "add_item":
                self.player.inventory.append(value)
            elif key == "add_trait":
                self.player.traits[value[0]] = value[1]

    def get_current_text(self):
        text = self.current_node.text if self.current_node else "Game Over"
        if self.current_node.effects:
            self.apply_effects(self.current_node.effects)
        return text.replace("{name}", self.player.name)

    def is_game_over(self):
        return not self.current_node


# Create the game
game = StoryGame()

# Create character
player_name = input("Enter your character's name: ")
player = Character(player_name)
game.player = player

nodes_data = [
    ("start", "You wake up in a mysterious land. Do you explore or rest?",
     ["explore", "rest"]),
    ("explore", "You venture deep into the woods and find an old cabin. Do you enter or continue exploring?", [
     "enter_cabin", "continue_exploring"]),
    ("rest", "You find a cozy spot and rest for a while. When you wake up, you see a map nearby. Will you follow the map or ignore it?", [
     "follow_map", "ignore_map"]),
    ("enter_cabin", "Inside the cabin, you discover a hidden passage. Do you enter the passage or stay in the cabin?", [
     "enter_passage", "stay_in_cabin"]),
    ("continue_exploring", "You stumble upon a magical waterfall. Do you drink from it or move on?", [
     "drink_water", "move_on"]),
    ("follow_map", "Following the map, you find a hidden treasure. Do you take it or leave it?", [
     "take_treasure", "leave_treasure"]),
    ("enter_passage", "The passage leads to an ancient temple. Do you explore further or leave?", [
     "explore_temple", "leave_temple"]),
    ("stay_in_cabin", "You find a journal that reveals the history of the land. Do you keep reading or close the journal?", [
     "keep_reading", "close_journal"]),
    ("drink_water", "Drinking from the waterfall grants you enhanced senses. Will you use them to uncover secrets or continue your journey?", [
     "uncover_secrets", "continue_journey"]),
    ("move_on", "As you move on, you encounter a talking animal. Do you listen to its advice or ignore it?", [
     "listen_to_animal", "ignore_animal"]),
    ("enter_passage", "The passage leads to an underground city. Do you explore the city or return to the surface?", [
     "explore_city", "return_to_surface"]),
    ("uncover_secrets", "Using your enhanced senses, you find a hidden cave. Do you enter the cave or keep moving?", [
     "enter_cave", "keep_moving"]),
    ("listen_to_animal", "The animal warns you of danger ahead. Do you heed its warning or take your chances?", [
     "heed_warning", "take_chances"]),
    ("node88", "You come across a portal that leads to another realm. Do you step through or stay?", [
     "step_through", "stay"]),
    ("explore_city", "You discover an ancient artifact that can grant a wish. What do you wish for?", [
     "wish_for_power", "wish_for_wisdom"]),
    ("return_to_surface", "You emerge from the passage and find yourself in a bustling marketplace. Do you explore or leave?", [
     "explore_marketplace", "leave_marketplace"]),
    ("enter_cave", "Inside the cave, you find a friendly spirit. Do you converse with it or leave?", [
     "converse_with_spirit", "leave_cave"]),
    ("keep_moving", "You continue your journey and encounter a group of fellow travelers. Do you join them or go your own way?", [
     "join_travelers", "go_own_way"]),
    ("heed_warning", "You avoid the danger and find a hidden treasure. What will you do with the treasure?", [
     "share_treasure", "keep_treasure"]),
    ("take_chances", "Your gamble pays off, and you uncover a secret passage. Will you enter it or continue?", [
     "enter_secret_passage", "continue_journey"]),
    ("step_through", "You step through the portal and find yourself in a futuristic city. How do you navigate this new world?", [
     "explore_futuristic_city", "find_a_way_back"]),
    ("stay", "You decide to stay in the current realm, building a new life for yourself.", []),
    ("explore_marketplace", "In the marketplace, you meet a mysterious merchant. Will you buy a rare item or ignore the merchant?", [
     "buy_item", "ignore_merchant"]),
    ("leave_marketplace", "You leave the marketplace and find yourself in a tranquil garden. Do you explore further or rest?", [
     "explore_garden", "rest_in_garden"]),
    ("node89", "You face a final challenge. Do you confront it head-on or seek help?",
     ["confront", "seek_help"]),
    ("confront", "With courage, you conquer the challenge and become a legend.", []),
    ("seek_help", "You gather allies and together you overcome the final obstacle.", []),
]


for node_id, text, options, effects in nodes_data:
    game.add_node(node_id, text, options, effects)

# Start the game
game.start("start")

# Game loop
while not game.is_game_over():
    print(game.get_current_text())
    if game.current_node.options:
        choice = input("Enter your choice (0 or 1): ")
        game.make_choice(int(choice))
    else:
        break
