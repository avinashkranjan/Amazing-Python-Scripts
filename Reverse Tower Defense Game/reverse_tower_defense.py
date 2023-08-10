import random

# Enemy types with varying attack capabilities
ENEMY_TYPES = [
    {"name": "Goblin", "damage": 20, "chance_to_evade": 0.1},
    {"name": "Orc", "damage": 30, "chance_to_evade": 0.15},
    {"name": "Troll", "damage": 40, "chance_to_evade": 0.2},
]

# Special attacks with cooldown periods
SPECIAL_ATTACKS = [
    {"name": "Fireball", "damage": 50, "cooldown": 3},
    {"name": "Lightning Strike", "damage": 60, "cooldown": 5},
    {"name": "Ice Nova", "damage": 45, "cooldown": 4},
    {"name": "Poison Dart", "damage": 40, "cooldown": 3},
]

# Initialize game variables
level = 1
total_points = 0
enemy_type = ENEMY_TYPES[0]
special_attack_cooldown = 0


def setup_defenses():
    defenses = []
    for i in range(5):
        defense_strength = random.randint(50 + 10*level, 100 + 10*level)
        defenses.append(defense_strength)
    return defenses


def choose_enemy_type():
    global enemy_type
    enemy_type = random.choice(ENEMY_TYPES)


def use_special_attack():
    global special_attack_cooldown
    if special_attack_cooldown == 0:
        special_attack = random.choice(SPECIAL_ATTACKS)
        special_attack_cooldown = special_attack["cooldown"]
        print(
            f"Used {special_attack['name']}! It deals {special_attack['damage']} damage!")
        return special_attack["damage"]
    else:
        print("Special attack is on cooldown. Keep attacking the defenses!")
        return 0


def upgrade_enemy():
    global enemy_type
    enemy_type_index = ENEMY_TYPES.index(enemy_type)
    if enemy_type_index < len(ENEMY_TYPES) - 1:
        enemy_type = ENEMY_TYPES[enemy_type_index + 1]
        print(
            f"You upgraded to {enemy_type['name']}. They deal more damage now!")


def attack(defenses):
    global special_attack_cooldown, total_points
    total_defense_strength = sum(defenses)
    print(f"Current defenses: {defenses}")
    print(f"Total defense strength: {total_defense_strength}")

    if total_defense_strength <= 0:
        print("Congratulations! You breached the defenses!")
        total_points += 100 + 20 * level
        return True
    else:
        while True:
            print("\nChoose your action:")
            print("1. Normal Attack")
            print("2. Use Special Attack")
            print("3. Upgrade Enemy Type")
            action = input("Enter the number of your action: ")

            if action == "1":
                damage = enemy_type["damage"]
                if random.random() < enemy_type["chance_to_evade"]:
                    print(f"{enemy_type['name']} evaded your attack!")
                    damage = 0
                else:
                    print(
                        f"You attacked the defenses and caused {damage} damage!")
                defenses[random.randint(0, len(defenses) - 1)] -= damage
                return False

            elif action == "2":
                damage = use_special_attack()
                defenses[random.randint(0, len(defenses) - 1)] -= damage
                return False

            elif action == "3":
                upgrade_enemy()
                return False

            else:
                print("Invalid input. Please enter a valid action number.")


def main():
    global level, total_points, special_attack_cooldown

    print("Welcome to the Reverse Tower Defense Game!")
    print("You are controlling the enemy horde trying to breach the AI's defenses.")

    while True:
        print(f"\n--- Level {level} ---")

        defenses = setup_defenses()
        points = 0
        special_attack_cooldown = 0

        while True:
            if attack(defenses):
                level += 1
                total_points += points
                break

            if special_attack_cooldown > 0:
                special_attack_cooldown -= 1

            print("\nChoose the defense you want to attack:")
            for i in range(len(defenses)):
                print(f"{i+1}. Defense {i+1} - Strength: {defenses[i]}")

        print(f"\nLevel {level-1} completed!")
        print(f"Points earned in Level {level-1}: {points}")
        print(f"Total points: {total_points}")

        play_again = input(
            "Do you want to play the next level? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing! Game Over!")


if __name__ == "__main__":
    main()
