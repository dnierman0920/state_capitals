from ctypes.wintypes import BOOLEAN
import random 

states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}, {
    "name": "Arkansas",
    "capital": "Little Rock"
}, {
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Colorado",
    "capital": "Denver"
}, {
    "name": "Connecticut",
    "capital": "Hartford"
}, {
    "name": "Delaware",
    "capital": "Dover"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}, {
    "name": "Georgia",
    "capital": "Atlanta"
}, {
    "name": "Hawaii",
    "capital": "Honolulu"
}, {
    "name": "Idaho",
    "capital": "Boise"
}, {
    "name": "Illinois",
    "capital": "Springfield"
}, {
    "name": "Indiana",
    "capital": "Indianapolis"
}, {
    "name": "Iowa",
    "capital": "Des Moines"
}, {
    "name": "Kansas",
    "capital": "Topeka"
}, {
    "name": "Kentucky",
    "capital": "Frankfort"
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge"
}, {
    "name": "Maine",
    "capital": "Augusta"
}, {
    "name": "Maryland",
    "capital": "Annapolis"
}, {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "Michigan",
    "capital": "Lansing"
}, {
    "name": "Minnesota",
    "capital": "St. Paul"
}, {
    "name": "Mississippi",
    "capital": "Jackson"
}, {
    "name": "Missouri",
    "capital": "Jefferson City"
}, {
    "name": "Montana",
    "capital": "Helena"
}, {
    "name": "Nebraska",
    "capital": "Lincoln"
}, {
    "name": "Nevada",
    "capital": "Carson City"
}, {
    "name": "New Hampshire",
    "capital": "Concord"
}, {
    "name": "New Jersey",
    "capital": "Trenton"
}, {
    "name": "New Mexico",
    "capital": "Santa Fe"
}, {
    "name": "New York",
    "capital": "Albany"
}, {
    "name": "North Carolina",
    "capital": "Raleigh"
}, {
    "name": "North Dakota",
    "capital": "Bismarck"
}, {
    "name": "Ohio",
    "capital": "Columbus"
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
}, {
    "name": "Oregon",
    "capital": "Salem"
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
}, {
    "name": "Rhode Island",
    "capital": "Providence"
}, {
    "name": "South Carolina",
    "capital": "Columbia"
}, {
    "name": "South Dakota",
    "capital": "Pierre"
}, {
    "name": "Tennessee",
    "capital": "Nashville"
}, {
    "name": "Texas",
    "capital": "Austin"
}, {
    "name": "Utah",
    "capital": "Salt Lake City"
}, {
    "name": "Vermont",
    "capital": "Montpelier"
}, {
    "name": "Virginia",
    "capital": "Richmond"
}, {
    "name": "Washington",
    "capital": "Olympia"
}, {
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]

# Your program should prompt the user to identify the capital associated with a given state.
#  There should be running tallies on the number of correct and incorrect answers for each state
#   After getting through all 50 states one time, users should be asked whether or not they want to play again.

# *Provide a welcome message to introduce the player to the game.

print("Welcome to THE US STATE CAPITAL GAME! \nfollow the prompts and guess the capitals")

# *Make sure the states don't appear in alphabetical order in the prompts. 
# This will make the game a bit more challenging for the user.
def shuffle_states():
    random.shuffle(states)

# *Initialize new keys in the dictionaries that store the number of times a user gets a capital correct 
# and the number of times the answer is wrong.
def create_tally(correct: bool, index: int):
    if(correct):
        if "correct_tally" in states[index]: states[index]["correct_tally"] += 1
        else: states[index]["correct_tally"] = 1
    else:
        if "wrong_tally" in states[index]: states[index]["wrong_tally"] += 1
        else: states[index]["wrong_tally"] = 1

        







##########################################     REQUIREMENTS    ############################################



# *Initialize new keys in the dictionaries that store the number of times a user gets a capital correct 
# and the number of times the answer is wrong.

# *Through all 50 states, prompt the user to name the capital of the state.

# *If the answer is correct, display a message saying so, and increment the correct key.

# *If the answer is wrong, display a message saying so, and increment the wrong key.

# *After each prompt, display a message telling the reader how many times the state was answered
#  correctly out of the total number of times answered.

# *Once the user has gone through all 50 states, ask them if they'd like to play again.

# *Getting Started You're given an array of dictionaries that contain each state name and capital.

# *Hint: For the purposes of developing this program, start with a test array of three dictionaries
#  so you don't have to play through all 50 states each time.

# Potentially Useful Methods *print *input *for loop *sorted *random.shuffle()

# Bonus! Calculate a overall total score, display a running tally for each prompt If the user plays again,
#  set the order of how the prompts appear to start with the ones they got wrong the most often. 
# Add a hint functionality that prints the first 3 letters of a capital