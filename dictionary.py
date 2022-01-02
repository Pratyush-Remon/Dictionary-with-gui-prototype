import json
from difflib import get_close_matches

data=json.load(open("C:\\Users\\lenovo pc\\python\\dictionary\\dic.json"))

def translate(w):
    w=w.lower()

    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        response=input("Do you mean %s instead?[Y/N]"%get_close_matches(w,data.keys())[0])
        response=response.upper()
        if response=='Y':
            print(get_close_matches(w,data.keys())[0])
        elif response=='N':
            print("Word don't exists in our dictionary")
        else:
            print("We can't understand your response")
    else:
        print("Word doesn't exist in our dictionary")

word=input("Enter the word you desire to know the meaning of:")
output=translate(word)
def display(t):
    if type(t)=='list':
         for item in list:
               print(item)
    else:
        print(t)

display(output)
