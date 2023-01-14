import git
import os

repo = git.Repo(os.getcwd())

# List the last 20 commits
for i, c in enumerate(repo.iter_commits('HEAD', max_count=20)):
    print(f'{i+1}: {c.summary}')

# Get user input for which commit to reset to
choice = input('Enter the number of the commit to reset to: ')
try:
    choice = int(choice)
except ValueError:
    print('Invalid input. Exiting.')
    exit()

# Get the chosen commit
chosen_commit = list(repo.iter_commits('HEAD', max_count=20))[choice-1]

# Soft reset to the chosen commit
repo.head.reset(commit=chosen_commit, index=True, working_tree=True)
