# Git & GitHub Workshop -hi

## Intro
> _ADD LATER_

## Installing Git & GitHub CLI

To install **Git** based on your OS:

- **Windows**: [https://git-scm.com/downloads/win](https://git-scm.com/downloads/win)
- **Ubuntu**:  
  ```bash
  sudo apt-get install git
   ```

- **Fedora**:
  For Fedora 21 and below:

  ```bash
  sudo yum install git
  ```

- For Fedora 22 and above:

  ```bash
  sudo dnf install git
  ```
- **macOS**:

  ```bash
  brew install git
  ```
  
To install **GitHub CLI** (gh): [https://github.com/cli/cli#installation](https://github.com/cli/cli#installation)


---

## Setting up Git & GitHub CLI

After installing Git, configure your user information and default branch:

```bash
# Check Git version
git --version

# Set your Git username
git config --global user.name "Your Name"

# Set your Git email
git config --global user.email "your.email@example.com"

# Set 'main' as the default branch for new repos
git config --global init.defaultBranch main

# Authenticate GitHub CLI
gh auth login
```
---

## Git Commands

```bash
# Initializing a repository
git init

# Checking the current state of the repo
git status

# Adding a single file to the staging area
git add file-name

# Adding all files to the staging area
git add .

# Committing staged changes with a message
git commit -m "your commit message"

# Viewing commit history
git log

# Viewing commit history in short form
git log --oneline

# Checking the differences between working directory and last commit
git diff

# Restoring a modified file to the last committed version
git restore file-name

# Removing a file from the staging area (unstage)
git restore --staged file-name
````

---

## GitHub Integration

```bash
# Connecting local repo to GitHub
git remote add origin https://github.com/your-username/your-repo.git

# Renaming the default branch to main (if needed)
git branch -M main

# Pushing commits to GitHub
git push origin main

# Cloning a repository from GitHub
git clone https://github.com/some-user/some-repo.git

# Pulling latest changes from the main branch
git pull origin main

# Fetching changes from the remote without merging them into your current branch
git fetch
```

---

## Branching

```bash
# List all branches
git branch

# Create a new branch
git branch new-branch

# List all branches (local + remote)
git branch -a

# Switch to a branch (existing)
git switch branch-name

# Create and switch to a new branch (shortcut)
git switch -c new-branch

# OR using older syntax
git checkout -b new-branch

# Rename a branch (while on it)
git branch -m new-name

# Delete a local branch (only if merged)
git branch -d branch-name
```

### Combining Branches
```bash
# Merging another branch into your current branch
git merge branch-name

# Rebase your current branch on top of another branch
git rebase branch-name
```

---
## Undoing Commits and Fixing Mistakes
```bash
# Edit last commit message
git commit --amend

# Undo last commit, keep changes staged
git reset --soft HEAD~1

# Undo last commit, unstage changes
git reset --mixed HEAD~1

# Undo last commit and discard changes (careful!)
git reset --hard HEAD~1
```

---
## Working with Stash

```bash
# Save your uncommitted changes temporarily
git stash

# List all stashed entries
git stash list

# Re-apply the most recent stash and remove it
git stash pop

# Apply without removing from stash list
git stash apply

```
---

## Best Practices for Commit Messages

| Prefix   | Purpose                                                      |
|----------|--------------------------------------------------------------|
| `fix:`   | Bug fixes or small corrections in code                      |
| `feat:`  | New features or enhancements                                |
| `ref:`   | Code refactoring (changing structure without changing behavior) |
| `chore:` | Maintenance tasks, code cleanup, or setup improvements      |
| `add:`   | Adding new technologies, libraries, or configurations       |
| `break:` | Breaking changes, usually in global config or API           |
| `doc:`   | Documentation updates                                       |

### Examples:
```bash
git commit -m "fix: fixed a piece of code crashing on load"
git commit -m "feat: added user profile feature"
git commit -m "ref: simplified logic in signup controller"
git commit -m "chore: cleaned up unused imports"
git commit -m "add: introduced ESLint and Prettier configs"
git commit -m "break: updated global config to new API structure"
git commit -m "doc: added setup instructions to README"
```
---

## How to Make a Pull Request (PR)

Follow these steps to contribute to a project by making a Pull Request:

1. **Fork the repository on GitHub**  
   Go to the original repository and click the **"Fork"** button at the top-right corner.  
   This creates a copy of the repository under your GitHub account.

2. **Clone your fork to your local machine**
   ```bash
   git clone https://github.com/your-username/the-repo-name.git
   cd the-repo-name
    ```

3. **Create a new branch for your changes**

   ```bash
   git checkout -b your-feature-branch
   ```

4. **Make your changes and commit them**

   ```bash
   git add .
   git commit -m "feat: meaningful commit message"
   ```

5. **Push your branch to your fork on GitHub**

   ```bash
   git push origin your-feature-branch
   ```

6. **Open a Pull Request on GitHub**

   * Go to your forked repository on GitHub.
   * Click the **"Compare & pull request"** button.
   * Add a **clear title** and **description** explaining what your PR does. (Refer to [Good Things to Mention in a Pull Request (PR)](#good-things-to-mention-in-a-pull-request-pr))
   * Click **"Create pull request"**.

---

## Good Things to Mention in a Pull Request (PR)

When opening a Pull Request on GitHub, it’s important to clearly explain what your code does. This helps maintainers review your work faster and improves your chances of getting it merged.

### Include the Following in Your PR:

1. **Description**  
   Briefly describe what changes you made and why.  
2. **Screenshot** (if applicable)  
   Include before/after screenshots or a small GIF if your change affects the UI.
3. **Issue it Resolves**  
   Link the issue your PR fixes (if any). Use the format:  
```
Fixes #12 (#12 means issue number 12)
Closes #5
Resolves #8
```
4. **Features to Add (Optional)**  
If your PR lays the groundwork for upcoming features, mention them here.

6. **Tag Maintainers (Optional)**  
If you want feedback or a quicker review, you can politely tag the project maintainers using `@username`.


---

Bonus Tips:

- Be polite and clear in your PR description.
- Use bullet points or markdown formatting for readability.
- If your PR is still a work in progress, add `[WIP]` to the title or use GitHub’s draft PR feature.

---

## Workshop Conducted By

> _To be added_

---
