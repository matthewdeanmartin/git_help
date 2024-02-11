import git

repo = git.Repo(".")
commits = list(repo.iter_commits())

for commit in commits:
    author = commit.author
    date = commit.committed_datetime.strftime("%x")
    message = commit.message.strip()
    changes = []
    for diff in commit.diff(create_patch=True):
        for line in diff.diff.split("\n"):
            if line.startswith("+") or line.startswith("-"):
                changes.append(line)

    print("Author: %s <%s>" % (author.name, author.email))
    print("Date: %s" % date)
    print("Full Comment: %s" % message)
    for change in changes:
        print("    %s" % change[1:])
    print("\n")
