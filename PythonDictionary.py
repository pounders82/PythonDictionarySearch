import json
import difflib

def dictionary(word):
    if word.lower() in data:
        return data[word.lower()]
    else:
        matches = difflib.get_close_matches(word.lower(), data)
        if not matches:
            print("That word is not in the dictionary")
        else:
            answer = (input("Did you mean "+ matches[0]+"? [y/n]"))

            if answer == "y":
                return data[matches[0]]

            else:
                print("That word is not in the dictionary")

data = json.load(open("data.json"))
print(data["rain"])

word = input("Please enter a word:\n")
definition = dictionary(word)
if definition:
    for i in definition:
        print(i)
