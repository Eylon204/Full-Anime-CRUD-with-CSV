import os
import pandas as pd

csv_file = 'Anime.csv'

# Function to clean the anime names and character names
def clean_data(df):
    # Check if 'Anime Name' and 'Character Name' exist before cleaning
    if 'Anime Name' in df.columns and 'Character Name' in df.columns:
        df['Anime Name'] = df['Anime Name'].str.strip().str.title()  # Strip spaces and title case
        df['Character Name'] = df['Character Name'].str.strip().str.title()  # Strip spaces and title case
        df.drop_duplicates(subset=['Anime Name'], keep='first', inplace=True)  # Remove duplicate anime names
    else:
        print("Error: 'Anime Name' or 'Character Name' column is missing.")
    return df

# Function to add a new Anime to the CSV file
def add_to_csv():
    anime_name = input('Enter the name of the Anime: ').strip().title()  # Normalize input
    character_name = input('Enter the name of the Character: ').strip().title()  # Normalize input
    df = pd.DataFrame([[anime_name, character_name]], columns=['Anime Name', 'Character Name'])
    
    if not os.path.isfile(csv_file):
        df.to_csv(csv_file, index=False)
        print(f"Created new CSV file: {csv_file}")
    else:
        existing_df = pd.read_csv(csv_file)
        combined_df = pd.concat([existing_df, df], ignore_index=True)  # Add new entry
        cleaned_df = clean_data(combined_df)  # Clean the data
        cleaned_df.to_csv(csv_file, index=False)
        print(f"Appended to existing CSV file: {csv_file}")
    print('The Anime was added to the CSV file.')

# Function to display the contents of the CSV file
def show_csv():
    if os.path.isfile(csv_file):
        df = pd.read_csv(csv_file)
        print(df.columns)  # Debugging print to check the columns in the CSV file
        if 'Anime Name' in df.columns and 'Character Name' in df.columns:
            cleaned_df = clean_data(df)  # Clean the data before displaying
            print(cleaned_df)
        else:
            print("Error: 'Anime Name' or 'Character Name' column is missing from the CSV file.")
    else:
        print("CSV file not found.")

# Function to delete an Anime from the CSV file
def delete_from_csv():
    if not os.path.isfile(csv_file):
        print("CSV file not found.")
        return
    df = pd.read_csv(csv_file)
    print(df.columns)
    anime_to_delete = input("Enter the name of the Anime to delete: ").strip().title()  # Normalize input

    if 'Anime Name' in df.columns:
        df = clean_data(df)  # Clean the data before deleting
        if anime_to_delete in df['Anime Name'].values:
            df = df[df['Anime Name'] != anime_to_delete]
            df.to_csv(csv_file, index=False)
            print(f'{anime_to_delete} was deleted from the CSV.')
        else:
            print(f'{anime_to_delete} was not found in the CSV.')
    else:
        print("'Anime Name' column not found in the CSV.")

# Function to update an existing Anime in the CSV file
def update_csv():
    if not os.path.isfile(csv_file):
        print('CSV file not found.')
        return
    df = pd.read_csv(csv_file)
    print(df.columns)
    anime_to_update = input('Enter the name of the Anime to update: ').strip().title()  # Normalize input

    if 'Anime Name' in df.columns:
        df = clean_data(df)  # Clean the data before updating
        if anime_to_update in df['Anime Name'].values:
            new_anime_name = input('Enter new Anime name (or press Enter to skip): ').strip().title()
            new_character_name = input('Enter new Character name (or press Enter to skip): ').strip().title()

            if new_anime_name:
                df.loc[df['Anime Name'] == anime_to_update, 'Anime Name'] = new_anime_name
            if new_character_name:
                df.loc[df['Anime Name'] == anime_to_update, 'Character Name'] = new_character_name

            df.to_csv(csv_file, index=False)
            print(f'{anime_to_update} was updated.')
        else:
            print(f'{anime_to_update} was not found in the CSV.')
    else:
        print("'Anime Name' column not found in the CSV.")

# Function to search for an Anime in the CSV file
def search_csv():
    if not os.path.isfile(csv_file):
        print('CSV file not found.')
        return
    df = pd.read_csv(csv_file)
    print(df.columns)
    search_query = input('Enter the name of the Anime to search: ').strip().title()  # Normalize input

    if 'Anime Name' in df.columns:
        df = clean_data(df)  # Clean the data before searching
        if search_query in df['Anime Name'].values:
            result = df[df['Anime Name'] == search_query]
            print(result)
        else:
            print(f'{search_query} was not found in the CSV.')
    else:
        print("'Anime Name' column not found in the CSV.")

# Function to exit the program
def exit_program():
    print("Saving data and exiting...")
    exit()