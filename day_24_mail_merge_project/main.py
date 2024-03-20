# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt", mode="r") as file:
    letter_recipients = file.readlines()

with open("Input/Letters/starting_letter.txt", mode="r") as file:
    initial_letter = file.read()

for recipient in letter_recipients:
    format_name = recipient.strip()

    with open(f"Output/ReadyToSend/letter_for_{format_name}", mode="w") as file:
        personalized_letter = initial_letter .replace("[name]", f"{format_name}")
        file.write(personalized_letter)
