import requests

def search_character(name):
    url = f"https://api.api-onepiece.com/v2/characters/en?search={name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # This is likely a list, not a dict
        if len(data) > 0:
            return data[0]  # First matching character
        else:
            print(f"⚠️ No match found for '{name}'.")
            return None
    else:
        print("❌ API error. Please check your connection.")
        return None

def display_character(character):
    print("\n=== 🧭 ONE PIECE CHARACTER ===")
    print(f"  Name     : {character.get('name')}")
    print(f"  Crew     : {character.get('crew')}")
    print(f"  Role     : {character.get('role')}")
    print(f"  Bounty   : {character.get('bounty')}")
    print(f"  Fruit    : {character.get('fruit')}")
    print("==============================\n")

def run_search():
    while True:
        name = input("🔎 Enter character name (or 'q' to quit): ").strip().lower()
        if name == "q":
            print("👋 Thanks for exploring the Grand Line!")
            break

        character = search_character(name)
        if character:
            display_character(character)


if __name__ == "__main__":
    run_search()
