
# Virtual Environments (venv)
- A virtual environment provides an isolated Python environment for our project with its own installed packages.
- We donot need to install 'venv' separately. When you install Python, it already includes a built-in module called venv. We can use that to create a virtual environment for our project.
- Each virtual environment (venv) has its own Python interpreter executable and its own installed packages.

    ## Create, activate and deactivate a venv 
    - Create : ``python3 -m venv .venv``
    - Activate : ``source .venv/bin/activate``
    - Deactivate : ``deactivate`` : Run deactivate only when a virtual environment is currently active.
    - Verify the active Python interpreter : ``python3 -c 'import sys; print(sys.executable)'``

    **Imp note** - Changing folders with cd does NOT automatically change virtual environments. You must explicitly deactivate the old environment and activate the desired one.

    ## Other commands : 
    - ``python3 -m pip --version`` // Identifies pip's version and Python installation
    - ``python3 -m pip list`` // Lists installed packages and their versions
    - ``python3 -m pip show pytest`` // Displays details about the installed pytest package
    

    ## Understanding requirements.txt :
    - This is one of the most important Python dependency-management skills.
    - Imagine an engineer clones my EvalKit repository from GitHub. They receive my Python source code, but they won't receive my virtual environment, because we exclude it from Git. How will they know which Python packages to install. That's one purpose of requirements.txt
    - ``python3 -m pip freeze`` - This outputs installed packages in a format suitable for a requirements.txt file
    - ``python3 -m pip freeze > requirements.txt`` - Creates or overwrites the file with the current dependency snapshot (You can also use the traditional 'nano' and 'cat' terminal commands to create, write and view the contents but the above command is much easier)

    - There are 2 categories of dependencies :
        - **Direct dependencies**: Packages your project explicitly needs, such as pytest and python-dotenv.
        - **Transitive dependencies**: Packages required by your direct dependencies.

    ## Recreating an Environment
    - If an engineer clones my Python project from GitHub. They receive:
        - My Python source code.
        - My test files.
        - My requirements.txt.
    But they don't receive your .venv directory because Git ignores it.
    How do they recreate an equivalent Python environment using only the project files and requirements.txt.

    - The installation command: ``python3 -m pip install -r requirements.txt``. So once you are in a new project with a newly created venv, run the command and then verify 'python3 -m pip list' 