import json
import difflib

#This method takes in a word.  It checks to see if the lowercase version of the word is in the 
#data.json file.  If the word is found it returns the definitions found.  If the word is not found
#it checks to see if there are any close mataches and ask the user if that what they mean and return the
#definition is so.
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

#Enables access to data in json file
data = json.load(open("data.json"))

word = input("Please enter a word:\n")
definition = dictionary(word)
if definition:
    for i in definition:
        print(i)
