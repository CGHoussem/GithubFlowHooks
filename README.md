# GitHub Flow Hooks

These hooks are designed to automate the process of gitflow when the git repository is hosted at GitHub.

It helps creating Pull Requests, merging them when finishing a feature, bugfix, hotfix or a release; etc..

## Requirements

In order for the hooks to function, a github PAT that has access to the GitHub project should be present in the `
~.gitconfig` file.

Here is an example on how to setup up the token in the `.gitconfig` file:

```
[gitflow "token"]
	<PROJECT OWNER> = <INSERT PAT HERE>
```

The <PROJECT OWNER> is the owner/namespace of the GitHub project; The owner of a GitHub project can be extracted from it's URL.

Let's take this repository as an example:

- URL: <https://github.com/CGHoussem/GithubFlowHooks>

The owner of the "GithubFlowHooks" project is "CGHoussem"


**The PAT should at least have the "Pull requests" and "Contents" _Read and write_ repository permissions.**

## Additional features


1. The `latest` tag

You may need the need to create a latest tag to your hotfixes / releases. This is achievable by adding the option `use-latest` to the gitflow options config, like so:

```
[gitflow "options"]
	use-latest = true
```

For the boolean gitflow options:

- The **true** values can be expressed using the following values: '1', 'yes', 'true', 'on'
- The **false** values can be expressed using the following values: '0', 'no', 'false', 'off'
