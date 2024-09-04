import os
import pandas as pd
from anime_funcs import add_to_csv, delete_from_csv, exit_program, search_csv, show_csv, update_csv
from enum import Enum  # נייבא רק את Enum כאן

# Create the menu options in Enum
class Selection(Enum):
    ADD = 1
    DELETE = 2
    SHOW = 3
    EXIT = 4
    UPDATE = 5
    SEARCH = 6

# Function to display the menu and return the user's selection
def menu():
    print("Displaying menu")  # Debugging print
    for i in Selection:
        print(f'{i.value}-{i.name}')
    return Selection(int(input('Your selection: ')))

# Check if the CSV file exists
csv_file = 'Anime.csv'
if not os.path.exists(csv_file):
    data = {'Anime Name': [], 'Character Name': []}
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    print(f"CSV file '{csv_file}' created successfully!")
else:
    print(f"CSV file '{csv_file}' already exists.")

# Main loop to run the menu
if __name__ == '__main__':
    while True:
        user_selection = menu()
        if user_selection == Selection.ADD:add_to_csv()
        elif user_selection == Selection.DELETE:delete_from_csv()
        elif user_selection == Selection.SHOW:show_csv()
        elif user_selection == Selection.EXIT:exit_program()
        elif user_selection == Selection.UPDATE: update_csv()
        elif user_selection == Selection.SEARCH:search_csv()