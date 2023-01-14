import git
import os

# Set up the Repo object using the current working directory
repo = git.Repo(os.getcwd())

# Fetch the remote branches
origin = repo.remote('origin')
origin.fetch()

# Check if the remote main branch has changed
remote_main = repo.create_head('main', origin.refs.main)
local_main = repo.heads.main

if local_main.commit != remote_main.commit:
    print("Remote main branch has changed, please pull the changes first.")
    exit()

# Stage all changed files
repo.git.add(A=True)

# Prompt the user for a commit message
commit_message = input("Enter a commit message: ")

# Commit the changes
repo.index.commit(commit_message)

# Push the changes
origin.push()

print("Commit and push successful!")
