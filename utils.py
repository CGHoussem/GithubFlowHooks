import os
import sys
import re
import subprocess
import configparser


def get_github_owner_from_git():
    # Get the remote URL of the Git repository
    try:
        remote_url_bytes = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])
        remote_url = remote_url_bytes.decode().strip()
    except subprocess.CalledProcessError:
        print("Failed to retrieve Git remote URL.")
        return None

    # Regular expression patterns for matching GitHub repository URLs
    ssh_pattern = r'^git@github\.com:([^/]+)/.*$'
    https_pattern = r'^https://github\.com/([^/]+)/.*$'

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
        print('Unable to get the owner of the git project', file=sys.stderr)
        return None

    gitconfig = configparser.ConfigParser()
    gitconfig.read(f'{os.getenv("HOME")}/.gitconfig')
    try:
        token = gitconfig['gitflow "token"'][owner]
        if token and len(token) == 0:
            print(f'Github token of the owner "{owner}" is not configured correctly', file=sys.stderr)
            return None
    except KeyError:
        print(f'Unable to get the github token from gitconfig for the owner: {owner}', file=sys.stderr)
        return None
    
    return token

