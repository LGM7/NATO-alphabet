import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

# Loop through rows of a data frame
for (index, rows) in df.iterrows():
    # TODO 1. Create a dictionary in this format:
    # {"A": "Alfa", "B": "Bravo"}
    df_dict = {rows.letter: rows.code for (index, rows) in df.iterrows()}
print(df_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_name = input("What is the name?\n").upper()
name_list = list(input_name)

# TODO 2. Run a loop to check if the alphabets exist in the dictionary and provide the relative NATO pairs
output_list = []
for a in name_list:
    for (key, value) in df_dict.items():
        if a == key:
            output_list.append(value)
print(output_list)

