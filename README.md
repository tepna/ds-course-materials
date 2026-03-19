# Data Science



## How to Get Started?  

- Install Python & Jupyter Notebook (`pip install jupyter` & `jupyter notebook`)
- Use Poetry (For Dependency Management)
- Use Conda (For Managing Python & Libraries)
- No Installation Needed: Google Colab (For Cloud-Based Learning) [Google Colab](https://colab.research.google.com/)

## SSH Key Setup in Visual Studio Code

### 1. Open VS Code → Terminal
### 2. Generate SSH key:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
````
### 3. Start agent & add key:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
```
### 4. Copy key:

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
### 5. Add it to [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)


## Installation Instructions

### 1. Clone the Repository

Clone this repository using:

```bash
git clone <repo_url>
```

Replace `<repo_url>` with the actual URL of your repository.

### 2. Navigate to the Project Directory

Change into the project directory:

```bash
cd ds-course-materials
```

### 3. Install Dependencies

Inside the project directory, install all dependencies using Poetry:

```bash
poetry install
```

This command will read your `pyproject.toml` file, create a virtual environment (if one doesn't exist), and install the required packages.

### 4. Running Your Notebooks

If your project includes Jupyter notebooks, you can start Jupyter Lab using Poetry. Make sure you've installed all project dependencies and then run:

```bash
poetry run jupyter lab
```

This command will launch Jupyter Lab in your default browser, allowing you to open and run your notebooks interactively.

---

## Git Basics

Use this guide to push your homework to a separate branch, then sync with `main`.

### One-time setup

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### Git Clone (first time)

```bash
git clone <REPO_URL>
cd <repo-folder>
```

### Create a new branch

```bash
# Newer syntax
git switch -c homework/name

# or classic
git checkout -b homework/name
```

### Check current branch

```bash
git branch
```

### Status, stage, commit, push

```bash
git status
git add path/to/files     # or: git add .
git commit -m "Add homework: EDA"
git push
```

### Switch to `main` and pull latest

```bash
git switch main           # or: git checkout main
git pull --ff-only        # or: git pull --rebase
```

---

## Quick reference

```bash
git branch                   # local branches
git branch -a                # local + remote
git switch <branch>          # switch
git checkout -b <branch>     # create + switch (classic)
git status                   # what changed
git add <file>               # stage
git commit -m "message"      # commit
git pull                     # fetch + merge/rebase
git fetch                    # only download
git push                     # upload commits
git log --oneline --graph    # compact history
```
---

## Marimo
```bash
poetry run marimo edit 
```
Launches the Marimo notebook editor using the virtual environment managed by Poetry.
It opens the Marimo interface and lets you browse or create notebooks interactively.

You can also open a specific folder or notebook directly:

```bash
poetry run marimo edit notebooks/marimo
```
