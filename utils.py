import configparser
import os
import re
import subprocess
import sys

import requests


def print_error(msg: str):
    print(f"\033[1;91mError: {msg}\033[0m", file=sys.stderr)


def print_warning(msg: str):
    print(f"\033[1;93Warning: {msg}\033[0m", file=sys.stderr)


def print_info(msg: str):
    print(f"\033[1;94mInfo: {msg}\033[0m")


def print_success(msg: str):
    print(f"\033[1;92mSuccess: {msg}\033[0m")


def get_projet_prs(token, branch):
    p = subprocess.Popen(
        "git rev-parse --show-toplevel", stdout=subprocess.PIPE, shell=True
    )
    (output, _) = p.communicate()
    _ = p.wait()
    repo = os.path.basename(output.decode()).strip()
    owner = get_github_owner_from_git()

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    params = {
        "head": f"{owner}:{branch}",
    }
    response = requests.get(url, params=params, headers=headers)

    if not response.ok:
        print(
            f"Unable to get pull requests ({response.status_code}): {response.reason}",
            file=sys.stderr,
        )
        exit(1)
    jsonObj = response.json()

    if len(jsonObj) <= 0:
        return None

    return jsonObj


def get_pr(token, branch):
    prs = get_projet_prs(token, branch)
    if prs is None:
        return None
    pr_number = prs[0]["number"]

    p = subprocess.Popen(
        "git rev-parse --show-toplevel", stdout=subprocess.PIPE, shell=True
    )
    (output, _) = p.communicate()
    _ = p.wait()
    repo = os.path.basename(output.decode()).strip()
    owner = get_github_owner_from_git()

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    params = {
        "head": f"{owner}:{branch}",
    }
    response = requests.get(url, params=params, headers=headers)

    if not response.ok:
        print(
            f"Unable to get the pull request #{pr_number} ({response.status_code}): {response.reason}",
            file=sys.stderr,
        )
        exit(1)
    jsonObj = response.json()

    return jsonObj


def get_github_owner_from_git():
    # Get the remote URL of the Git repository
    try:
        remote_url_bytes = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"]
        )
        remote_url = remote_url_bytes.decode().strip()
    except subprocess.CalledProcessError:
        print("Failed to retrieve Git remote URL.")
        return None

    # Regular expression patterns for matching GitHub repository URLs
    ssh_pattern = r"^git@github\.com:([^/]+)/.*$"
    https_pattern = r"^https://github\.com/([^/]+)/.*$"

    # Check if the remote URL matches GitHub repository URL patterns
    if re.match(ssh_pattern, remote_url):
        owner_name = re.match(ssh_pattern, remote_url).group(1)
    elif re.match(https_pattern, remote_url):
        owner_name = re.match(https_pattern, remote_url).group(1)
    else:
        print("Remote URL is not a GitHub repository.")
        return None

    return owner_name


def get_token():
    token = None

    owner = get_github_owner_from_git()
    if owner is None:
        raise Exception("Unable to get the owner of the git project")

    gitconfig = configparser.ConfigParser()
    gitconfig.read(f"{os.getenv('HOME')}/.gitconfig")
    try:
        token = gitconfig.get('gitflow "token"', option=owner)
        if token and len(token) == 0:
            raise Exception(
                f'Github token of the owner "{owner}" is not configured correctly'
            )
    except configparser.NoOptionError as err:
        raise Exception(err.message)
    except configparser.NoSectionError as err:
        raise Exception(err.message)

    return token
