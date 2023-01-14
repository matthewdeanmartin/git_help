import git
import os

# Set up the Repo object using the current working directory
repo = git.Repo(os.getcwd())

# Get the blame for the file
file_path = "path/to/file"
blame = repo.git.blame(file_path)

# Create a dictionary to store the person -> emoji mapping
people = {}


emojis = [
"👨‍🔬",
"👨‍🍳",
"👨‍🎤",
"👨‍🎨",
"👨‍💻",
"👨‍🔧",
"👨",
"👨‍🌾",
"👨‍🏫",
"👨‍💼",
"👨‍🏭",
"👨‍🚀",
"👨‍🚒",
"👨‍🎓"]

# Parse the blame output and add people with corresponding emojis
for line in blame.splitlines():
    # Extract the person's name and email from the blame output
    name, email = line.split()[2:4]

    # Check if the person is already in the dictionary
    if (name, email) not in people:
        people[(name, email)] = emojis[len(people)-1]

    print(f"{people[(name, email)]}{name}<{email}> {line}")
