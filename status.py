import git
import os

# Set up the Repo object using the current working directory
repo = git.Repo(os.getcwd())

# Get the status of the repository
status = repo.git.status()

# Print the status with emojis
print("🎉 Git Status 🎉")
print("\n🚚 Tracking:")
print(status)

if repo.is_dirty():
    print("\n🚫 Uncommitted changes:")
else:
    print("\n🚀 Clean and committed! 🚀")
