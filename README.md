# Git-extractor

Small python script to retrieve interesting data from a .git folder.

```git config --list``` : Get all repository configurations.

```git log ```: List commits with details of author, date, and message.

```git branch -a``` : List all branches, including remote ones.

```git tag``` : List all tags.

```git show -s HEAD~5..HEA``` : Show details of the last 5 commits.

```git log --format='%aN <%aE>``` | sort -u : List all unique authors.

```git ls-files``` : List all files tracked by Git.

```git diff```: Show uncommitted changes.

```git diff --cached```: Show changes in the staging area.

```git log -p```: Show full history with details of changes in each commit.

```git --version```: Show the installed Git version.

```git remote -v```: Show information about the remote repository (origin, etc.).

# Usage

```git clone https://github.com/mqueguin/git-extractor.git && cd git-extractor```

```python3 git_extractor.py path/to/.git```
