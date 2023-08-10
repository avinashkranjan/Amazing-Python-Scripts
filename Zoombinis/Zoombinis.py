import random

# Constants
ZOOMBINIS_COUNT = 16
ZOOMBINIS_PER_TEAM = 8

# Functions


def setup_teams():
    teams = []
    for i in range(2):
        team = []
        for _ in range(ZOOMBINIS_PER_TEAM):
            team.append(random.randint(1, 4))
        teams.append(team)
    return teams


def display_teams(teams):
    for i, team in enumerate(teams, start=1):
        print(f"Team {i}: {team}")


def main():
    print("Welcome to Zoombinis!")
    teams = setup_teams()

    while True:
        display_teams(teams)
        team_choice = int(input("Select a team (1 or 2): "))

        if team_choice < 1 or team_choice > 2:
            print("Invalid team choice. Please select 1 or 2.")
            continue

        selected_team = teams[team_choice - 1]
        zoombini_choice = int(input("Select a Zoombini (1-8): "))

        if zoombini_choice < 1 or zoombini_choice > 8:
            print("Invalid Zoombini choice. Please select a number between 1 and 8.")
            continue

        zoombini = selected_team[zoombini_choice - 1]
        print(f"Selected Zoombini: {zoombini}")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("Thanks for playing Zoombinis!")
            break


if __name__ == "__main__":
    main()
