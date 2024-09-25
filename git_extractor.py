import os
import subprocess
import sys

def run_command(command, git_folder_path):
    try:
        result = subprocess.run(command, cwd=git_folder_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Error running command {command}: {e}")
        return None

def extract_git_info(git_folder_path):
    # Configuration générale
    config = run_command("git config --list", git_folder_path)
    if config:
        print("\n--- Configuration ---\n")
        print(config)

    # Liste des commits
    commits = run_command("git log --pretty=format:'%h - %an, %ar : %s'", git_folder_path)
    if commits:
        print("\n--- Historique des commits ---\n")
        print(commits)

    # Liste des branches
    branches = run_command("git branch -a", git_folder_path)
    if branches:
        print("\n--- Branches ---\n")
        print(branches)

    # Liste des tags
    tags = run_command("git tag", git_folder_path)
    if tags:
        print("\n--- Tags ---\n")
        print(tags)

    # Modifications récentes (derniers 5 commits)
    recent_changes = run_command("git show -s HEAD~5..HEAD", git_folder_path)
    if recent_changes:
        print("\n--- Modifications récentes ---\n")
        print(recent_changes)

    # Liste des auteurs
    authors = run_command("git log --format='%aN <%aE>' | sort -u", git_folder_path)
    if authors:
        print("\n--- Auteurs ---\n")
        print(authors)

    # Liste des fichiers suivis par git
    tracked_files = run_command("git ls-files", git_folder_path)
    if tracked_files:
        print("\n--- Fichiers suivis par Git ---\n")
        print(tracked_files)

    # Contenu des fichiers non commités
    unstaged_diff = run_command("git diff", git_folder_path)
    if unstaged_diff:
        print("\n--- Changements non commités ---\n")
        print(unstaged_diff)

    # Fichiers dans le staging area
    staged_diff = run_command("git diff --cached", git_folder_path)
    if staged_diff:
        print("\n--- Changements en attente de commit (staging area) ---\n")
        print(staged_diff)

    # Log complet avec détails des changements
    full_log = run_command("git log -p", git_folder_path)
    if full_log:
        print("\n--- Log complet avec détails des changements ---\n")
        print(full_log)

    # Récupération de la version Git et des informations du dépôt
    version = run_command("git --version", git_folder_path)
    if version:
        print("\n--- Version Git ---\n")
        print(version)

    repo_info = run_command("git remote -v", git_folder_path)
    if repo_info:
        print("\n--- Informations du dépôt ---\n")
        print(repo_info)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} /path/to/.git")
        sys.exit(1)

    git_folder_path = sys.argv[1]

    if os.path.exists(git_folder_path):
        extract_git_info(git_folder_path)
    else:
        print(f"Le dossier {git_folder_path} n'existe pas.")

