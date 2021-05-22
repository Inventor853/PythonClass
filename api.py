import requests

name = input("What is the name of the pokemon? ")

package = requests.get("https://pokeapi.co/api/v2/pokemon/" + name)

if package.text == "Not Found":
    print("There is no such pokemon")
else:
    pokemon = package.json()

    print(pokemon)