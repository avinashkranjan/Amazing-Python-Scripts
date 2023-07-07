import random

# Lists of story elements
characters = ['Alice', 'Bob', 'Charlie', 'Eve']
settings = ['a small town', 'a mysterious castle',
            'a futuristic city', 'an enchanted forest']
actions = ['discovered a hidden treasure', 'solved a puzzling mystery',
           'overcame their fears', 'saved the world']
conclusions = ['and they lived happily ever after.',
               'and they vowed to continue their adventures.', 'and they returned home, forever changed.']

# Generate a random story


def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    action = random.choice(actions)
    conclusion = random.choice(conclusions)

    story = f"Once upon a time, {character} found themselves in {setting}. They {action} {conclusion}"

    return story


# Generate and print a story
story = generate_story()
print(story)
