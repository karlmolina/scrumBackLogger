from github import Github

g = Github("karlgmolina@gmail.com", "just3min")

for repo in g.get_user().get_repos():
    print(repo.name)