
# Anime CRUD CSV Application

This Python-based CRUD (Create, Read, Update, Delete) application allows users to manage a list of anime and their characters stored in a CSV file. The application provides an interactive menu that lets users perform actions such as adding, deleting, updating, searching, and displaying anime entries.

## Features

- **Add Anime**: Add a new anime and its main character to the CSV file.
- **Delete Anime**: Delete an existing anime from the CSV file.
- **Show All Anime**: Display all the anime entries stored in the CSV file.
- **Update Anime**: Update the name of an anime and/or its main character.
- **Search Anime**: Search for a specific anime by its name.
- **Exit**: Exit the application while saving data to the CSV file.

## Installation

To set up the application on your local machine, follow these steps:

### Prerequisites

- Python 3.x must be installed on your machine.

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/anime-crud-csv.git
   cd anime-crud-csv
   ```

2. **Install the required dependencies**:

   Install the dependencies listed in the `requirements.txt` file by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

   These dependencies include:
   - `pandas` for working with the CSV file.
   - Other libraries like `numpy`, `pytz`, and more.

3. **Run the application**:
   ```bash
   python Main.py
   ```

   The application will automatically create an `Anime.csv` file if one doesn't exist.

## Project Structure

- **Main.py**: The main file that contains the loop of the application and handles the menu system for the user interactions.
- **anime_funcs.py**: Contains all the CRUD operations (create, read, update, delete) and additional functions to work with the CSV file.
- **Anime.csv**: The file where the data (anime names and character names) is stored. This file will be generated automatically if it doesn't already exist.
- **requirements.txt**: Lists the Python packages required to run the application.

## Usage

Once the application is running, the user is presented with an interactive menu:

```text
1 - ADD
2 - DELETE
3 - SHOW
4 - EXIT
5 - UPDATE
6 - SEARCH
```

Choose the desired operation by typing the corresponding number and following the on-screen prompts.

### Example Commands:

- **Add Anime**: The program will ask for the anime name and its main character. It will add this entry to the CSV file.
- **Delete Anime**: Enter the name of the anime you wish to delete, and the program will remove it from the file.
- **Show All Anime**: Display the entire list of stored anime and their main characters.
- **Update Anime**: Allows you to update the anime name or its main character.
- **Search Anime**: Enter the anime name to search for specific entries.

## Code Overview

### Main.py

This file starts by importing the necessary libraries (`os`, `pandas`, and the functions from `anime_funcs.py`) and displays a menu for the user to choose options.

Key functions include:
- `menu()`: Displays the available options and returns the user’s selection.
- The main loop (`while True`) continuously presents the menu and calls the appropriate functions from `anime_funcs.py` based on the user's selection.

### anime_funcs.py

This file contains the core functionality for handling the CSV file.

- `clean_data(df)`: Cleans the data by trimming spaces, capitalizing names, and removing duplicates.
- `add_to_csv()`: Adds a new anime and its main character to the CSV file.
- `show_csv()`: Displays all entries stored in the CSV file.
- `delete_from_csv()`: Deletes an anime entry from the CSV file.
- `update_csv()`: Updates an existing anime entry in the CSV file.
- `search_csv()`: Searches for an anime by name.
- `exit_program()`: Exits the program safely.

## Example of Adding a New Anime

```text
Enter the name of the Anime: Naruto
Enter the name of the Character: Naruto Uzumaki
```

This will add the anime "Naruto" and its main character "Naruto Uzumaki" to the `Anime.csv` file.

## Example Code:

### clean_data():
This function cleans the data in the CSV file by trimming spaces, capitalizing names, and removing duplicates.

```python
def clean_data(df):
    if 'Anime Name' in df.columns and 'Character Name' in df.columns:
        df['Anime Name'] = df['Anime Name'].str.strip().str.title()
        df['Character Name'] = df['Character Name'].str.strip().str.title()
        df.drop_duplicates(subset=['Anime Name'], keep='first', inplace=True)
    else:
        print("Error: 'Anime Name' or 'Character Name' column is missing.")
    return df
```

### add_to_csv():
This function adds a new anime and its character to the CSV file.

```python
def add_to_csv():
    anime_name = input('Enter the name of the Anime: ').strip().title()
    character_name = input('Enter the name of the Character: ').strip().title()
    df = pd.DataFrame([[anime_name, character_name]], columns=['Anime Name', 'Character Name'])
    
    if not os.path.isfile(csv_file):
        df.to_csv(csv_file, index=False)
        print(f"Created new CSV file: {csv_file}")
    else:
        existing_df = pd.read_csv(csv_file)
        combined_df = pd.concat([existing_df, df], ignore_index=True)
        cleaned_df = clean_data(combined_df)
        cleaned_df.to_csv(csv_file, index=False)
        print(f"Appended to existing CSV file: {csv_file}")
    print('The Anime was added to the CSV file.')
```

### delete_from_csv():
This function deletes an anime entry from the CSV file based on the anime name provided by the user.

```python
def delete_from_csv():
    if not os.path.isfile(csv_file):
        print("CSV file not found.")
        return

    df = pd.read_csv(csv_file)
    anime_to_delete = input("Enter the name of the Anime to delete: ").strip().title()

    if 'Anime Name' in df.columns:
        df = clean_data(df)
        if anime_to_delete in df['Anime Name'].values:
            df = df[df['Anime Name'] != anime_to_delete]
            df.to_csv(csv_file, index=False)
            print(f'{anime_to_delete} was deleted from the CSV.')
        else:
            print(f'{anime_to_delete} was not found in the CSV.')
    else:
        print("'Anime Name' column not found in the CSV.")
```

### Dependencies

- `pandas` (2.2.2): Used for managing and manipulating the CSV file.
- `numpy` (2.1.0): Included in the requirements but not directly used in the current code.
- Other libraries are included as dependencies, but may not be directly relevant to this project (like `Flask`, `Werkzeug`).

You can view the complete list of dependencies in the `requirements.txt` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
