import random

def generate_state_name():
    state_prefixes = ["Andhra", "Arunachal", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat",
                      "Haryana", "Himachal", "Jharkhand", "Karnataka", "Kerala", "Madhya", "Maharashtra",
                      "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
                      "Sikkim", "Tamil", "Telangana", "Tripura", "Uttar", "Uttarakhand", "West"]

    state_suffixes = [" Pradesh", " Pradesh", " Pradesh", " Nadu", " Pradesh", " Bengal", " Pradesh", " Pradesh",
                      " Pradesh", " Pradesh", " Pradesh", " Pradesh", " Pradesh", " Pradesh", " Pradesh",
                      " Pradesh", " Pradesh", " Pradesh", " Pradesh", " Pradesh", " Pradesh", " Pradesh",
                      " Pradesh", " Nadu", " Pradesh", " Pradesh", " Pradesh", " Pradesh"]

    state_name = random.choice(state_prefixes) + random.choice(state_suffixes)
    return state_name

if __name__ == "__main__":
    num_names = int(input("Enter the number of unique state names you want to generate: "))

    unique_state_names = set()
    while len(unique_state_names) < num_names:
        state_name = generate_state_name()
        unique_state_names.add(state_name)

    print("\nGenerated Unique State Names:")
    for state_name in unique_state_names:
        print(state_name)
