import git
import os

# Set up the Repo object using the current working directory
repo = git.Repo(os.getcwd())

# Get the status of the repository
status = repo.git.status()

# Print the status with emojis
print("š Git Status š")
print("\nš Tracking:")
print(status)

if repo.is_dirty():
    print("\nš« Uncommitted changes:")
else:
    print("\nš Clean and committed! š")
