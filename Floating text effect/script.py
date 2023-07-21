import time

# Function to print floating text


def print_floating_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Adjust the sleep duration for desired speed
    print()


# Installation process
print_floating_text("Hi, I am Shivansh Jain.")
time.sleep(1)  # Simulating a delay
print_floating_text("I am a Computer Science student.")
time.sleep(1)  # Simulating a delay
print_floating_text(
    "I have added this python script which creates floating text effects.")
time.sleep(1)  # Simulating a delay
print_floating_text(
    "I know full stack web development using HTML, CSS, Javascript, Django.")
time.sleep(1)  # Simulating a delay
print_floating_text("I like cricket, music and mythology.")

# Further code execution
print("Continuing with further code execution...")
# ... Rest of the code ...
