import requests

package = requests.get("https://pokeapi.co/api/v2/pokemon/mewtwo")

pokemons = package.json()

print(pokemons["abilities"])