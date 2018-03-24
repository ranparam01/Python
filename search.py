import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    word= word.lower()
    if word in data:
        return (data[word])
    elif len(get_close_matches(word, data.keys()))>0:
        yn= input("Did you mean %s instead? Enter Y for yes and N for No:  "%get_close_matches(word,data.keys())[0])
        yn=yn.lower()
        if yn=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="n":
            return "The word doesnt exist in our data dictionary"
        else:
            return "We did not understand your entry"
    else:
        return "The word doesnt exist"

word= input("Enter the search text :")
output=translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
