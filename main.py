import art, game_data, random

def format_data(data):
    """Formats the data in name, description and country."""
    data_name = data["name"]
    data_description = data["description"]
    data_country = data["country"]
    return f"{data_name}, a {data_description}, from {data_country}."

def random_index():
    """Randomly choose a number from 0 - 49 (inclusive) for an index."""
    return random.randint(0, 49)

def game(a_index, b_index, score):
    a = game_data.data[a_index]
    b = game_data.data[b_index]
    a_count = a["follower_count"]
    b_count = b["follower_count"]

    print("Compare A: " + format_data(a))
    print(f"{art.vs}")
    print("Against B: " + format_data(b))

    ans = input("Who has more followers? Type 'A' or 'B': ").upper()

    if (a_count > b_count and ans == 'A') or (a_count < b_count and ans == 'B'):
        new_random_index = random_index()
        if new_random_index == a_index or new_random_index == b_index:
            new_random_index = random_index()
        print("\n" * 20) #clear the screen
        print(art.logo)
        print(f"You're right! Current score: {score + 1}.")
        game(b_index, new_random_index, score + 1)
    else:
        print("\n" * 20) #clear the screen
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}.")

print(art.logo)
game(random_index(), random_index(), 0)