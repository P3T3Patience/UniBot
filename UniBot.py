'''Build a chat bot for a student starting university. Use a real university as a reference point and design the bot to contact
 the relevant people and access the relevant places, etc'''
from SurreyUni import *

print("\nHi! I'm UniBot")
print(f"\n I'm here to help you with anything you may need to get you settled into university life here at the wonderful {university}.")

# Easter eggs
name = input("\n First off, what's your name?: ")
name = name.lower()
if name == "peter":
    print("\nPeter is the best name!\n")

if name == "obi wan":
    print("\n Hello there Obi Wan Kenobi! Or do you mean Old Ben Kenobi..?\n")
    name = "Master Kenobi"
name = name.title()

# Asking for what they need information on 
print(f"If you have a question {name}, ask it below. Type done when you're finished.")
question = ""

while question != "done":
    question = input("\n What is your question?: ")
    question = question.lower()

    if "address" in question:
        print(question)
        print(f"Well {name} Here are the contact details for the main university reception, they should be able to help:-\n")
        print(address)
        print(reception_tel)

    if "contact" in question:
        print(f"\n Well {name}, Here are the contact details for the main university reception, they should be able to help:-\n")
        print(address)
        print(reception_tel)
        print(f"If I can help with anything else {name}, just ask below. If not, type done when you're finished.")
    if "map" in question:
        print("\n A campus map can be found here: https://www.surrey.ac.uk/visit-university/our-campus")
        print(f"If I can help with anything else {name}, just ask below. If not, type done when you're finished.")

    if "finding" in question:
        print(f"\n A campus map can be found here: {campus_map}")
        print(f"If I can help with anything else {name}, just ask below. If not, type done when you're finished.")

    if "term dates" in question:
        print(f"Here are the key dates here at {university}:-")
        print(term_dates)
        print("\nFor more key dates, try: " + key_dates_link)
        print(f"If I can help with anything else {name}, just ask below. If not, type done when you're finished.")

    if "when is" in question:
        print(f"Here are the key dates here at {university}:-")
        print(term_dates)
        print("\nFor more key dates, try: " + key_dates_link)
        print(f"If I can help with anything else {name}, just ask below. If not, type done when you're finished.")

    if "supermarket" in question:
        print(f"There are a variety of options for food available, see them all here:- \n {food}")
        print(f"If I can help with anything else {name}, just ask below. If not, type done when you're finished.")    
    
    if "food" in question:
        print(f"\nThere are a variety of options for food available, see them all here:- \n {food}")
        print(f"\nIf I can help with anything else {name}, just ask below. If not, type done when you're finished.")    

    else:
        print("Sorry I'm not sure how to help.. Try re-wording your question.")
        print(f"If I can help with anything else {name}, just ask below. If not, type done when you're finished.")

# Escape from loop
if name == "Master Kenobi":
    print("It's over, you have the high ground.. Bye!")
else:
    print(f"\n Thanks for the memories {name}.. Have a great time here at {university}! Bye now!\n")