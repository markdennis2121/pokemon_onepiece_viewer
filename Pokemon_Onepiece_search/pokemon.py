import requests

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def display(pokemon_data):
    print(" ")
    print("=== POKEMON ===")
    print(f"  Name   : {pokemon_data['name'].capitalize()}")
    print(f"  ID     : {pokemon_data['id']}")
    print(f"  Weight : {pokemon_data['weight']}")
    print(f"  Height : {pokemon_data['height']}")
    print("===============")
    print(" ")
def main():
    while True:
        pokemon_name = input("🔎 Enter Pokémon name (or 'q' to quit): ").lower().strip()
        if pokemon_name == 'q':
            print("👋 Goodbye, trainer!")
            break

        info = get_pokemon_info(pokemon_name)
        if info:
            display(info)
        else:
            print(f"⚠️ No Pokémon found with the name '{pokemon_name}'. Try again.")

if __name__ == "__main__":
    main()