import requests
class GitHubPIError(Exception):
    pass

def get_user_repos(user_id):
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        raise GitHubPIError("User not found")
    
    data= response.json()
    return [repo["name"]for repo in data]
def get_commit_count(user_id, repo_name):
    url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code !=200:
        raise GitHubPIError("Repo not found")
    return len(response.json())

def get_repo_commit_summary(user_id):
    repos= get_user_repos(user_id)
    summary = []

    for repo in repos:
        count = get_commit_count(user_id, repo)
        summary.append((repo,count))

    return summary

def display_summary(summary):
    for repo, count in summary:
        print(f"Repo: {repo} Number of Commits: {count}")

if __name__ == "__main__":
    user= input("Enter GitHub user id:")
    result= get_repo_commit_summary(user)
    display_summary(result)
