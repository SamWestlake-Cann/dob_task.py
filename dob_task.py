# Store variable names + birth_dates in a list
names = []
birth_dates = []

# Open DOB.txt in readlines
with open("DOB.txt", "r") as text_file:
    data = text_file.readlines()

# Store birth dates + names
for line in data:
    parts = line.split()
    # Append from beginning to 2nd word
    names.append(parts[:2]) 
    # Append from 2nd word to the end of line 
    birth_dates.append(parts[2:])  

# Close DOB.txt file
text_file.close()

# Print the title Name followed by the names
print("Name")
for i, names in enumerate(names, start=1):
    print("{}. {}".format(i, " ".join(names)))

# Create space between Name and birth dates
print("")

# Print the title Birthdate followed by the birth dates
print("Birthdate")
for i, birth_dates in enumerate(birth_dates, start=1):
    print("{}. {}".format(i, " ".join(birth_dates)))