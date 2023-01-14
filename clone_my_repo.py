from github import Github
import getpass
import git

username = input("Enter your Github username: ")
password = getpass.getpass("Enter your Github password: ")

# Connect to Github using the provided credentials
g = Github(username, password)

# Get the user's repository
user = g.get_user()
repos = user.get_repos()

# List the user's repositories
for i, repo in enumerate(repos):
    print(f"{i+1}: {repo.name}")

# Get user input for which repository to clone
choice = input("Enter the number of the repository you want to clone: ")
try:
    choice = int(choice)
except ValueError:
    print("Invalid input. Exiting.")
    exit()

# Get the chosen repository
chosen_repo = repos[choice-1]

# Clone the repository
local_path = '/path/to/local/directory'
repo = git.Repo.clone_from(chosen_repo.ssh_url, local_path)
