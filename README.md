# Data Science



## How to Get Started?  
- No Installation Needed: Google Colab (For Cloud-Based Learning) [Google Colab](https://colab.research.google.com/)
- Install VS Code → install Python → install Poetry → install Git → clone repository → connect Poetry to Python → open in VS Code.

### Project Setup on Windows

This guide explains how to set up the project on **Windows** with:

- **Visual Studio Code**
- **Python 3.13.2**
- **pyenv-win**
- **Poetry**
- **Git**

### 1. Install Visual Studio Code

Download and install [Visual Studio Code](https://code.visualstudio.com/docs?dv=win).

After installation, open VS Code and install the following extensions:

- **Python** (by Microsoft)
- **Pylance** (by Microsoft)

### 2. Install `pyenv-win`

Open **PowerShell** and run:

```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
````

Close and reopen PowerShell, then check:

```powershell
pyenv --version
```

### 3. Install Python 3.13.2

Install the required Python version:

```powershell
pyenv install 3.13.2
pyenv global 3.13.2
```

Verify the installation:

```powershell
python --version
python -c "import sys; print(sys.executable)"
```

Expected output:

```text
Python 3.13.2
```

### 4. Install Poetry

Run the following command in **PowerShell**:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Check that Poetry is installed:

```powershell
poetry --version
```

### 5. Install Git

Install [Git for Windows](https://git-scm.com/install/windows) with:

```powershell
winget install --id Git.Git -e --source winget
```

Verify the installation:

```powershell
git --version
```

Configure your Git identity once:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### 6. SSH Key Setup for GitHub

Generate a new SSH key:

```powershell
ssh-keygen -t ed25519 -C "your_email@example.com"
```

When prompted for the file location, press **Enter** to use the default path.

Then add your key:

```powershell
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

```powershell
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

Show the public key and copy it:

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub
```

Add the copied public key to your [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) account.

### 7. Clone the Repository

Go to the folder where you want to store the project and clone it.

### HTTPS

```powershell
cd C:\Users\YourName\source\repos
git clone <repo_url>
cd ds-course-materials
```

### SSH

```powershell
cd C:\Users\YourName\source\repos
git clone git@github.com:OWNER/REPOSITORY.git
cd ds-course-materials
```

Replace `<repo_url>` or the SSH URL with the actual repository URL.

### 8. Configure the Project Python Version

Inside the repository, set the local Python version:

```powershell
pyenv local 3.13.2
python --version
```

### 9. Create the Poetry Environment

Configure Poetry to create the virtual environment inside the project folder:

```powershell
poetry config virtualenvs.in-project true --local
```

Create the environment with Python 3.13.2 and install dependencies:

```powershell
poetry env use 3.13.2
poetry install
```

If needed, you can also point Poetry to a specific Python executable:

```powershell
poetry env use "$env:USERPROFILE\.pyenv\pyenv-win\versions\3.13.2\python.exe"
poetry install
```

### 10. Open the Project in VS Code

From the repository folder, run:

```powershell
code .
```

In VS Code:

1. Press `Ctrl + Shift + P`
2. Search for **Python: Select Interpreter**
3. Choose the interpreter from:

```text
ds-course-materials\.venv\Scripts\python.exe
```

### 11. Verify the Setup

Run the following commands inside the project:

```powershell
python --version
poetry --version
poetry env info
poetry run python --version
```

## Running Your Notebooks

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
