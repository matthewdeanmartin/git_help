import git
import os

# Set up the Repo object using the current working directory
repo = git.Repo(os.getcwd())

# Fetch the remote branch
origin = repo.remote('origin')
origin.fetch()

# Pull the changes from the remote main branch
origin.pull(refspec='main:main')



"""
# Alternative method
from git import Git

git = Git(os.getcwd())
git.pull("origin", "main")
"""